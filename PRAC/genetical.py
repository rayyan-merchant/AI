import random

# Configuration
num_staff = 5  # Number of employees
num_shifts = 21  # 7 days * 3 shifts per day
max_shifts_per_staff = 7
required_staff_per_shift = 2
population_size = 10
mutation_rate = 0.1
max_generations = 1000

# Fitness function (lower is better)
def evaluate_fitness(schedule):
    penalty = 0

    # Check shift coverage
    for shift in range(num_shifts):
        assigned_count = sum(schedule[staff][shift] for staff in range(num_staff))
        if assigned_count < required_staff_per_shift:
            penalty += (required_staff_per_shift - assigned_count) * 10  # Understaffed penalty

    # Check consecutive shifts for each staff
    for staff in range(num_staff):
        for shift in range(num_shifts - 1):
            if schedule[staff][shift] == 1 and schedule[staff][shift + 1] == 1:
                penalty += 5  # Penalty for consecutive shifts

    return penalty

# Create a random schedule
def create_random_schedule():
    schedule = [[0] * num_shifts for _ in range(num_staff)]
    for staff in range(num_staff):
        assigned_shifts = random.sample(range(num_shifts), random.randint(3, max_shifts_per_staff))
        for shift in assigned_shifts:
            schedule[staff][shift] = 1
    return schedule

# Selection (Top 50%)
def select_parents(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]
    return sorted_population[:len(population) // 2]

# Crossover (Single-point crossover)
def crossover(parent1, parent2):
    point = random.randint(0, num_shifts - 1)
    child = [parent1[i][:point] + parent2[i][point:] for i in range(num_staff)]
    return child

# Mutation (Swap shifts for one staff)
def mutate(schedule):
    staff = random.randint(0, num_staff - 1)
    shift1, shift2 = random.sample(range(num_shifts), 2)
    schedule[staff][shift1], schedule[staff][shift2] = schedule[staff][shift2], schedule[staff][shift1]
    return schedule

# Genetic Algorithm
def genetic_algorithm():
    population = [create_random_schedule() for _ in range(population_size)]

    for generation in range(max_generations):
        fitness_scores = [evaluate_fitness(schedule) for schedule in population]
        best_fitness = min(fitness_scores)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

        # Selection
        parents = select_parents(population, fitness_scores)

        # Crossover and Mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)

        population = new_population

    # Best schedule
    best_schedule = population[fitness_scores.index(min(fitness_scores))]
    print("\nBest Schedule (Staff x Shifts):")
    for staff in range(num_staff):
        print(f"Staff {staff + 1}: {best_schedule[staff]}")

# Run the Genetic Algorithm
genetic_algorithm()










import random

# Define the size of the chessboard (N-Queens)
N = 8
population_size = 10
mutation_rate = 0.1
max_generations = 100

# Fitness function: counts non-attacking pairs of queens
def calculate_fitness(individual):
    non_attacking_pairs = 0
    total_pairs = N * (N - 1) // 2  # Maximum possible non-attacking pairs

    # Check for conflicts
    for i in range(N):
        for j in range(i + 1, N):
            # No same column or diagonal conflict
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1

    return non_attacking_pairs / total_pairs  # Fitness score

# Generate a random individual (chromosome) based on column positions
def create_random_individual():
    return random.sample(range(N), N)  # Ensure unique column positions

# Create an initial population of random individuals
def generate_population():
    return [create_random_individual() for _ in range(population_size)]

# Selection: Tournament Selection
def select_parents(population, fitness_scores):
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
    return sorted_population[:len(population) // 2]  # Select top 50%

# Crossover: Single-Point Crossover ensuring unique column positions
def crossover(parent1, parent2):
    point = random.randint(1, N - 2)  # Choose a crossover point
    child = parent1[:point] + parent2[point:]

    # Ensure unique column positions
    missing = set(range(N)) - set(child)
    duplicates = [col for col in child if child.count(col) > 1]

    for i in range(len(child)):
        if child.count(child[i]) > 1:
            child[i] = missing.pop()

    return child

# Mutation: Swap two queen positions randomly
def mutate(individual):
    idx1, idx2 = random.sample(range(N), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic Algorithm main function
def genetic_algorithm():
    population = generate_population()
    generation = 0
    best_fitness = 0

    while best_fitness < 1.0 and generation < max_generations:
        fitness_scores = [calculate_fitness(ind) for ind in population]
        best_fitness = max(fitness_scores)

        print(f"Generation {generation}, Best Fitness: {best_fitness}")

        # Check for optimal solution
        if best_fitness == 1.0:
            break

        # Selection
        parents = select_parents(population, fitness_scores)

        # Crossover
        new_population = [crossover(random.choice(parents), random.choice(parents)) for _ in range(population_size)]

        # Mutation
        for i in range(len(new_population)):
            if random.random() < mutation_rate:
                new_population[i] = mutate(new_population[i])

        population = new_population
        generation += 1

    # Return the best solution
    best_individual = max(population, key=calculate_fitness)
    return best_individual, calculate_fitness(best_individual)

# Run the Genetic Algorithm
solution, fitness = genetic_algorithm()
print("\nBest Solution:", solution)
print("Best Fitness:", fitness)
