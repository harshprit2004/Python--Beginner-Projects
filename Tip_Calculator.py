bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

tip = (bill * tip_percent) / 100
total = bill + tip

print("Tip:", tip)
print("Total amount to pay:", total)
