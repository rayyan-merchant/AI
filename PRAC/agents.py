# Q1
import random

class Environment:

  def __init__(self):
    self.components = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    self.state = {component: random.choice(["safe", "vulnerable"]) for component in self.components}


  def get_state(self):
    return self.state


class Agent:

  def __init__(self):
    self.vulnerable_components = []

  def scan(self,  environment):
    state = environment.get_state()

    for component, status in state.items():
      if status == "vulnerable":
        self.vulnerable_components.append(component)
        print(f"Warning: Component {component} is vulnerable.")
      elif status == 'safe':
        print(f"Success: Component {component} is safe.")

  def patching_vulnerabilities(self, environment):
    state = environment.get_state()
    for component in self.vulnerable_components:
      state[component] = "safe"
      print(f"Success: Component {component} has been patched and is now marked as safe")
    environment.state = state

  def get_vulnerable_components(self):
    return self.vulnerable_components


def run_agent(agent, environment):
  print("Scanning...")
  agent.scan(environment)
  print("Patching vulnerabilities...")
  agent.patching_vulnerabilities(environment)
  print("Final system state:")
  print(environment.get_state())


agent = Agent()
environment = Environment()

run_agent(agent, environment)






# Q2
import random

class Environment:
    def __init__(self):
        self.servers = [1, 2, 3, 4, 5]
        self.state = {server: random.choice(["underloaded", "balanced", "overloaded"]) for server in self.servers}

    def get_state(self):
        return self.state

    def update_state(self, new_state):
        self.state = new_state

class LoadBalancerAgent:
    def __init__(self):
        self.overloaded_servers = []
        self.underloaded_servers = []

    def scan(self, environment):
        state = environment.get_state()
        self.overloaded_servers = [server for server in state if state[server] == "overloaded"]
        self.underloaded_servers = [server for server in state if state[server] == "underloaded"]

        for server in self.overloaded_servers:
            print(f"Warning: Server {server} is overloaded.")
        for server in self.underloaded_servers:
            print(f"Note: Server {server} is underloaded.")

    def load_balancing(self, environment):
        state = environment.get_state()

        while self.overloaded_servers and self.underloaded_servers:
            overloaded_server = self.overloaded_servers.pop()
            underloaded_server = self.underloaded_servers.pop()

            state[overloaded_server] = "balanced"
            state[underloaded_server] = "balanced"

            print(f"Balanced: Server {overloaded_server} offloaded tasks to Server {underloaded_server}.")

        environment.update_state(state)

def run_agent():
    environment = Environment()
    agent = LoadBalancerAgent()

    print("Initial State:")
    print(environment.get_state())

    print("Scanning...")
    agent.scan(environment)

    print("Load balancing...")
    agent.load_balancing(environment)

    print("Final system state:")
    print(environment.get_state())

run_agent()






# Q3
import random

class Environment:
  def __init__(self):
    self.tasks = [1, 2, 3, 4, 5]
    self.state = {task: random.choice(["completed", "failed"]) for task in self.tasks}

  def get_state(self):
    return self.state

  def get_tasks(self):
    return self.tasks


class BackupManagementAgent:

  def __init__(self):
    self.failed_tasks = []

  def scan(self, environment):
    state = environment.get_state()
    for task in state:
      if state[task] == 'failed':
        self.failed_tasks.append(task)
        print(f"Warning: Task {task} is failed.")
    return self.failed_tasks

  def retry_failed_tasks(self, environment):
    state = environment.get_state()
    for task in self.failed_tasks:
      state[task] = 'completed'
      print(f"Success: Task {task} has been retried and completed")
    environment.state = state
    return environment.state


def run_agent(agent, environment):
  print("Initial State:")
  print(environment.get_state())
  print("Scanning...")
  agent.scan(environment)
  print("Retrying failed tasks...")
  agent.retry_failed_tasks(environment)
  print("Final system state:")
  print(environment.get_state())


agent = BackupManagementAgent()
environment = Environment()

run_agent(agent, environment)




# Q4
import random

class Environment:

  def __init__(self):
    self.components = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    self.state = {component: random.choice(["safe", "low risk", "high risk"]) for component in self.components}

  def get_state(self):
    return self.state


class Agent:

  def __init__(self):
    self.risks = []

  def scan(self, environment):
    state = environment.get_state()
    for component, risk in state.items():
      if risk == "low risk":
        print(f"Warning: Component {component} has a low risk vulnerability.")
        self.risks.append(component)
      elif risk == "high risk":
        print(f"Warning: Component {component} has a high risk vulnerability.")
        self.risks.append(component)
      elif risk == "safe":
        print(f"Success: Component {component} is safe.")

  def patching_vulnerabilities(self, environment):
    state = environment.get_state()
    for component, risk in state.items():
      if risk == "low risk":
        state[component] = "safe"
        print(f"Success: Component {component} has been patched and is now marked as safe")
      elif risk == "high risk":
        print(f"Warning: Component {component} has a high risk vulnerability and requires premium patching.")
    environment.state = state
    return environment.state


