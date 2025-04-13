class Product:
    def __init__(self, name, frequency, volume):
        self.name = name
        self.frequency = frequency
        self.volume = volume
        self.efficiency = frequency / volume

class Slot:
    def __init__(self, id, distance):
        self.id = id
        self.distance = distance
        self.capacity = 1  # Assuming each slot holds one product
        self.assigned_product = None

products = [
    Product("Product 1", frequency=15, volume=2),
    Product("Product 2", frequency=8, volume=1),
    Product("Product 3", frequency=20, volume=3)
]

slots = [
    Slot("Slot 1", distance=1),
    Slot("Slot 2", distance=2),
    Slot("Slot 3", distance=3)
]

products.sort(key=lambda p: p.efficiency, reverse=True)

slots.sort(key=lambda s: s.distance)

assignments = {}
used_slots = set()

for product in products:
    for slot in slots:
        if slot.id not in used_slots:
            assignments[product.name] = slot.id
            used_slots.add(slot.id)
            break

print("Product Assignments (Closer slot = less walking distance):\n")
for product in products:
    assigned_slot = assignments.get(product.name, "Not Assigned")
    print(f"{product.name} → {assigned_slot}")

