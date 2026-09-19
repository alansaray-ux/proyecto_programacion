# Programa preliminar: grafo de prueba del Metro de Madrid
# en relacion a un tutorial sobre networkx y matplotlob programa preeliminar:

import networkx as nx
import matplotlib.pyplot as plt

# crear el grafo vacío
# utilizando la libreria networkx
metro = nx.Graph()

# agregar las estaciones (nodos) - solo 5 de prueba
estaciones = ["Sol", "Gran Via", "Callao", "Opera", "Plaza de España"]
metro.add_nodes_from(estaciones)

# agregar las conexiones (aristas) entre estaciones
conexiones = [
    ("Sol", "Gran Via"),
    ("Gran Via", "Callao"),
    ("Callao", "Opera"),
    ("Opera", "Plaza de España"),
    ("Sol", "Opera")  # conexión extra para simular un ciclo
]
metro.add_edges_from(conexiones)

# mostrar información básica del grafo
print("Estaciones:", metro.nodes())
print("Conexiones:", metro.edges())
print("Numero de estaciones:", metro.number_of_nodes())
print("Numero de conexiones:", metro.number_of_edges())

# dibujar el grafo
nx.draw(metro, with_labels=True, node_color="lightblue", node_size=1500)
plt.show()