def run_agent(agent, environment):
  print("Initial State: ")
  print(environment.get_state())
  print("Scanning...")
  agent.scan(environment)
  print("Patching vulnerabilities...")
  agent.patching_vulnerabilities(environment)
  print("Final system state:")
  print(environment.get_state())


agent = Agent()
environment = Environment()

run_agent(agent, environment)




# Q5
import random

class Environment:

  def __init__(self):
    self.corridors = ["Corridor 1", "Corridor 2"]
    self.rooms = ["Room 101", "Room 102", "Room 103"]
    self.nurse_stations = ["Nurse Station A", "Nurse Station B"]
    self.medicine_storage = "Medicine Storage"
    self.task = [
        {"room": "Room 101", "medicine": "Aspirin", "patient_id": "P1001", "delivered": False},
        {"room": "Room 102", "medicine": "Antibiotic", "patient_id": "P1002", "delivered": False},
        {"room": "Room 103", "medicine": "Insulin", "patient_id": "P1003", "delivered": False},
    ]

  def get_state(self):
    return self.task


class Agent:

  def __init__(self):
    self.current_location = "Starting Point"

  def move_to(self, destination):
    print(f"Moving from {self.current_location} to {destination}...")
    self.current_location = destination
    print(f"Arrived at {self.current_location}.\n")

  def pick_up_medicine(self, medicine):
    print(f"Picking up {medicine} from the medicine storage...")
    print(f"{medicine} has been picked up.\n")

  def scan_patient_id(self, expected_id):
    print("Scanning patient ID...")
    success = random.random() < 0.9
    scanned_id = expected_id if success else "UNKNOWN"
    print(f"Scanned patient ID: {scanned_id} (expected: {expected_id})")
    return scanned_id == expected_id

  def deliver_medicine(self, task):
    print(f"Delivering {task['medicine']} to {task['room']}...")
    print("Medicine delivered successfully.\n")

  def alert_staff(self, room):
    print(f"Alerting staff at nurse station regarding an issue at {room}...")
    print("Staff has been alerted.\n")

  def execute_delivery(self, environment):
    tasks = environment.get_state()
    print("Starting delivery tasks...\n")

    for task in tasks:
      print(f"Processing task for {task['room']}: Deliver {task['medicine']} to patient {task['patient_id']}")
      self.move_to(task["room"])
      self.pick_up_medicine(task["medicine"])
      if self.scan_patient_id(task["patient_id"]):
        self.deliver_medicine(task)
      else:
        print("Patient ID mismatch detected!")
        self.alert_staff(task["room"])
      self.move_to(random.choice(environment.corridors))

    print("All tasks processed.\n")


def run_agent(agent, environment):
  print("Initial State: ")
  print(environment.get_state())
  print("Executing delivery tasks...")
  agent.execute_delivery(environment)


agent = Agent()
environment = Environment()

run_agent(agent, environment)



# Q6
class Environment:
  def __init__(self):
    self.grid = {
        'a': 'safe', 'b': 'safe', 'c': 'fire',
        'd': 'safe', 'e': 'fire', 'f': 'safe',
        'g': 'safe', 'h': 'safe', 'j': 'fire'
    }

  def get_status(self):
    return self.grid

  def update_status(self, room, status):
    self.grid[room] = status

  def display(self):
      rows = [
          ['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'j']
      ]
      symbol = lambda status: "🔥" if status == 'fire' else " "
      print("Current Environment:")
      for row in rows:
          print(" | ".join(symbol(self.grid[room]) for room in row))
      print()


class Robot:
  def __init__(self):
    self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    self.position = self.path[0]

  def move(self, environment):
    for room in self.path:
      self.position = room
      print(f"Robot is moving to room '{self.position}'...")

      if environment.grid[room] == 'fire':
        print(f"Fire detected in room '{self.position}'. Extinguishing fire...")
        environment.update_status(room, 'safe')
      else:
        print(f"Room '{self.position}' is already safe.")
      environment.display()


def run_agent(agent, environment):
  state = environment.get_status()
  print("Initial State: ")
  print(state)
  print("Executing delivery tasks...")
  agent.move(environment)
  print("Final State: ")
  print(environment.get_status())


agent = Robot()
environment = Environment()

run_agent(agent, environment)
