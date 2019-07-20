class Number:
    def __init__(self, start_num):
        self.start_num = start_num


    def loop(self):
        for x in range(self.start_num + 1):
            print(x)


n1 = int(input())

data = Number(start_num=n1)

print(f"{data.loop()}")
