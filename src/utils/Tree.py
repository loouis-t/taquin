class Tree:
    def __init__(self, root, current_node, heuristique):
        """
        Initialise un arbre vide.

        Args:
            root: La racine de l'arbre (noeud parent).
            current_node: Le noeud courant de l'arbre (grille courante).
            heuristique: heuristique de la grille courante par rapport a
            la grille cible
        """

        self.root: Tree = root
        self.current_node = current_node
        self.nodes: list[Tree] = []
        self.heuristique = heuristique

    def get_root(self):
        """
        Retourne la racine de l'arbre (noeud parent).
        """

        return self.root

    def set_root(self, root):
        """
        Définis la racine du noeud courant

        Args:
          root: racine du noeud courant
        """
        self.root = root

    def get_current_node(self):
        """
        Retourne le noeud courant de l'arbre (grille courante).
        """

        return self.current_node

    def set_current_node(self, current_node):
        """
        Définis le noeud courant (grille courante)

        Args:
          current_node: noeud courant (grille courante)
        """
        self.current_node = current_node

    def get_nodes(self):
        """
        Retourne la liste des fils du noeud courant.
        """

        return self.nodes

    def add_node(self, node):
        """
        Définis les fils du noeud courant

        Args:
            node: noeud fils du noeud courant
        """
        self.nodes.append(node)

    def get_heuristique(self):
        """
        Retourne l'heuristique de la grille courante
        """
        return self.heuristique

    def set_heuristique(self, heuristique):
        """
        Définis l'heuristique du noeud courant (grille courante)

        Args:
            heuristique: heuristique du noeud courant (grille courante)
        """
        self.heuristique = heuristique

    def pop_child_min_heuristique(self):
        """
        Retire le fils du noeud courant avec l'heuristique la plus faible (cas 
        où il ne mène pas à la solution)
        """
        child_min_heuristique = self.get_nodes()[0]
        for child in self.get_nodes():
            if child.get_heuristique() < child_min_heuristique.get_heuristique():
                child_min_heuristique = child
        self.get_nodes().remove(child_min_heuristique)
