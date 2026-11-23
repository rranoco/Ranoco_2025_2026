#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display(self):
        return f"name {self.name}; age: {self.get_age()}"

    def study(self, subject):
        return f"{self.name} is studying."

person1 = Person("Ryz", 15)
student1 = Person("Lina", 20)
print(person1.display())
print(student1.study())

#   It's better to access age through the getter method or get_age because it ensures that the code for age is private and cannot be accessed directly.