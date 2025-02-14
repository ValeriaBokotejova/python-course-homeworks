class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

person_1 = Person("Alessa", 15)
person_2 = Person("Alessa", 15)
print("Are they equal?", person_1 == person_2)
