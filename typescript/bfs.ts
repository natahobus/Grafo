type Grafo = { [cidade: string]: { [vizinho: string]: number } };
type Resultado = { caminho: string[]; custo: number; visitados: number };

function depthFirst(
  grafo: Grafo,
  inicio: string,
  objetivo: string,
  visitados: Set<string> = new Set(),
  caminho: string[] = [],
  custo: number = 0
): Resultado {
  caminho.push(inicio);
  visitados.add(inicio);

  if (inicio === objetivo) {
    return { caminho: [...caminho], custo, visitados: visitados.size };
  }

  for (const [vizinho, peso] of Object.entries(grafo[inicio] || {})) {
    if (!visitados.has(vizinho)) {
      const result = depthFirst(grafo, vizinho, objetivo, visitados, caminho, custo + peso);
      if (result.caminho.length > 0) return result;
    }
  }

  caminho.pop(); // backtracking
  return { caminho: [], custo: 0, visitados: visitados.size };
}

// ----------------- TESTE -----------------
const graphDFS: Grafo = {
  "Pelotas": { "Camaquã": 150, "Rio Grande": 55 },
  "Camaquã": { "Pelotas": 150, "Porto Alegre": 125 },
  "Rio Grande": { "Pelotas": 55, "Porto Alegre": 320 },
  "Porto Alegre": { "Camaquã": 125, "Rio Grande": 320 }
};

console.log(depthFirst(graphDFS, "Pelotas", "Porto Alegre"));
