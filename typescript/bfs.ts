type Grafo = { [cidade: string]: { [vizinho: string]: number } };
type Resultado = { caminho: string[]; custo: number; visitados: number };

function breadthFirst(grafo: Grafo, inicio: string, objetivo: string): Resultado {
  const fila: [string, string[]][] = [[inicio, [inicio]]];
  const visitados: Set<string> = new Set();

  while (fila.length > 0) {
    const [no, caminho] = fila.shift()!;

    if (visitados.has(no)) continue;
    visitados.add(no);

    if (no === objetivo) {
      return { caminho, custo: caminho.length - 1, visitados: visitados.size };
    }

    for (const vizinho of Object.keys(grafo[no] || {})) {
      if (!visitados.has(vizinho)) {
        fila.push([vizinho, [...caminho, vizinho]]);
      }
    }
  }

  return { caminho: [], custo: 0, visitados: visitados.size };
}

// ----------------- TESTE -----------------
const graphBFS: Grafo = {
  "Pelotas": { "Camaquã": 150, "Rio Grande": 55 },
  "Camaquã": { "Pelotas": 150, "Porto Alegre": 125 },
  "Rio Grande": { "Pelotas": 55, "Porto Alegre": 320 },
  "Porto Alegre": { "Camaquã": 125, "Rio Grande": 320 }
};

console.log(breadthFirst(graphBFS, "Pelotas", "Porto Alegre"));
