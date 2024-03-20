import random


# Функция для генерации случайного графа с заданным количеством вершин
def generate_random_graph(num_vertices, num_edges):
    graph = {}
    edges = 0

    while edges < num_edges:
        v1 = random.randint(1, num_vertices)
        v2 = random.randint(1, num_vertices)

        if v1 != v2 and v2 not in graph.get(v1, []):
            if v1 not in graph:
                graph[v1] = []
            if v2 not in graph:
                graph[v2] = []

            graph[v1].append(v2)
            graph[v2].append(v1)
            edges += 1

    return graph


# Функция начальной популяции
def generate_initial_population(graph, num_colors, population_size):
    population = []
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
def mutate_solution(solution, num_colors, mutation_rate):
    mutated_solution = solution.copy()
    for vertex in mutated_solution:
        if random.random() < mutation_rate:
            original_color = mutated_solution[vertex]
            new_color = random.randint(0, num_colors - 1)
            mutated_solution[vertex] = new_color if new_color != original_color else (new_color + 1) % num_colors
    return mutated_solution


# Функция эволюции решений
def evaluate_solution(graph, solution):
    num_colors_used = max(solution.values()) + 1
    return num_colors_used


# Функция проверки конфликтов ребёр
def check_conflicts(graph, solution):
    for vertex in graph:
        color = solution[vertex]
        for neighbor in graph[vertex]:
            if solution[neighbor] == color:
                return True
    return False


# Функция иммунного алгоритма
def immune_algorithm(graph, num_colors, population_size, num_generations, mutation_rate):
    population = generate_initial_population(graph, num_colors, population_size)

    for gen in range(num_generations):
        new_population = []

        for solution in population:
            clone = clone_solution(solution)
            mutated_solution = mutate_solution(solution, num_colors, mutation_rate)
            if evaluate_solution(graph, mutated_solution) <= evaluate_solution(graph, clone) and not check_conflicts(
                    graph, mutated_solution):
                new_population.append(mutated_solution)
            else:
                new_population.append(clone)

        population = new_population

    best_solution = min(population, key=lambda x: evaluate_solution(graph, x))
    best_num_colors = evaluate_solution(graph, best_solution)

    return best_solution, best_num_colors


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


# Функция генерирует правильный граф
def generating_graph(num_vertices, num_edges):
    # Генерация случайного графа с заданным количеством вершин
    random_graph = generate_random_graph(int(num_vertices), int(num_edges))

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


def coloring_account(graph, population_size, num_generations, mutation_rate):
    colors_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange",
                   "Cyan", "Magenta", "Lime", "Pink", "Teal", "Indigo",
                   "Brown", "Silver", "Gold", "Violet", "Turquoise", "Coral",
                   "Maroon", "Olive"]

    '''print("Граф:")
    for vertex, neighbors in graph.items():
        print(f"{chr(64 + vertex)} - {[chr(64 + neighbor) for neighbor in neighbors]}")'''

    # Использование иммунного алгоритма для оптимизации цветов
    num_colors = min_colors_needed(graph)
    optimized_colors, optimized_num_colors = immune_algorithm(graph, num_colors, int(population_size),
                                                              int(num_generations),
                                                              float(mutation_rate))

    # Создаем пустой словарь
    new_optimized_graph = {}

    print("Раскрашенный граф:")
    for vertex, color in optimized_colors.items():
        key = vertex
        value = f"{colors_list[color]}"
        new_optimized_graph[key] = value

    for vertex, neighbors in new_optimized_graph.items():
        print(f"{vertex} - {neighbors}")

    print(f"Минимальное количество цветов по функции: {num_colors}")
    print(f"Оптимизированное количество цветов: {optimized_num_colors}")

    return new_optimized_graph
