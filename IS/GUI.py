import tkinter
import time
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Style

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Coloring_account import coloring_account, generating_graph


# Функция для рисования вершин нужными нам цветами
def draw_colored_graph(G, pos, color_dict):
    node_colors = [color_dict[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='black', width=2, alpha=0.8)


# Функция осн интерфейса
def gui():
    # Инициализация окна
    window = Tk()

    # Даю название окну
    window.title("Раскраска графа")

    # Узнаю размер экрана
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    # Выставляю фулл размер
    window.geometry(f"{width}x{height}+0+0")

    style = Style()
    style.theme_use("default")
    style.configure("Label", font=("Helvetica", 14))
    style.map("Label")

    # Рисую начальное пустое поле под граф
    fig = plt.figure(figsize=(14, 14))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    # Функция для работы программы
    def start():
        # Очищаю форму от предыдущих рисунков
        fig.clf()

        # Данные для графа
        # Сам граф
        graph_dict = generating_graph(input_field_4.get(), input_field_5.get())
        # Цвета графа
        color_graph = coloring_account(graph_dict, input_field_1.get(), input_field_2.get(), input_field_3.get())

        # Создаем граф и добавляем узлы и связи
        G = nx.Graph()
        for node, neighbors in graph_dict.items():
            G.add_node(node)
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        pos = nx.random_layout(G, seed=42)

        # Отображение графа на tkinter canvas(не раскрашенный)
        nx.draw(G, pos, with_labels=True, edge_color='black', width=2, alpha=0.8)

        # Рисую то что получилось
        canvas.draw()

        # Обновляю окно
        window.update()

        # Задержка в сек
        time.sleep(10)

        fig.clf()

        # Отображение графа на tkinter canvas(раскрашенный)
        draw_colored_graph(G, pos, color_graph)
        canvas.draw()

        window.update()
        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab():
        scrolled_text.delete(1.0, END)

    main_frame = LabelFrame(window, text="Параметры", font=('Arial', 20))

    left_frame = Frame(main_frame)
    right_frame = Frame(main_frame)
    console_frame = LabelFrame(window, text="Консоль лог", font=('Arial', 20))

    label_1 = Label(left_frame, text="Размер популяции", font=('Arial', 20))

    label_2 = Label(left_frame, text="Кол-во итераций", font=('Arial', 20))

    label_3 = Label(left_frame, text="Коэффициент мутации", font=('Arial', 20))

    label_4 = Label(left_frame, text="Кол-во вершин", font=('Arial', 20))

    label_5 = Label(left_frame, text="Кол-во рёбер", font=('Arial', 20))

    input_field_1 = Entry(right_frame, font=('Arial', 20))
    input_field_1.insert(0, "50")

    input_field_2 = Entry(right_frame, font=('Arial', 20))
    input_field_2.insert(0, "100")

    input_field_3 = Entry(right_frame, font=('Arial', 20))
    input_field_3.insert(0, "0.1")

    input_field_4 = Entry(right_frame, font=('Arial', 20))
    input_field_4.insert(0, "10")

    input_field_5 = Entry(right_frame, font=('Arial', 20))
    input_field_5.insert(0, "5")

    scrolled_text = scrolledtext.ScrolledText(console_frame)
    delete_button = Button(window, text="Очистить лог", command=delete_lab, font=('Arial', 20))

    run_button = Button(window, text="Выполнить", foreground="black", background="#00FFFF", command=start,
                        font=('Arial', 20))

    main_frame.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_frame.pack(side=LEFT, fill=BOTH, expand=True)
    right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    label_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    label_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    label_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    label_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    label_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    input_field_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    input_field_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    input_field_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    input_field_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    input_field_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    scrolled_text.pack(padx=5, pady=5, fill=BOTH, expand=True)

    run_button.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    console_frame.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    delete_button.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Запускаем главный цикл tkinter
    tk.mainloop()


gui()
