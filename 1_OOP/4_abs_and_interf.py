from abc import ABC, abstractmethod

'''
    Первый вариант
'''

class Transport(ABC):
    def __init__(self):
        self.engine = False
        self.is_moving = False

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def start_engine(self):
        self.engine = True

    def stop_engine(self):
        self.engine = False

    def move(self):
        self.engine = True
        self.is_moving = True


class Boat(Transport):
    def start_engine(self):
        self.engine = True

    def stop_engine(self):
        self.engine = False

    def move(self):
        self.engine = True
        self.is_moving = True


'''
    Второй вариант
'''

class Transport2(ABC):
    def __init__(self):
        self.engine = False

    def start_engine(self):
        self.engine = True

    def stop_engine(self):
        self.engine = False

    @abstractmethod
    def move(self):
        pass


class Car2(Transport2):
    def __init__(self):
        super().__init__()
        self.wheels_moving = False

    def move(self):
        self.start_engine()
        self.wheels_moving = True


class Boat2(Transport2):
    def __init__(self):
        super().__init__()
        self.is_moving = False

    def move(self):
        self.start_engine()
        self.is_moving = True

