def dfs(graph, start, goal):
    visited = []  # List for visited nodes
    stack = []    # Initialize stack

    visited.append(start)
    stack.append(start)

    while stack:
        node = stack.pop()  # LIFO: Pop from top
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in reversed(graph[node]):  # Reverse to maintain correct order
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Run DFS
print("\nFollowing is the Depth-First Search (DFS):")
dfs(graph, start_node, goal_node)




class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        else:
            return environment.dfs_search(percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dfs_search(self, start, goal):
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"

            for neighbour in reversed(self.graph.get(node, [])):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)

        return "Goal not found"

# Define the Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Create instances of agent and environment
agent = GoalBasedAgent(goal_node)
environment = Environment(graph)

# Run the agent
run_agent(agent, environment, start_node)
