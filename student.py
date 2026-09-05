class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_grade(self, grade):
        self.grade = grade

s1=Student("Alice", 20, "A")
print(s1.get_name())  # Output: Alice
print(s1.get_age())   # Output: 20
print(s1.get_grade()) # Output: A
print("Before update:", s1.get_name(), s1.get_age(), s1.get_grade())
s1.set_name("Bob")
s1.set_age(22)
s1.set_grade("B")
print("After update:", s1.get_name(), s1.get_age(), s1.get_grade())
print("Before update:", s1.get_name(), s1.get_age(), s1.get_grade())