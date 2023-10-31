class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""

        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fishes":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "birds":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
animals = int(input())
zoo = Zoo(zoo_name)

for i in range(animals):
    current_animal = input().split()
    species = current_animal[0]
    name = current_animal[1]
    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))