from src.Taquin import Taquin
from src.utils.Tree import Tree


class TaquinAStar(Taquin):
    def __init__(
        self,
        heuristique: int,
        grid: list[list[int]] = [[4, 5, 1], [2, 8, 3], [7, 6, 0]],
        verbose: bool = False,
    ):
        """
        Initialise une instance de la classe taquin_a_star.

        Cette classe est héritée de la classe taquin et utilise
        l'algorithme A* pour résoudre le puzzle (taquin).

        Args:
            heuristique: `0` pour l'heuristique de `Hamming` ou `1` pour celle
            de `Manhattan`.
        """

        super().__init__(grid)
        self.heuristique = heuristique
        self.verbose = verbose

    def d_hamming(self, grid: list):
        """
        Calcule la distance de Hamming entre la grille actuelle et la grille
        cible.

        Args:
            grid: La grille pour laquelle calculer la distance.
        """
        d = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] != self.goal_grid[x][y]:
                    d += 1
        return d

    def d_manhattan(self, grid: list):
        """
        Calcule la distance de Manhattan entre la grille actuelle et la grille
        cible.

        Args:
            grid: La grille pour laquelle calculer la distance.
        """
        d = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                (goal_x, goal_y) = self.find_index(self.goal_grid, grid[x][y])
                d += abs(x - goal_x) + abs(y - goal_y)

        return d

    def d(self, grid: list):
        """
        Calcule la distance entre la grille actuelle et la grille cible en
        tenant compte de la distance choisie (Manhattan ou Hamming).

        Args:
            grid: La grille pour laquelle calculer la distance.

        Returns:
            La distance entre la grille actuelle et la grille cible.
        """
        if self.heuristique == 0:
            return self.d_hamming(grid)
        else:
            return self.d_manhattan(grid)

    def solve(self):
        """
        Résout le puzzle en utilisant l'algorithme A*.

        Returns:
            La grille résolue ou `None` si aucune solution n'a été trouvée.
        """

        if self.is_solved(self.get_grid()):
            return True
        heuristique = self.d(self.get_grid())
        solver = Tree(None, self.get_grid(), heuristique)

        visited_states = set()  # set of visited states (avoid infinite loops)
        while not self.is_solved(solver.get_current_node()):
            # find the position of the empty space
            (x, y) = self.find_index(self.get_grid(), 0)
            # Try to move the empty space in every direction
            # Add to the tree if the move is valid
            for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                # clone the current taquin to try the move
                clone = self.clone()
                if clone.move(*move):
                    # Convert the grid to a tuple to add to visited set
                    grid_tuple = tuple(map(tuple, clone.get_grid()))
                    if grid_tuple not in visited_states:
                        visited_states.add(grid_tuple)
                        # if the move is valid, add the new grid to the tree
                        # (child to current node)
                        solver.add_node(
                            Tree(
                                solver,
                                clone.get_grid(),
                                clone.d(clone.get_grid()),
                            )
                        )

            # get solver child_node with min heuristique
            if solver.get_nodes():
                solver = min(
                    solver.get_nodes(), key=lambda node: node.get_heuristique()
                )
                # Set the current grid to the grid with the min heuristique
                self.set_grid(solver.get_current_node())
                if self.verbose:
                    print(self)  # see the solving process
            else:
                if solver is not None:
                    # Remove the node with the min heuristique to try another
                    # combination
                    solver = solver.get_root()
                    solver.pop_child_min_heuristique()
                else:
                    print("No solution found")
                    return None

        return self
