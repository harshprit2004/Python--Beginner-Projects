balance = 0
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. New balance: ₹{balance}")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
    else:
        print("Not Enough balance")

def check_balance():
    print(f"Current balance: ₹{balance}")

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    i = input("Enter your choice (1-4): ")
    if i == '1':
        amt = int(input("Enter amount to deposit: ₹"))
        deposit(amt)
    elif i == '2':
        amt = int(input("Enter amount to withdraw: ₹"))
        withdraw(amt)
    elif i == '3':
        check_balance()
    elif i == '4':
        print("Thank you for using the Bank App!")
        break
    else:
        print("Invalid")
