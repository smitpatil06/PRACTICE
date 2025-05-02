class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def celebrate(person):
    print(f"Happy Birthday, {person.name}!")
    person.age += 1
    print(f"{person.name} is now {person.age} years old.")


p1 = Person("Alice", 25)
celebrate(p1)
