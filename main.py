from src.TaquinAStar import TaquinAStar
import time

if __name__ == '__main__':
    # On peut utiliser l'heuristique de Hamming
    start_time = time.time()
    taquin_hamming = TaquinAStar(0)
    taquin_hamming.solve()
    elapsed_time = time.time() - start_time
    print("Temps d'exécution avec l'heuristique de Hamming: %s secondes" % elapsed_time)

    # On peut aussi utiliser l'heuristique de Manhattan
    start_time = time.time()
    taquin_manhattan = TaquinAStar(1)
    taquin_manhattan.solve()
    elapsed_time = time.time() - start_time
    print("Temps d'exécution avec l'heuristique de Manhattan: %s secondes" % elapsed_time)