class Student:
    student ={
        "id": [101, 102, 103, 104, 105, 106, 107, 108],
        "name": ['Sahil','Rohit','Rahul','Rajeev','Ramesh','Rakesh','Ravi','Rohit'],
        "age": [20, 22, 21, 23, 20, 22, 21, 23],
        "grade": ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
    }
    def __init__(self,id):
        self.id = id
        self.name = self.student["name"][id]
        self.age = self.student["age"][id]
        self.grade = self.student["grade"][id]

    def get_name(self, id):
        return self.student["name"][id]

    def get_age(self, id):
        return self.student["age"][id]

    def get_grade(self, id):
        return self.student["grade"][id]

    def set_name(self, name, id):
        self.student["name"][id] = name

    def set_age(self, age, id):
        self.student["age"][id] = age

    def set_grade(self, grade, id):
        self.student["grade"][id] = grade

s1=Student(0)
print(s1.get_name(0))  # Output: Sahil
print(s1.get_age(0))   # Output: 20
print(s1.get_grade(0)) # Output: A
print("Before update:", s1.get_name(0), s1.get_age(0), s1.get_grade(0))
s1.set_name("Bob", 0)
s1.set_age(22, 0)
s1.set_grade("B", 0)
print("After update:", s1.get_name(0), s1.get_age(0), s1.get_grade(0))
print("Before update:", s1.get_name(0), s1.get_age(0), s1.get_grade(0))