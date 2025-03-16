def bfs(graph, start, goal):
    visited = []  # List for visited nodes
    queue = []    # Initialize a queue

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)  # Dequeue
        print(node, end=" ")

        if node == goal:  # Stop if goal is found
            print("\nGoal found!")
            break

        for neighbour in graph[node]: 
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Define Start and Goal Nodes
start_node = 'A'
goal_node = 'I'

# Run BFS
print("\nFollowing is the Breadth-First Search (BFS):")
bfs(graph, start_node, goal_node)




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
            return environment.bfs_search(percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def bfs_search(self, start, goal):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        while queue:
            node = queue.pop(0)
            print(f"Visiting: {node}")

            if node == goal:
                return f"Goal {goal} found!"

            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

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
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

run_agent(agent, environment, start_node)

