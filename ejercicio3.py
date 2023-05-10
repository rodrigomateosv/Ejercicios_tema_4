import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, nombre, tipo):
        self.vertices[nombre] = {"tipo": tipo, "vecinos": {}}

    def conectar_vertices(self, origen, destino, distancia):
        self.vertices[origen]["vecinos"][destino] = distancia
        self.vertices[destino]["vecinos"][origen] = distancia

    def dijkstra(self, inicio, fin):
        distancias = {vertice: float("infinity") for vertice in self.vertices}
        distancias[inicio] = 0

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

            if vertice_actual == fin:
                return distancias[fin]

            if distancia_actual == distancias[vertice_actual]:
                for vecino, distancia_vecino in self.vertices[vertice_actual]["vecinos"].items():
                    nueva_distancia = distancia_actual + distancia_vecino

                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return None

# Creación del grafo y vértices
grafo = Grafo()

estaciones = [
    "King's Cross", "Waterloo", "Victoria Train Station",
    "Liverpool Street Station", "St. Pancras", "Euston"
]

for estacion in estaciones:
    grafo.agregar_vertice(estacion, "estacion")

for i in range(1, 13):
    grafo.agregar_vertice(i, "desvio")

# Conectar vértices siguiendo las restricciones
grafo.conectar_vertices("King's Cross", 1, 5)
grafo.conectar_vertices(1, 2, 3)
grafo.conectar_vertices(2, "Waterloo", 4)

grafo.conectar_vertices("Victoria Train Station", 3, 2)
grafo.conectar_vertices(3, 4, 1)
grafo.conectar_vertices(4, "Liverpool Street Station", 6)

grafo.conectar_vertices("St. Pancras", 5, 3)
grafo.conectar_vertices(5, 6, 1)
grafo.conectar_vertices(6, "King's Cross", 7)

# Caminos más cortos
camino_kings_cross_waterloo = grafo.dijkstra("King's Cross", "Waterloo")
camino_victoria_liverpool = grafo.dijkstra("Victoria Train Station", "Liverpool Street Station")
camino_st_pancras_kings_cross = grafo.dijkstra("St. Pancras", "King's Cross")

print("Camino más corto desde King's Cross hasta Waterloo:", camino_kings_cross_waterloo)
print("Camino más corto desde Victoria Train Station hasta Liverpool Street Station:", camino_victoria_liverpool)
print("Camino más corto desde St. Pancras hasta King's Cross:", camino_st_pancras_kings_cross)
