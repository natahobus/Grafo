export type Grafo = { [cidade: string]: { [vizinho: string]: number } };
export type Resultado = { caminho: string[]; custo: number; visitados: number };