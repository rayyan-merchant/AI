# Q1. Enhanced Maze Navigation with Multiple Goals
from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None, cost=0, goals_left=None):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.goals_left = goals_left if goals_left else set()

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(current_pos, goals_left):
    if not goals_left:
        return 0
    return min(abs(current_pos[0] - g[0]) + abs(current_pos[1] - g[1]) for g in goals_left)

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]

def best_first_search_multiple_goals(maze, start, goal_positions):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start, None, 0, set(goal_positions))
    frontier = PriorityQueue()
    frontier.put((0, start_node))
    visited = set()

    while not frontier.empty():
        _, current_node = frontier.get()
        current_pos = current_node.position
        goals_left = current_node.goals_left.copy()

        if current_pos in goals_left:
            goals_left.remove(current_pos)

        if not goals_left:
            return reconstruct_path(current_node)

        visited.add((current_pos, frozenset(goals_left)))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)

            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                maze[new_pos[0]][new_pos[1]] == 0):

                new_node = Node(new_pos, current_node, current_node.cost + 1, goals_left)

                if (new_pos, frozenset(goals_left)) not in visited:
                    frontier.put((heuristic(new_pos, goals_left) + new_node.cost, new_node))

    return None

maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal_positions = [(4, 4), (2, 3)]

path = best_first_search_multiple_goals(maze, start, goal_positions)
if path:
    print("Shortest Path covering all goals:", path)
else:
    print("No path found")







# Q2. Implement an A* Search where the edge costs change dynamically at random intervals.
from queue import PriorityQueue
import random

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dynamic_a_star(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    visited = set()
    costs = {start: 0}
    completed_goals = set()
    full_path = []

    while not frontier.empty():
        curr_cost, curr_pos, curr_path = frontier.get()

        if curr_pos in visited:
            continue

        visited.add(curr_pos)
        curr_path.append(curr_pos)

        if curr_pos in goals:
            completed_goals.add(curr_pos)
            full_path.extend(curr_path)
            if completed_goals == goals:
                return full_path
            curr_path = [curr_pos]

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0:
                new_cost = curr_cost + random.randint(1, 10)
                if new_pos not in costs or new_cost < costs[new_pos]:
                    costs[new_pos] = new_cost
                    remaining_goals = goals - completed_goals
                    if remaining_goals:
                        priority = new_cost + min(heuristic(new_pos, goal) for goal in remaining_goals)
                    else:
                        priority = new_cost
                    frontier.put((priority, new_pos, curr_path.copy()))

    return "No path to all goals"

maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = {(4, 4), (0, 3), (3, 1)}

path_dynamic_astar = dynamic_a_star(maze, start, goals)

print("\nDynamic A* Optimized Path")
if isinstance(path_dynamic_astar, list):
    for step in path_dynamic_astar:
        print(f"→ {step}")
else:
    print(path_dynamic_astar)





# Scenario 3️⃣: Multiple Paths, Different Costs

from queue import PriorityQueue

# Graph with multiple paths and different costs
graph = {
    'A': [('B', 1, 7), ('C', 4, 3)],
    'B': [('D', 5, 2), ('E', 2, 4)],
    'C': [('E', 1, 4)],
    'D': [('F', 3, 1)],
    'E': [('F', 2, 1)],
    'F': []  # Goal node
}

def astar_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, 0))  # (f-value, node, g-cost)
    visited = set()
    came_from = {start: None}
    g_costs = {start: 0}

    while not pq.empty():
        f_value, node, g_cost = pq.get()

        if node in visited:
            continue

        print(f"Visiting: {node}")
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal found! Path: {path}")
            return path

        for neighbor, edge_cost, heuristic in graph[node]:
            new_g_cost = g_cost + edge_cost
            new_f_value = new_g_cost + heuristic

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = node
                pq.put((new_f_value, neighbor, new_g_cost))

    print("\nGoal not reachable!")
    return None

# Run A* Search for Scenario 3
print("A* Search for Scenario 3 (Multiple Paths, Different Costs):")
astar_search(graph, 'A', 'F')




# Scenario 4️⃣: Grid-Based Pathfinding (Maze)

from queue import PriorityQueue

# Define a 3x3 grid maze as a graph
grid_graph = {
    (0,0): [(0,1,1), (1,0,1)],
    (0,1): [(0,2,1), (1,1,1)],
    (0,2): [(1,2,1)],
    (1,0): [(1,1,1), (2,0,1)],
    (1,1): [(1,2,1), (2,1,1)],
    (1,2): [(2,2,1)],
    (2,0): [(2,1,1)],
    (2,1): [(2,2,1)],
    (2,2): []  # Goal
}

def astar_grid_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start, 0))  # (f-value, node, g-cost)
    visited = set()
    came_from = {start: None}
    g_costs = {start: 0}

    # Manhattan Distance Heuristic (for grids)
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    while not pq.empty():
        f_value, node, g_cost = pq.get()

        if node in visited:
            continue

        print(f"Visiting: {node}")
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal found! Path: {path}")
            return path

        for neighbor, edge_cost in graph[node]:
            new_g_cost = g_cost + edge_cost
            new_f_value = new_g_cost + heuristic(neighbor, goal)

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = node
                pq.put((new_f_value, neighbor, new_g_cost))

    print("\nGoal not reachable!")
    return None

# Run A* Search for Scenario 4
print("\nA* Search for Scenario 4 (Grid-Based Pathfinding):")
astar_grid_search(grid_graph, (0,0), (2,2))
