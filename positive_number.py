class Number:
    def __init__(self, num):
        self.num = num


    def if_num(self):
        if self.num > 0:
            print(f"The number {self.num} is positive.")
        elif self.num < 0:
            print(f"The number {self.num} is negative.")
        else:
            print(f"The number {self.num} is zero.")


number = float(input())

data = Number(num=number)

print(data.if_num())

