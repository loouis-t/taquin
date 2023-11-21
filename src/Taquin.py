from copy import deepcopy

class Taquin:
    def __init__(self, grid: list[list[int]] = [
            [4, 5, 1], 
            [2, 8, 3], 
            [7, 6, 0]
        ]):
        self.grid = grid
        self.goal_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_index(self, goal_grid, value: int):
        """
        Trouve la position d'une valeur dans une grille (liste de listes).

        Args:
            goal_grid: La grille dans laquelle chercher.
            value: La valeur à chercher.
        """

        for x in range(len(goal_grid)):
            for y in range(len(goal_grid[x])):
                if goal_grid[x][y] == value:
                    return (x, y)

        return (-1, -1)

    def move(self, move_x: int, move_y: int):
        """
        Déplace une case dans la grille, si le déplacement est valide.

        Args:
            x: La position en x de la case à déplacer.
            y: La position en y de la case à déplacer.
            move_x: Le déplacement en x de la case.
            move_y: Le déplacement en y de la case.
        """
        # Find the position of the empty space
        (x, y) = self.find_index(self.grid, 0)

        # Check if the move is valid (inside of grid and not diagonal)
        if (
            # move is diagonal
            (move_x == 0 and move_y == 0)
            or (move_x != 0 and move_y != 0)
            # move is outside of grid
            or (y + move_y < 0 or y + move_y >= len(self.grid))
            or (x + move_x < 0 or x + move_x >= len(self.grid[0]))
            # move is more than one
            or abs(move_x) > 1
            or abs(move_y) > 1
        ):
            return False

        # Move to the new position
        self.grid[x][y] = self.grid[x + move_x][y + move_y]
        self.grid[x + move_x][y + move_y] = 0

        return True

    def is_solved(self, grid: list):
        """
        Vérifie si la grille actuelle est la grille cible.
        """
        return grid == self.goal_grid

    def get_grid(self):
        """
        Retourne la grille actuelle.
        """
        return self.grid
    
    def set_grid(self, grid: list):
        """
        Définis la grille actuelle.

        Args:
            grid: La grille à définir.
        """
        self.grid = grid

    def __str__(self):
        formatted_res = " _______\n"
        for x in self.grid:
            formatted_res += (
                "| " + str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + " |\n"
            )
        formatted_res += " -------"

        return formatted_res.replace("0", " ")
    
    def clone(self):
        """
        Crée une copie indépendante de l'objet TaquinAStar actuel.
        """
        return deepcopy(self)


# game = Taquin()
# print(game)

# print(game.move(0, 1))
# print(game)
# print(game.move(1, 1, -1, 0))
# print(game)

# print(game.is_solved())