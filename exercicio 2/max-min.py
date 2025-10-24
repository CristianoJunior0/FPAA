def maxmin_select(lista):
    n = len(lista)

    # Caso base: lista com 1 elemento
    if n == 1:
        return lista[0], lista[0]

    # Caso base: lista com 2 elementos
    if n == 2:
        if lista[0] < lista[1]:
            return lista[0], lista[1]
        else:
            return lista[1], lista[0]

    # Divide a lista ao meio
    meio = n // 2
    min_esq, max_esq = maxmin_select(lista[:meio])
    min_dir, max_dir = maxmin_select(lista[meio:])

    # Combina os resultados
    menor = min(min_esq, min_dir)
    maior = max(max_esq, max_dir)

    return menor, maior


if __name__ == "__main__":
    lista = [4, 2, 9, 1, 7, 6, 3]
    print("Lista:", lista)
    menor, maior = maxmin_select(lista)
    print("Menor elemento:", menor)
    print("Maior elemento:", maior)
