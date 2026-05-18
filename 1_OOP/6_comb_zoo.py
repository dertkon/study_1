from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Flyable:
    def move(self):
        return "I'm flying!"


class Swimmable():
    def move(self):
        return "I'm swimming!"


class Dog(Animal):
    def speak(self):
        return 'Woof!'

    def move(self):
        return 'Я бегаю'


class Bird(Flyable, Animal):
    def speak(self):
        return 'Tweet!'


class Fish(Swimmable, Animal):
    def speak(self):
        return ' . . . '


hatiko = Dog()
woody = Bird()
nemo = Fish()

animals = [hatiko, woody, nemo]

for animal in animals:
    print(animal.speak())
    print(animal.move())
