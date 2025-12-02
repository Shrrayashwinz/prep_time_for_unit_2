class Parrot:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    birdy = Parrot("Polly", 2, "Green")
    print(birdy.name)  # Output the name attribute

class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Max")
print(d.name)
