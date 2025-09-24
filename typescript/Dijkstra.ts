type Grafo = { [cidade: string]: { [vizinho: string]: number } };
type Resultado = { caminho: string[]; custo: number; visitados: number };

function dijkstra(grafo: Grafo, inicio: string, objetivo: string): Resultado {
  const dist: { [cidade: string]: number } = {};
  const prev: { [cidade: string]: string | null } = {};
  const visitados: Set<string> = new Set();

  for (const cidade in grafo) {
    dist[cidade] = Infinity;
    prev[cidade] = null;
  }
  dist[inicio] = 0;

  while (visitados.size < Object.keys(grafo).length) {
    // Pega nó com menor distância
    let u: string | null = null;
    for (const cidade in grafo) {
      if (!visitados.has(cidade) && (u === null || dist[cidade] < dist[u])) {
        u = cidade;
      }
    }
    if (u === null || dist[u] === Infinity) break;

    visitados.add(u);

    if (u === objetivo) break;

    for (const [vizinho, peso] of Object.entries(grafo[u])) {
      const novoCusto = dist[u] + peso;
      if (novoCusto < dist[vizinho]) {
        dist[vizinho] = novoCusto;
        prev[vizinho] = u;
      }
    }
  }

  // Reconstruir caminho
  const caminho: string[] = [];
  let atual: string | null = objetivo;
  while (atual) {
    caminho.unshift(atual);
    atual = prev[atual];
  }

  return { caminho, custo: dist[objetivo], visitados: visitados.size };
}

// ----------------- TESTE -----------------
const graphDijkstra: Grafo = {
  "Pelotas": { "Camaquã": 150, "Rio Grande": 55 },
  "Camaquã": { "Pelotas": 150, "Porto Alegre": 125 },
  "Rio Grande": { "Pelotas": 55, "Porto Alegre": 320 },
  "Porto Alegre": { "Camaquã": 125, "Rio Grande": 320 }
};

console.log(dijkstra(graphDijkstra, "Pelotas", "Porto Alegre"));
