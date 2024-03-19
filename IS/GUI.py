import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Coloring_account import coloring_account, generating_graph


# Функция для рисования вершин нужными нам цветами
def draw_colored_graph(G, pos, color_dict):
    node_colors = [color_dict[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='black', width=2, alpha=0.8)


# Данные для графа из нового словаря
graph_dict = generating_graph()
color_graph = coloring_account(graph_dict)

# Создаем граф и добавляем узлы и связи
G = nx.Graph()
for node, neighbors in graph_dict.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Создаем окно tkinter
root = tk.Tk()
root.title("Граф")

# Отображение графа на tkinter canvas
fig, ax = plt.subplots()
pos = nx.random_layout(G, seed=42)
draw_colored_graph(G, pos, color_graph)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Запускаем главный цикл tkinter
tk.mainloop()
