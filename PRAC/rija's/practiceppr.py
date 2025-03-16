# Q1

#q1 bfs dfs rescue robot
from collections import deque

# Define the grid
grid = [
    ['O', 'O', 'X', 'O', 'T'],
    ['O', 'X', 'O', 'O', 'X'],
    ['P', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'X', 'O']
]

# Possible moves: Right, Left, Down, Up
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Find start and goal positions
def find_positions(grid):
    start, goal = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'P':
                start = (r, c)
            if grid[r][c] == 'T':
                goal = (r, c)
    return start, goal

# BFS Algorithm
def bfs(grid, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (current, path) = queue.popleft()

        if current == goal:
            return path  # Return path to goal

        visited.add(current)
        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 'X' and (nr, nc) not in visited:
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None  # No path found

# DFS Algorithm
def dfs(grid, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        (current, path) = stack.pop()

        if current == goal:
            return path  # Return path to goal

        visited.add(current)
        r, c = current

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 'X' and (nr, nc) not in visited:
                stack.append(((nr, nc), path + [(nr, nc)]))

    return None  # No path found

# Find start and goal positions
start, goal = find_positions(grid)

# Run BFS and DFS
bfs_path = bfs(grid, start, goal)
dfs_path = dfs(grid, start, goal)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)











# Q2
# q2 A* courier robot
import heapq

# Define the weighted grid
grid = [
    [1, 2, 3, '#', 4],
    [1, '#', 1, 2, 2],
    [2, 3, 1, '#', 1],
    ['#', '#', 2, 1, 1],
    [1, 1, 2, 2, 1]
]

# Define possible moves
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Heuristic Function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def a_star(grid):
    rows, cols = len(grid), len(grid[0])
    start, goal = (0, 0), (rows - 1, cols - 1)
    open_set = [(0, start)]
    g_costs = {start: 0}
    came_from = {start: None}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                new_g_cost = g_costs[current] + grid[nr][nc]
                if (nr, nc) not in g_costs or new_g_cost < g_costs[(nr, nc)]:
                    g_costs[(nr, nc)] = new_g_cost
                    f_cost = new_g_cost + heuristic((nr, nc), goal)
                    heapq.heappush(open_set, (f_cost, (nr, nc)))
                    came_from[(nr, nc)] = current

    return None  # No path found

# Run A* search
optimal_path = a_star(grid)
print("A* Optimal Path:", optimal_path)








# Q3
# function optimisation GA
import random

# Function to optimize
def f(x):
    return 2 * (x ** 2) - 1

# Convert binary to integer
def binary_to_int(binary):
    return int("".join(map(str, binary)), 2)

# Generate initial population
def generate_population(size):
    return [[random.randint(0, 1) for _ in range(6)] for _ in range(size)]

# Tournament Selection
def tournament_selection(population):
    selected = random.sample(population, 3)
    return max(selected, key=lambda ind: f(binary_to_int(ind)))

# Uniform Crossover
def crossover(parent1, parent2):
    return [random.choice([p1, p2]) for p1, p2 in zip(parent1, parent2)]

# Adaptive Mutation
def mutate(individual, gen, max_gen):
    if random.random() < (1 - gen/max_gen):  # Higher mutation probability in early generations
        index = random.randint(0, len(individual) - 1)
        individual[index] = 1 - individual[index]
    return individual

# Genetic Algorithm
def genetic_algorithm():
    population = generate_population(10)
    generations = 50

    for gen in range(generations):
        population = [mutate(crossover(tournament_selection(population), tournament_selection(population)), gen, generations) for _ in range(10)]

    best = max(population, key=lambda ind: f(binary_to_int(ind)))
    return binary_to_int(best), f(binary_to_int(best))

print("Best Solution:", genetic_algorithm())
