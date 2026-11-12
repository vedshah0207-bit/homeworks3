total = int(input("Give the total amt to pay. "))
total_pay = int(input("How much have you paid. "))

def find_change(total, paid):
    return paid - total

print("You will receive", find_change(total, total_pay))