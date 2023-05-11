# This program simulates a simple grocery shop where items can be added to a cart and the total cost can be calculated.

# Define the prices of the items
prices = {
    "apple": 0.75,
    "banana": 1.25,
    "bread": 2.50,
    "cheese": 3.75,
    "milk": 2.00
}

# Define a function to add items to the cart
def add_item(cart, item, quantity):
    if item in prices:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.")
    else:
        print(f"Sorry, we don't have {item} in stock.")

# Define a function to calculate the total cost of the items in the cart
def calculate_total(cart):
    total = 0
    for item, quantity in cart.items():
        if item in prices:
            total += prices[item] * quantity
    return total

# Define the main function
def main():
    cart = {}
    while True:
        print("Please select an option:")
        print("1. Add item to cart")
        print("2. Calculate total cost")
        print("3. Exit")
        choice = input()
        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(cart, item, quantity)
        elif choice == "2":
            total = calculate_total(cart)
            print(f"Total cost: ${total:.2f}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the program
if __name__ == "__main__":
    main()