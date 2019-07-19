class Test:
    def __init__(self, name, age, town, salary):
        self.name = name
        self.age = age
        self.town = town
        self.salary = salary


    def age_range(self):
        range_age = None
        if age <= 18:
            range_age = 'teen'
        elif age <= 70:
            range_age = 'aduit'
        else:
            range_age = 'elder'
        return range_age


    def salary_range(self):
        range_salary = 0
        if salary <= 500:
            range_salary = 'low'
        elif age <= 2000:
            range_salary = 'medium'
        else:
            range_salary = 'high'
        return range_salary


name = input()
age = int(input())
town = input()
salary = float(input())
data = Test(name=name, age=age, town=town, salary=salary)


print(f"Name: {data.name}\n"
      f"Age: {data.age}\n"
      f"Town: {data.town}\n"
      f"Salary: {data.salary}\n"
      f"Age range: {data.age_range()}\n"
      f"Salary range: {data.salary_range()}\n")

