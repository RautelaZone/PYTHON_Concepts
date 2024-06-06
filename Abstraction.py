from abc import ABC, abstractmethod

''' 
    An abstract in python refers to an abstract base class (ABC) in which 
    methods can be abstract and non abstract in nature.
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        return f"This is an animal named {self.name}."


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Example usage
dog = Dog("Buddy")
print(dog.describe())  # Output: This is an animal named Buddy.
print(dog.make_sound())  # Output: Woof!

cat = Cat("Whiskers")
print(cat.describe())  # Output: This is an animal named Whiskers.
print(cat.make_sound())  # Output: Meow!
