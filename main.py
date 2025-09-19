import heapq
from collections import deque

# ----------------- GRAFOS -----------------
GRAPH = {
    "Pelotas": {"Camaquã": 150, "Rio Grande": 55, "Bagé": 180, "Santa Maria": 370},
    "Camaquã": {"Pelotas": 150, "Guaíba": 68, "Porto Alegre": 125},
    "Guaíba": {"Camaquã": 65, "Porto Alegre": 30},
    "Porto Alegre": {"Guaíba": 30, "Camaquã": 125, "Rio Grande": 320, "Bagé": 380, "Santa Maria": 290},
    "Rio Grande": {"Pelotas": 55, "Porto Alegre": 320},
    "Bagé": {"Pelotas": 180, "Porto Alegre": 380},
    "Santa Maria": {"Pelotas": 370, "Porto Alegre": 290}
}

GRAPH2 = {
    "Pelotas": {"Camaquã": 150, "Rio Grande": 55, "Bagé": 180, "Santa Maria": 370, "Alegrete": 100},
    "Camaquã": {"Pelotas": 150, "Guaíba": 68, "Porto Alegre": 125},
    "Guaíba": {"Camaquã": 65, "Porto Alegre": 30},
    "Porto Alegre": {"Guaíba": 30, "Camaquã": 125, "Rio Grande": 320, "Bagé": 380, "Santa Maria": 290, "Alegrete": 120},
    "Rio Grande": {"Pelotas": 55, "Porto Alegre": 320},
    "Bagé": {"Pelotas": 180, "Porto Alegre": 380},
    "Santa Maria": {"Pelotas": 370, "Porto Alegre": 290},
    "Alegrete": {"Pelotas": 100, "Porto Alegre": 120}
}

# ----------------- DFS -----------------
def depth_first(grafo, inicio, objetivo, visitados=None, caminho=None, custo=0):
    if visitados is None:
        visitados, caminho = set(), []

    caminho.append(inicio)
    visitados.add(inicio)

    if inicio == objetivo:
        return caminho[:], custo, len(visitados)

    for vizinho, peso in grafo.get(inicio, {}).items():
        if vizinho not in visitados:
            result = depth_first(grafo, vizinho, objetivo, visitados, caminho, custo + peso)
            if result[0]:
                return result

    caminho.pop()  # backtracking
    return [], 0, len(visitados)

# BFS 
def breadth_first(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])  # (nó atual, caminho até aqui)
    visitados = set()

    while fila:
        no, caminho = fila.popleft()

        if no in visitados:
            continue
        visitados.add(no)

        if no == objetivo:
            return caminho, len(caminho) - 1, len(visitados)

        for vizinho in grafo[no]:
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))

    return [], 0, len(visitados)

# Best-First 
def best_first(grafo, inicio, objetivo):
    fila = [(0, inicio, [inicio])]
    visitados = set()

    while fila:
        custo, no, caminho = heapq.heappop(fila)

        if no in visitados:
            continue

        visitados.add(no)

        if no == objetivo:
            return caminho, custo, len(visitados)

        for vizinho, peso in grafo.get(no, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))

    return [], 0, len(visitados)

#  Dijkstra 
def dijkstra(grafo, inicio, objetivo):
    dist = {no: float('inf') for no in grafo}
    prev = {no: None for no in grafo}
    dist[inicio] = 0
    fila = [(0, inicio)]
    visitados = set()

    while fila:
        custo, no = heapq.heappop(fila)

        if no in visitados:
            continue
        visitados.add(no)

        if no == objetivo:
            break

        for vizinho, peso in grafo[no].items():
            novo_custo = custo + peso
            if novo_custo < dist[vizinho]:
                dist[vizinho] = novo_custo
                prev[vizinho] = no
                heapq.heappush(fila, (novo_custo, vizinho))

    caminho, atual = [], objetivo
    while atual:
        caminho.insert(0, atual)
        atual = prev[atual]

    return caminho, dist[objetivo], len(visitados)

#  TESTES 
if __name__ == "__main__":
    inicio, destino = "Pelotas", "Porto Alegre"

    print("DFS:", depth_first(GRAPH, inicio, destino))
    print("BFS:", breadth_first(GRAPH, inicio, destino))
    print("Best-First:", best_first(GRAPH2, inicio, destino))
    print("Dijkstra:", dijkstra(GRAPH, inicio, destino))
