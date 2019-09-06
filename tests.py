def singleton(cl):
    instance = None
    print(id(instance))

    def wrapper(*args):
        nonlocal instance
        if not instance:
            instance = cl(*args)
        return instance
    return wrapper


# @singleton
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def return_sum(x, y):
        return x+y

    def func_3(self, x, y):
        return Employee.return_sum(x, y)


print(Employee.return_sum(5, 8))