class LivingBeing:
    def __init__(self, name):
        self.name = name

class Persona(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        print("Hello! I am a person.")

class Student(Persona):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().greet()
        print(f"Hello! I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}.")

student = Student("Ana", 29, "S123")
student.greet()