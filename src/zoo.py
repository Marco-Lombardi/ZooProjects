class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id


    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def add_animal(self, animal, fence):
        if fence.area >= animal.height * animal.width and fence.habitat == animal.preferred_habitat:
            fence.animals.append(animal)
            return True
        else:
            return False

    def remove_animal(self, animal, fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            return True
        else:
            return False

    def feed(self):
        for fence in self.fences:
            for animal in fence.animals:
                if fence.area >= (animal.height + 0.02 * animal.height) * (animal.width + 0.02 * animal.width):
                    animal.health += 1
                    animal.height += 0.02 * animal.height
                    animal.width += 0.02 * animal.width

    def clean(self):
        total_cleaning_time = 0.0
        for fence in self.fences:
            area_occupied = sum(animal.height * animal.width for animal in fence.animals)
            cleaning_time = area_occupied / (fence.area - area_occupied) if fence.area - area_occupied != 0 else area_occupied
            total_cleaning_time += cleaning_time
        return total_cleaning_time

    def describe_zoo(self):
        zoo_info = ""
        zoo_info += "Guardiani dello zoo:\n"
        for keeper in self.zoo_keepers:
            zoo_info += f"{keeper.name} {keeper.surname}, ID: {keeper.id}\n"

        zoo_info += "\nRecinti dello zoo:\n"
        for i, fence in enumerate(self.fences):
            zoo_info += f"\nRecinto {i + 1}:\n"
            zoo_info += f"Area: {fence.area}\n"
            zoo_info += f"Temperatura: {fence.temperature}\n"
            zoo_info += f"Habitat: {fence.habitat}\n"
            zoo_info += "Animali:\n"
            for animal in fence.animals:
                zoo_info += f"- Nome: {animal.name}, Specie: {animal.species}, Salute: {animal.health}%\n"
        
        return zoo_info
