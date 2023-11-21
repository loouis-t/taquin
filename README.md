# Jeu de Taquin

Jeu de Taquin utilisant l'algorithme `A*` pour trouver la solution.
Il utilise l'heuristique de la distance de `Manhattan` et de la distance de `Hamming`.

## Démarrer le jeu

Le fichier `main.py` contient le code pour lancer le jeu.  
Il utilise le mélange par défaut et chronomètre le temps de résolution avec l'algorithme `A*` (en utilisant la distance de `Manhattan`, et la distance de `Hamming`).

```bash
python3 main.py

(ou <your_python_command> main.py)
```

## Changer le mélange de départ

Le mélange de départ est défini dans le constructeur de la classe `Taquin` (`src/Taquin.py`) et dans la classe héritée de celle-ci `TaquinAStar` (`src/TaquinAStar.py`).  
Pour changer le mélange, il suffit d'en passer une en paramètre du constructeur (et ainsi ne pas utiliser le paramètre par défaut).

**Attention :**
La grille passée en paramètre doit être une grille valide (problème de parité).

```python
# main.py

# votre_grille_de_depart avec exactement un "n" à 0 (case vide), exemple :
votre_grille_de_depart = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Remplacer
taquin_hamming = TaquinAStar(0)
# Par
taquin_hamming = TaquinAStar(0, votre_grille_de_depart)
```
