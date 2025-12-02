# Define the Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute
        self.grade = grade

    def introduce(self):
        # Print the introduction message
        print("Hey, I am", self.name, "and I am", self.age, "years old. I am in grade", self.grade)

# Create a Student object with name "Alice" and age 21
student1 = Student("Alice", 21, 10)

# Call the introduce method
student1.introduce()

print(student1)  # Output the name attribute