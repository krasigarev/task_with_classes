class Number:
    def __init__(self, start_num, end_num, step):
        self.start_num = start_num
        self.end_num = end_num
        self.step = step

    def loop(self):
        for x in range(self.start_num, self.end_num, self.step):
            print(x)


n1 = int(input())
n2 = int(input())
n3 = int(input())

data = Number(start_num=n1, end_num=n2, step=n3)


print(f"{data.loop()}")

