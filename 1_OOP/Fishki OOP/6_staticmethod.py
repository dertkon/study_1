class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def is_freezing(temp):
        return temp <= 0