function dijkstra(grafo, inicio, objetivo) {
  let dist = {};
  let prev = {};
  let naoVisitados = new Set(Object.keys(grafo));

  for (let no in grafo) {
    dist[no] = Infinity;
    prev[no] = null;
  }
  dist[inicio] = 0;

  while (naoVisitados.size > 0) {
    let u = [...naoVisitados].reduce((a, b) => dist[a] < dist[b] ? a : b);
    naoVisitados.delete(u);

    if (u === objetivo) break;

    for (let vizinho in grafo[u]) {
      let alt = dist[u] + grafo[u][vizinho];
      if (alt < dist[vizinho]) {
        dist[vizinho] = alt;
        prev[vizinho] = u;
      }
    }
  }

  let caminho = [];
  let u = objetivo;
  while (u) {
    caminho.unshift(u);
    u = prev[u];
  }

  return { caminho, custo: dist[objetivo] };
}

module.exports = dijkstra;
// Exporta a função para ser usada em outros arquivos 