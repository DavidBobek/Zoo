import uuid


class Caretaker:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        self.id = str(uuid.uuid4())

    def care(self, animal):
        self.animals.append(animal)

    def takeResponsibility(self, list_of_animals):
        for x in list_of_animals:
            self.animals.append(x)
