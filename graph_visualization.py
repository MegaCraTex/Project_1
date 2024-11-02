import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adj_matrix, labels):
    # Создаем граф из матрицы смежности
    G = nx.from_numpy_array(np.array(adj_matrix))
    
    # Рисуем граф
    pos = nx.circular_layout(G)  # Позиции узлов в форме круга
    nx.draw(G, pos, with_labels=True, labels=labels, node_color='lightblue', node_size=800, font_size=16, font_weight='bold', edge_color='gray')
    
    plt.title("Граф в форме круга")
    plt.show()

# Обновленная матрица смежности
adj_matrix = [
    [0, 1, 0, 0, 0, 1],  # а
    [1, 0, 1, 0, 0, 0],  # б
    [0, 1, 0, 1, 0, 0],  # в
    [0, 0, 1, 0, 1, 0],  # г
    [0, 0, 0, 1, 0, 1],  # д
    [1, 0, 0, 0, 1, 0]   # е
]

# Метки для узлов (а, б, в, г, д, е)
labels = {0: "а", 1: "б", 2: "в", 3: "г", 4: "д", 5: "е"}

draw_graph(adj_matrix, labels)
