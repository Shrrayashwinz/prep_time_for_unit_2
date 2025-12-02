# Define the Student class
class Student:
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute

    def introduce(self):
        # Print the introduction message
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Create a Student object with name "Alice" and age 21
student1 = Student("Alice", 21)

# Call the introduce method
student1.introduce()

print(student1)  # Output the name attribute