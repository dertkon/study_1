
class Flyable:
    def fly(self):
        return "I'm flying!"


class Swimmable():
    def swim(self):
        return "I'm swimming!"


class Duck(Flyable, Swimmable):
    def make_sound(self):
        return 'Quack!'


donald = Duck()

print(donald.fly())
print(donald.swim())
print(donald.make_sound())