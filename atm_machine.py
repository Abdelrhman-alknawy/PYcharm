# This program simulates a basic ATM machine with withdraw, deposit, and balance inquiry functions.

# Define the initial balance
balance = 1000

# Define the functions for withdraw, deposit, and balance inquiry
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Current balance is {balance}.")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposit successful. Current balance is {balance}.")

def balance_inquiry():
    global balance
    print(f"Current balance is {balance}.")

# Define the main function
def main():
    while True:
        print("Welcome to the ATM machine.")
        print("Please select an option:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Balance inquiry")
        print("4. Exit")
        choice = input()
        if choice == "1":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == "3":
            balance_inquiry()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
