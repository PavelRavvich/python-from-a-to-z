class Person:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_string(self):
        print(str(self.name) + ' : ' + str(self.age))


class Student(Person):
    course = None

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def to_string(self):
        print(str(self.name) + ' : ' + str(self.age) + ' : ' + str(self.course))



joe = Person('Joe', 24)
joe.to_string()

max = Student('Joe', 24, 2)
max.to_string()