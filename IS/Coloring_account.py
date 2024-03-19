import random


# Функция для генерации случайного графа с заданным количеством вершин
def generate_random_graph(num_vertices):
    graph = {}
    for vertex in range(1, num_vertices + 1):
        if vertex not in graph:
            graph[vertex] = []

        # Генерация случайного количества соседей для вершины
        for _ in range(random.randint(1, num_vertices // 2)):
            neighbor = random.randint(1, num_vertices)
            if neighbor != vertex and neighbor not in graph[vertex] and vertex not in graph.get(neighbor, []):
                graph[vertex].append(neighbor)
                if neighbor not in graph:
                    graph[neighbor] = [vertex]
                else:
                    graph[neighbor].append(vertex)

    return graph


# Функция для определения минимального количества цветов для раскраски графа
def min_colors_needed(graph):
    colors = {}
    for vertex in graph:
        used_colors = set(colors.get(neighbour, None) for neighbour in graph[vertex])
        for color in range(len(used_colors) + 1):
            if color not in used_colors:
                colors[vertex] = color
                break

    return max(colors.values()) + 1


# Функция реализации иммунного алгоритма с использованием жадной раскраски для оптимизации цветов
def immune_algorithm(graph, num_colors, num_generations):
    # Инициализация словаря best_colors для лучших цветов
    # и переменной best_num_colors для лучшего числа цветов как бесконечности
    best_colors = {}
    best_num_colors = float('inf')
    # Переменная для хранения предыдущего лучшего числа цветов
    previous_best_num_colors = best_num_colors

    # Цикл для проведения num_generations итераций
    for gen in range(num_generations):
        # Инициализация словаря colors для выбранных цветов на текущей итерации
        colors = {}
        # Цикл для каждой вершины в графе
        for vertex in graph:
            # Создается множество used_colors для хранения цветов соседей вершины
            used_colors = set(colors.get(neighbour, None) for neighbour in graph[vertex])
            # Цикл для перебора всех возможных цветов в диапазоне от 0 до num_colors
            for color in range(num_colors):
                # Проверка, если цвет не использовался у соседей текущей вершины
                if color not in used_colors:
                    colors[vertex] = color
                    # Вывод результата каждой итерации
                    print(f"Итерация: {gen} - вершина: {vertex} - цвет: {color}")
                    break

        # Определение количества использованных цветов на текущей итерации
        num_colors_used = max(colors.values()) + 1
        # Если текущее количество использованных цветов меньше лучшего найденного до этого
        if num_colors_used < best_num_colors:
            best_colors = colors
            best_num_colors = num_colors_used

        if previous_best_num_colors == best_num_colors:  # Проверка на изменение лучшего числа цветов
            print("Улучшений нет, прекращаем итерации")
            break

        previous_best_num_colors = best_num_colors  # Обновляем предыдущее лучшее число цветов для следующей проверки

    # Возвращение лучших цветов и лучшего числа цветов
    return best_colors, best_num_colors


def generating_graph():
    # Генерация случайного графа с заданным количеством вершин
    num_vertices = random.randint(20, 21)
    random_graph = generate_random_graph(num_vertices)

    # Создаем новый словарь с буквами в качестве ключей
    new_graph = {}
    for key, value in random_graph.items():
        new_key = chr(65 + key - 1)  # Преобразуем числовой ключ в букву ('A', 'B', 'C', ...)
        new_value = [chr(65 + num - 1) for num in value]  # Преобразуем числовые значения в буквы
        new_graph[new_key] = new_value

    print("Граф:")
    for vertex, neighbors in new_graph.items():
        print(f"{vertex} - {neighbors}")

    return new_graph


def coloring_account(graph):
    colors_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange",
                   "Cyan", "Magenta", "Lime", "Pink", "Teal", "Indigo",
                   "Brown", "Silver", "Gold", "Violet", "Turquoise", "Coral",
                   "Maroon", "Olive"]

    '''print("Граф:")
    for vertex, neighbors in graph.items():
        print(f"{chr(64 + vertex)} - {[chr(64 + neighbor) for neighbor in neighbors]}")'''

    # Определение минимального количества цветов
    min_colors = min_colors_needed(graph)
    print(f"Мин кол-во цветов: {min_colors}\n")

    # Использование иммунного алгоритма для оптимизации цветов
    num_generations = 100
    optimized_colors, optimized_num_colors = immune_algorithm(graph, min_colors, num_generations)

    # Создаем пустой словарь
    new_optimized_graph = {}

    print("Раскрашенный граф:")
    for vertex, color in optimized_colors.items():
        key = vertex
        value = f"{colors_list[color]}"
        new_optimized_graph[key] = value

    for vertex, neighbors in new_optimized_graph.items():
        print(f"{vertex} - {neighbors}")

    print(f"Оптимизированное количество цветов: {optimized_num_colors}")

    return new_optimized_graph
