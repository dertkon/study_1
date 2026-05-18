
class Bird:
    def __init__(self, name):
        self.name = name
        self.is_moving = False

    def speak(self):
        return 'Tweet!'

    def move(self):
        self.is_moving = True
        return "I'm moving!"


class Sparrow(Bird):
    def speak(self):
        return 'Chirik-pizdik-kyky'

    def move(self):
        self.is_moving = True
        return "I'm flying!"


class Penguin(Bird):
    def speak(self):
        return 'AAAAAAAAAAUGH'

    def move(self):
        self.is_moving = True
        return "I'm crawling"


birds = [Bird(name='Bird 1'),
        Sparrow(name='Sparrow 2'),
         Penguin(name='Penguin 3'),]

for bird in birds:
    print(bird.name)
    print(bird.speak())
    print(bird.move())
    print()