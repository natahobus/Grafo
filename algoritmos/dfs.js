function dfs(grafo, inicio, objetivo, visitados = new Set(), caminho = []) {
  caminho.push(inicio);
  visitados.add(inicio);

  if (inicio === objetivo) return caminho;

  for (let vizinho in grafo[inicio]) {
    if (!visitados.has(vizinho)) {
      let novoCaminho = dfs(grafo, vizinho, objetivo, visitados, [...caminho]);
      if (novoCaminho) return novoCaminho;
    }
  }
  return null;
}

module.exports = dfs;
