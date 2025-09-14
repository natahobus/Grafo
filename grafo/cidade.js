const grafo = {
  "Pelotas": { "Rio Grande": 60, "Canguçu": 50 },
  "Rio Grande": { "Pelotas": 60, "São José do Norte": 30 },
  "Canguçu": { "Pelotas": 50, "Porto Alegre": 200 },
  "São José do Norte": { "Rio Grande": 30 },
  "Porto Alegre": { "Canguçu": 200 }
};

module.exports = grafo;
