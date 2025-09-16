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
  dist = {}
  prev = {}
  nao_visitados = set(grafo.keys())

  maior = float('inf')

  for no in grafo:
      dist[no] = maior
      prev[no] = None
  dist[inicio] = 0

  while nao_visitados:
      u = min(nao_visitados, key=lambda no: dist[no])
      nao_visitados.remove(u)

      if dist[u] == maior:
          break

      if u == objetivo:
          break

      for vizinho, custo in grafo.get(u, {}).items():
          alt = dist[u] + custo
          if alt < dist[vizinho]:
              dist[vizinho] = alt
              prev[vizinho] = u

  caminho = []
  u = objetivo
  while u is not None:
      caminho.insert(0, u)
      u = prev[u]

  return {"caminho": caminho, "custo": dist[objetivo]}

inicial = "Pelotas"
destino = "Porto Alegre"
resultado = dijkstra(GRAPH2, inicial, destino)
print(f"Caminho: {resultado['caminho']} Custo: {resultado['custo']}")