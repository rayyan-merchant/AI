import random

# Problem Parameters
POP_SIZE = 10  # Population size
GENE_LENGTH = 5  # Number of bits (for x values from 0-31)
MUTATION_RATE = 0.1  # Mutation probability
GENERATIONS = 50  # Number of generations

# Fitness Function: f(x) = x^2 (Maximization)
def fitness(individual):
    x = int("".join(map(str, individual)), 2)  # Convert binary to integer
    return x ** 2  # Objective function

# Generate Initial Population (Random Binary Chromosomes)
def generate_population():
    return [[random.randint(0, 1) for _ in range(GENE_LENGTH)] for _ in range(POP_SIZE)]

# Selection: Tournament Selection
def tournament_selection(population):
    tournament_size = 3
    selected = random.sample(population, tournament_size)
    return max(selected, key=fitness)  # Choose best in tournament

# Crossover: Single-Point Crossover
def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation: Bit Flip Mutation
def mutate(individual):
    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]  # Flip bit
    return individual

# Genetic Algorithm
def genetic_algorithm():
    population = generate_population()
    
    for gen in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)  # Sort by fitness
        
        print(f"Generation {gen}: Best Fitness = {fitness(population[0])}")
        
        new_population = population[:2]  # Elitism (Keep top 2)
        
        while len(new_population) < POP_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population

    best_individual = max(population, key=fitness)
    best_x = int("".join(map(str, best_individual)), 2)
    print(f"\nOptimal Solution: x = {best_x}, f(x) = {best_x ** 2}")

# Run the Genetic Algorithm
genetic_algorithm()
