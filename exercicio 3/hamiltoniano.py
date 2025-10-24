def hamiltoniano(grafo, v, visitado, caminho):
    if len(caminho) == len(grafo):
        return caminho

    for vizinho in grafo[v]:
        if not visitado[vizinho]:
            visitado[vizinho] = True
            novo_caminho = hamiltoniano(grafo, vizinho, visitado, caminho + [vizinho])
            if novo_caminho:
                return novo_caminho
            visitado[vizinho] = False
    return None


def encontrar_caminho_hamiltoniano(grafo):
    for v in grafo:
        visitado = {vert: False for vert in grafo}
        visitado[v] = True
        caminho = hamiltoniano(grafo, v, visitado, [v])
        if caminho:
            return caminho
    return None


if __name__ == "__main__":
    grafo = {
        0: [1, 3],
        1: [0, 2, 3],
        2: [1, 3],
        3: [0, 1, 2]
    }

    caminho = encontrar_caminho_hamiltoniano(grafo)

    if caminho:
        print("Caminho Hamiltoniano encontrado:", caminho)
    else:
        print("Nenhum caminho Hamiltoniano encontrado.")
