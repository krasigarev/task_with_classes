class Receipt:
    def __init__(self, total, received):
        self.total = total
        self.received = received

    def cash(self):
        print(f"Cash receipt\n"
              f"--------------------------\n"
              f"Charged to_ {total1} _____\n"
              f"Received by_ {reversed1} _\n"
              f"--------------------------\n"
              f"@ Krasi")


total1 = int(input())
reversed1 = int(input())

data = Receipt(total=total1, received=reversed1)

print(data.cash())
