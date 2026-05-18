
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}'


class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language

    def get_info(self):
        info = super().get_info()
        info += f' Programming Language: {self.programming_language}'
        return info


class Manager(Employee):
    def __init__(self, name, position, salary, employees: list):
        super().__init__(name, position, salary)
        self.employees = employees

    def get_info(self):
        info = super().get_info()
        employees_names = [employee.name for employee in self.employees]
        info += f' Employees: {employees_names}'
        return info
