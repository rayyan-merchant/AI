# Graph with different edge costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}  # Goal Node
}

# Heuristic function (estimated cost to reach goal 'I')
heuristic = {
    'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7, 'F': 3, 'G': 6, 'H': 2, 'I': 0
}

# A* Search Function
def a_star(graph, start, goal):
    frontier = [(start, heuristic[start])]  # List-based priority queue (sorted manually)
    visited = set()  # Set to keep track of visited nodes
    g_costs = {start: 0}  # Cost to reach each node from start
    came_from = {start: None}  # Path reconstruction

    while frontier:
        # Sort frontier by f(n) = g(n) + h(n)
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)  # Get node with lowest f(n)

        if current_node in visited:
            continue

        print(f"Visiting: {current_node}")
        visited.add(current_node)

        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return path

        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost  # Path cost from start to neighbor
            f_cost = new_g_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, f_cost))

    print("\nGoal not found")
    return None

# Run A* Search
print("\nFollowing is the A* Search:")
a_star(graph, 'A', 'I')







from queue import PriorityQueue

# Example graph represented as an adjacency list with heuristic values
# Each node has (neighbor, cost, heuristic)
graph = {
    'A': [('B', 5, 9), ('C', 8, 5)],  # (neighbor, cost, heuristic)
    'B': [('D', 10, 4)],  # (neighbor, cost, heuristic)
    'C': [('E', 3, 7)],  # (neighbor, cost, heuristic)
    'D': [('F', 7, 5)],  # (neighbor, cost, heuristic)
    'E': [('F', 2, 1)],  # (neighbor, cost, heuristic)
    'F': []  # Goal node
}

def astar_search(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    pq = PriorityQueue()  # Priority queue to prioritize nodes based on f-value (cost + heuristic)
    pq.put((0, start, 0))  # (f-value, node, g-cost)
    
    while not pq.empty():
        f_value, node, g_cost = pq.get()  # Dequeue the node with the lowest f-value

        if node in visited:
            continue

        print(f"Visiting: {node}")  # Print the current node
        visited.add(node)  # Mark the current node as visited

        if node == goal:  # Check if the goal node is reached
            print("\nGoal reached!")
            return True

        # Explore neighbors of the current node
        for neighbor, edge_cost, heuristic in graph[node]:
            if neighbor not in visited:
                new_g_cost = g_cost + edge_cost  # Update g-cost
                new_f_value = new_g_cost + heuristic  # f(n) = g(n) + h(n)
                pq.put((new_f_value, neighbor, new_g_cost))  # Enqueue with updated priority

    print("\nGoal not reachable!")
    return False

# Example usage:
print("A* Search Path:")
astar_search(graph, 'A', 'F')
