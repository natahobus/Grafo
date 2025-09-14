function bfs(grafo, inicio, objetivo) {
  let fila = [[inicio]];
  let visitados = new Set();

  while (fila.length > 0) {
    let caminho = fila.shift();
    let no = caminho[caminho.length - 1];

    if (no === objetivo) return caminho;

    if (!visitados.has(no)) {
      visitados.add(no);
      for (let vizinho in grafo[no]) {
        fila.push([...caminho, vizinho]);
      }
    }
  }
  return null;
}

module.exports = bfs;
