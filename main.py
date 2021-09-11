
base_bill = float(input("Please enter the amount of the bill you have to pay: \n"))

party_size = int(input("Please enter the number of people in your group: \n"))

decided_tip = float(input("In decimal, please enter the total tip decided for the bill: \n"))

def tip_calculator():

    raw_total = (base_bill / party_size) * (decided_tip + 1)

    return "%.2f" %raw_total

print(f"The amount each person should pay is: ${tip_calculator()}.")