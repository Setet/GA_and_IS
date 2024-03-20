import tkinter
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, messagebox

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Coloring_account import coloring_account, generating_graph


# Функция для рисования вершин нужными нам цветами
def draw_colored_graph(G, pos, color_dict):
    node_colors = [color_dict[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='black', width=2, alpha=0.8)


def gui():
    window = Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry("%dx%d" % (width, height))
    window.title("Раскраска графа")

    fig = plt.figure(figsize=(14, 14))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    def start():
        fig.clf()
        # Данные для графа из нового словаря
        graph_dict = generating_graph(txt_4_window.get())
        color_graph = coloring_account(graph_dict, txt_1_window.get(), txt_2_window.get(), txt_3_window.get())

        # Создаем граф и добавляем узлы и связи
        G = nx.Graph()
        for node, neighbors in graph_dict.items():
            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        # Отображение графа на tkinter canvas
        pos = nx.random_layout(G, seed=42)
        draw_colored_graph(G, pos, color_graph)
        canvas.draw()

        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab():
        txt_window.delete(1.0, END)

    main_f_window = LabelFrame(window, text="Параметры")
    left_f_window = Frame(main_f_window)
    right_f_window = Frame(main_f_window)
    txt_f_window = LabelFrame(window, text="Консоль лог")

    lbl_1_window = Label(left_f_window, text="Размер популяции")
    lbl_2_window = Label(left_f_window, text="Кол-во итераций")
    lbl_3_window = Label(left_f_window, text="Коэффициент мутации")
    lbl_4_window = Label(left_f_window, text="Кол-во вершин")
    lbl_5_window = Label(left_f_window, text="Кол-во рёбер")

    txt_1_window = Entry(right_f_window)
    txt_2_window = Entry(right_f_window)
    txt_3_window = Entry(right_f_window)
    txt_4_window = Entry(right_f_window)
    txt_5_window = Entry(right_f_window)

    txt_window = scrolledtext.ScrolledText(txt_f_window)
    btn_del_window = Button(window, text="Очистить лог", command=delete_lab)
    btn_window = Button(window, text="Выполнить", foreground="black", background="#00FFFF", command=start)

    main_f_window.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_window.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_window.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_window.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_window.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_window.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_window.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_window.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Запускаем главный цикл tkinter
    tk.mainloop()


gui()
