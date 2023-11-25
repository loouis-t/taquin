from src.TaquinAStar import TaquinAStar
import time

if __name__ == "__main__":
    # On peut utiliser l'heuristique de Hamming
    start_time = time.time()
    taquin_hamming = TaquinAStar(0, verbose=False)
    taquin_hamming.solve()
    elapsed_time = time.time() - start_time
    print(
        "Temps d'exécution avec l'heuristique de Hamming: %s ms"
        % (elapsed_time * 1000)
    )

    # On peut aussi utiliser l'heuristique de Manhattan
    start_time = time.time()
    taquin_manhattan = TaquinAStar(1, verbose=True)
    taquin_manhattan.solve()
    elapsed_time = time.time() - start_time
    print(
        "Temps d'exécution avec l'heuristique de Manhattan: %s ms"
        % (elapsed_time * 1000)
    )
