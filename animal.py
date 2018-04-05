# Name: Vinson Aiono
# Date: 4/3/2018
# Coding Dojo Python Stack
# Description: Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

# Create an Animal Class with attributes of name and health
# Create method for walking to decrease health by one and running to increase health by 1
# Print the animal health each time walk/run
# Create instance to walk 3x and run 2x and print health

# Create Dog child class
# inherit everything from animal
#   attribute: default health of dog
#   methods: pet method increase health by 5

# Create Dragon child class
# Default health of 170
# fly() increase health by 10
# display health of 

class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.displayInfo()

    def displayInfo(self):
        print(self.name)
        print(self.health)
    def walk(self):
        self.health -= 1
        print(self.health)
        return self
    def run(self):
        self.health += 1
        print(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)
    def pet(self):
        self.health += 5
        print(self.health)
class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name, 170)
    def fly(self):
        self.health += 10
        print(self.health)
        


animal = Animal('charlie', 100)
rover = Dog('rover')
pete = Dragon('pete')

pete.walk().run().fly()

# rover.walk().walk().pet()

# animal.walk().walk().walk().run().run()

        

