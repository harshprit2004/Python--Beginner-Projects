bill = float(input("Enter total bill amount: ₹"))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people to split the bill: "))

tip = (bill * tip_percent) / 100
total = bill + tip
share = total / people

print("\n--- Tip Splitter ---")
print("Tip amount: ₹", round(tip, 2))
print("Total amount (with tip): ₹", round(total, 2))
print("Each person should pay: ₹", round(share, 2))
