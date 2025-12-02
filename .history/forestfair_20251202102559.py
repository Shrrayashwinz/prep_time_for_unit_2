class Parrot:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    birdy = Parrot("Polly")
    print(birdy.name)  # Output the name attribute

    def introduce(self):
        print("Hello, I am", self.name, ", I am", self.age, "years old and my color is", self.color)