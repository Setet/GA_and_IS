import random
import timeit


# Функция проверки всего графа на правильность раскраски
def check_graph_coloring(graph, coloring):
    for vertex, color in coloring.items():
        for neighbor in graph[vertex]:
            if coloring.get(neighbor) == color:
                return False
    return True


# Функция для генерации случайного графа с заданным количеством вершин
def generate_random_graph(num_vertices, num_edges):
    graph = {vertex: [] for vertex in range(num_vertices)}

    while num_edges > 0:
        vertex1 = random.randint(0, num_vertices - 1)
        vertex2 = random.randint(0, num_vertices - 1)

        if vertex1 != vertex2 and vertex2 not in graph[vertex1]:
            graph[vertex1].append(vertex2)
            graph[vertex2].append(vertex1)
            num_edges -= 1

    return graph


# Функция генерирует красивый граф с символами
def generating_graph(num_vertices, num_edges):
    # Генерация случайного графа с заданным количеством вершин
    random_graph = generate_random_graph(int(num_vertices), int(num_edges))

    # print(random_graph)

    # Создаем новый словарь с буквами в качестве ключей
    new_graph = {}
    for key, value in random_graph.items():
        # Преобразуем числовой ключ в букву ('A', 'B', 'C', ...)
        new_key = chr(66 + key - 1)
        # Преобразуем числовые значения в буквы
        new_value = [chr(66 + num - 1) for num in value]
        new_graph[new_key] = new_value

    return new_graph


# Функция начальной популяции
def generate_initial_population(graph, population_size):
    population = []
    # Минимальное количество цветов равно 3
    num_colors = max(len(graph), 3)
    for _ in range(population_size):
        colors = {}
        for vertex in graph:
            colors[vertex] = random.randint(0, num_colors - 1)
        population.append(colors)
    return population


# Функция клонирования решений
def clone_solution(solution):
    return solution.copy()


# Функция мутации решений
def mutate_solution(solution, mutation_rate):
    mutated_solution = solution.copy()
    num_colors = max(solution.values()) + 1
    for vertex in mutated_solution:
        if random.random() < mutation_rate:
            original_color = mutated_solution[vertex]
            new_color = random.randint(0, num_colors - 1)
            mutated_solution[vertex] = new_color if new_color != original_color else (new_color + 1) % num_colors
    return mutated_solution


# Функция проверки конфликтов ребер
def check_conflicts(graph, solution):
    for vertex in graph:
        color = solution[vertex]
        for neighbor in graph[vertex]:
            if solution[neighbor] == color:
                return True
    return False


# Функция используется для оценки качества
# В рамках данной задачи, функция evaluate_solution возвращает количество уникальных цветов,
# которые были использованы в решении.
# Чем меньше цветов используется, тем лучше решение с точки зрения минимизации количества используемых цветов.
def evaluate_solution(solution):
    return len(set(solution.values()))


# Функция иммунного алгоритма
def immune_algorithm(graph, population_size, num_generations, mutation_rate):
    population = generate_initial_population(graph, population_size)

    for gen in range(num_generations):
        new_population = []

        for solution in population:
            clone = clone_solution(solution)
            mutated_solution = mutate_solution(solution, mutation_rate)
            if evaluate_solution(mutated_solution) <= evaluate_solution(clone) and not check_conflicts(
                    graph, mutated_solution):
                new_population.append(mutated_solution)
            else:
                new_population.append(clone)

        population = new_population

    best_solution = min(population, key=lambda x: evaluate_solution(x))
    best_num_colors = evaluate_solution(best_solution)

    return best_solution, best_num_colors


# Функция раскраски графа
def coloring_account(graph, population_size, num_generations, mutation_rate):
    colors_list = [
        "Red", "Blue", "Green", "Yellow", "Purple",
        "Orange", "Cyan", "Magenta", "Lime", "Pink",
        "Teal", "Indigo", "Brown", "Silver", "Gold",
        "Violet", "Coral", "Maroon", "Olive"
    ]

    # Отчёт времени работы иммунного алгоритма
    time_start = timeit.default_timer()

    # Использование иммунного алгоритма для оптимизации цветов
    optimized_colors, optimized_num_colors = immune_algorithm(graph,
                                                              int(population_size),
                                                              int(num_generations),
                                                              float(mutation_rate))
    # Завершение работы иммунного алгоритма
    time_over = timeit.default_timer()

    # Время работы программы
    time = round(time_over - time_start, 4)

    # Создаем пустой словарь
    new_optimized_graph = {}

    # Заполняем словарь цветами
    for vertex, color in optimized_colors.items():
        key = vertex
        value = f"{colors_list[color]}"
        new_optimized_graph[key] = value

    return new_optimized_graph, optimized_num_colors, time
