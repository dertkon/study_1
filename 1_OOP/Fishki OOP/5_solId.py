class AnimalFlyable:
    def fly(self):
        print("Animal flying")


class AnimalRunnable:
    def run(self):
        print("Animal running")


class AnimalSwimmable:
    def swim(self):
        print("Animal swimming")


class Lion(AnimalRunnable):
    def run(self):
        print("Lion running")
