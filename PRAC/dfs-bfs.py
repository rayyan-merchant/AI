maze =[
    ['O' ,'O', 'X' ,'O' ,'T'],
    ['O', 'X', 'O', 'O', 'X'],
    ['P' ,'O' ,'O' ,'X' ,'O'],
    ['X' ,'X', 'O', 'O', 'O'],
    ['O' ,'O' ,'O', 'X' ,'O']
]

def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])
    directions = [[1,0], [0,1], [-1,0], [0,-1]]
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] in {'O', 'P', 'T'}:
                neighbors = []
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < rows and 0 <= y < cols and maze[x][y] in {'P', 'O', 'T'}:
                        neighbors.append((x, y))
                graph[(i, j)] = neighbors
    return graph

def get_pos(maze):
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'P':
                start = (i,j)
            if maze[i][j] == 'T':
                goal =  (i,j)
    return start, goal

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    print("\nBFS\n")
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            print(f"Goal found -> {path}")
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                    queue.append((neighbor, path + [neighbor]))
    print("Goal not found")
    return None

def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    print("\nDFS\n")
    while stack:
        node, path = stack.pop()
        if node == goal:
            print(f"Goal found -> {path}")
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                    stack.append((neighbor, path + [neighbor]))
    print("Goal not found")
    return None

graph = create_graph(maze)
start, goal = get_pos(maze)
bfs(graph, start, goal)
dfs(graph, start, goal)









maze = [
    [1, 1, 0, 1, 1],  #(2,0) -> (0,4)
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

def create_graph(maze):
    directions = [[1,0], [0,1], [-1, 0], [0, -1]]
    graph = {}
    rows = len(maze)
    cols = len(maze[0])
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                neighbors = []
                for dx, dy in directions:
                    nx, ny = i+dx, j+dy
                    if 0<= nx < rows and 0<= ny< cols and maze[nx][ny] == 1:
                        neighbors.append((nx,ny))
                graph[(i,j)] = neighbors
    return graph

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    print("\nBFS SEARCH\n")
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            print(f"Goal found -> {path}")
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    print("Goal not found")
    return None

def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    print("\nDFS SEARCH\n")
    while stack:
        node, path = stack.pop()
        if node == goal:
            print(f"Goal found -> {path}")
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

graph = create_graph(maze)
bfs(graph, (2,0), (0,4))
dfs(graph, (2,0), (0,4))






from collections import deque

# Graph Implementation
class GoalBasedAgentGraph:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        return percept == self.goal

    def act(self, percept, environment):
        if self.formulate_goal(percept):
            return f"Goal {self.goal} found!"
        else:
            return environment.bfs_search(percept, self.goal)

class EnvironmentGraph:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def bfs_search(self, start, goal):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            node, path = queue.popleft()
            print(f"Visiting: {node}")
            if node == goal:
                return f"Goal {goal} found! Path: {path}"

            if node in visited:
                continue

            visited.add(node)
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))

        return "Goal not found"

# Tree Implementation
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_tree(root, goal):
    queue = deque([(root, [root.value])])
    while queue:
        node, path = queue.popleft()
        if node.value == goal:
            return f"Goal {goal} found! Path: {path}"
        for child in node.children:
            queue.append((child, path + [child.value]))
    return "Goal not found"

# Maze Implementation
def bfs_maze(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return f"Goal {goal} found! Path: {path}"
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))

    return "Goal not found"
