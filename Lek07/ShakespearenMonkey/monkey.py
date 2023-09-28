import random


def generate_random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ') for _ in range(length))


def calculate_fitness(kromosom, maalsaetning):
    score = 0
    for i in range(len(kromosom)):
        if kromosom[i] == maalsaetning[i]:
            score += 1
    return score


def find_best_random_string(maalsaetning, num_strings):
    highest_fitness = -1
    best_string = ""
    for _ in range(num_strings):
        random_string = generate_random_string(len(maalsaetning))
        fitness = calculate_fitness(random_string, maalsaetning)
        if fitness > highest_fitness:
            highest_fitness = fitness
            best_string = random_string
    return best_string


def generate_neighbor(kromosom):
    # Generer en nabo ved at tilfældigt ændre en karakter i kromosomet
    index = random.randint(0, len(kromosom) - 1)
    new_char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    neighbor = kromosom[:index] + new_char + kromosom[index + 1:]
    return neighbor


def hill_climbing(maalsaetning, max_iterations):
    current_solution = generate_random_string(len(maalsaetning))  # Start med en tilfældig løsning
    current_fitness = calculate_fitness(current_solution, maalsaetning)

    for _ in range(max_iterations):
        neighbor = generate_neighbor(current_solution)
        neighbor_fitness = calculate_fitness(neighbor, maalsaetning)

        if neighbor_fitness > current_fitness:
            current_solution = neighbor
            current_fitness = neighbor_fitness

    return current_solution


maalsaetning = "To be or not to be that is the question"
num_strings = 10000
best_string = find_best_random_string(maalsaetning, num_strings)
print("Random")
print(f"Den bedste tilfældige streng er: {best_string}")
print(f"Fitness score: {calculate_fitness(best_string, maalsaetning)}")

# ----------- Hill climb -----------------
print();
max_iterations = 7500
best_string_hill_climbing = hill_climbing(maalsaetning, max_iterations)
print("Hill climb")
print(f"Den bedste streng fundet ved hill climbing er: {best_string_hill_climbing}")
print(f"Fitness score: {calculate_fitness(best_string_hill_climbing, maalsaetning)}")

# --------------- GA ---------------------
print()


def generate_population(population_size, kromosom_length):
    return [generate_random_string(kromosom_length) for _ in range(population_size)]


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(kromosom, mutation_rate):
    mutated_kromosom = ""
    for char in kromosom:
        if random.random() < mutation_rate:
            mutated_kromosom += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        else:
            mutated_kromosom += char
    return mutated_kromosom


def genetic_algorithm(maalsaetning, population_size, mutation_rate, generations):
    population = generate_population(population_size, len(maalsaetning))

    for generation in range(generations):
        population = sorted(population, key=lambda k: calculate_fitness(k, maalsaetning), reverse=True)
        if calculate_fitness(population[0], maalsaetning) == len(maalsaetning):
            break
        new_population = []
        for i in range(population_size // 2):
            parent1, parent2 = random.choices(population[:population_size // 2], k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population

    return population[0]


# Parametre
population_size = 100
mutation_rate = 0.01
generations = 1000

# Kør GA
best_string_genetic_algorithm = genetic_algorithm(maalsaetning, population_size, mutation_rate, generations)
print("Genetic algorithm")
print(f"Den bedste streng fundet ved genetisk algoritme er: {best_string_genetic_algorithm}")
print(f"Fitness score: {calculate_fitness(best_string_genetic_algorithm, maalsaetning)}")
