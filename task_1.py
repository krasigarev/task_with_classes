class Test:
    def __init__(self, name, age, town, salary):
        self.name = name
        self.age = age
        self.town = town
        self.salary = salary


name = input()
age = int(input())
town = input()
salary = float(input())
data = Test(name=name, age=age, town=town, salary=salary)

print(f"{data.name} is {data.age} old, is from {data.town} and makes ${data.salary}")