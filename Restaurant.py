# Welcoming the user
print("Welcome to the Restaurant...")

# Menu
menu = {
    "Burger": 60,
    "Pizza": 100,
    "Sandwich": 50,
    "Cold Coffee": 150,
    "Coffee": 70,
    "Maggie": 40,
    "Fries": 80,
}

# Displaying menu to the user
print("\nMenu:")
for item, price in menu.items():
    print(f"{item} - {price} Rupees")

order_total = 0

while True:
    # Taking the order from the user
    item1 = input("\nWhat would you like to have: ")
    if item1 in menu:
        print(f"Your {item1} is added successfully.")
        order_total += menu[item1]
    else:
        print("Sorry, we don't have that.")

    new_dish = input("Would you like to have something else? (Yes/No): ")
    if new_dish == "no":
        break

print(f"\nYour total bill is: {order_total} Rupees")
print("Thank you for visiting our restaurant!")
