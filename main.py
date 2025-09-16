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

def depthFirstSearch(grafo, inicio, objetivo, custoTotal, visitados=None, caminho=None):
    if visitados is None:
        visitados = set()  # conjunto para marcar cidades já visitadas
    if caminho is None:
      caminho = []

    caminho.append(inicio)
    visitados.add(inicio)

    if inicio == objetivo:
        return caminho, custoTotal

    for vizinho, custo in grafo.get(inicio, {}).items():
        if vizinho not in visitados:
            novoCaminho, custoViagem = depthFirstSearch(grafo, vizinho, objetivo, custoTotal + custo, visitados, caminho )

            if novoCaminho:
                return novoCaminho, custoViagem

    caminho.pop()   # remove o último nó (backtracking) se não deu certo


    return None, None

inicial = "Pelotas"
destino = "Porto Alegre"
caminho, custo = depthFirstSearch(GRAPH, inicial, destino, 0)
print(caminho, f"Custo: {custo}")
def bestFirst(grafo, inicio, objetivo):
    fila = [(0, inicio, [inicio])]
    visitados = set()
    contador = 0

    while fila:
        menorCusto = float('inf')
        indiceMelhorNo = -1

        for i, (custoFila, noFila, caminhoFila) in enumerate(fila):
            if custoFila < menorCusto:
                menorCusto = custoFila
                indiceMelhorNo = i

        custoAtual, noAtual, caminho = fila.pop(indiceMelhorNo)

        if noAtual in visitados:
            continue

        visitados.add(noAtual)
        contador += 1 

        if noAtual == objetivo:
            return caminho, custoAtual, contador

        for vizinho, custoAresta in grafo.get(noAtual, {}).items():
            if vizinho not in visitados:
                novoCusto = custoAtual + custoAresta
                novoCaminho = list(caminho)
                novoCaminho.append(vizinho)
                fila.append((novoCusto, vizinho, novoCaminho))

    return None, 0, contador 

inicial = "Pelotas"
destino = "Porto Alegre"
caminho, custo, cidadesVisitadas = bestFirst(GRAPH2, inicial, destino)
print(f"Caminho: {caminho}, Custo: {custo}, Cidades visitadas: {cidadesVisitadas}")



def dijkstra(grafo, inicio, objetivo):
    dist = {}   # guarda o custo mínimo até cada cidade
    prev = {}   # guarda o "pai" de cada cidade (para reconstruir caminho)
    nao_visitados = set(grafo.keys())  # conjunto de cidades não visitadas

    maior = float('inf')  # valor "infinito" inicial

    # inicializa distâncias
    for no in grafo:
        dist[no] = maior   # todas começam com infinito
        prev[no] = None
    dist[inicio] = 0       # cidade inicial = custo zero

    # enquanto ainda tem cidade não visitada
    while nao_visitados:
        # pega a cidade com menor distância atual
        u = min(nao_visitados, key=lambda no: dist[no])
        nao_visitados.remove(u)

        if dist[u] == maior:  # se não tem caminho até u
            break
        if u == objetivo:     # se já chegou no destino, pode parar
            break

        # para cada vizinho da cidade atual
        for vizinho, custo in grafo.get(u, {}).items():
            alt = dist[u] + custo  # novo custo passando por u
            if alt < dist[vizinho]:  # se esse custo é menor
                dist[vizinho] = alt  # atualiza distância mínima
                prev[vizinho] = u    # registra o "pai"

    # reconstrução do caminho
    caminho = []
    u = objetivo
    while u is not None:    # volta pelo "prev" até o início
        caminho.insert(0, u)
        u = prev[u]

    return {"caminho": caminho, "custo": dist[objetivo]}