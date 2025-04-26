# Project 8 - Concession Stand Program

menu = {"fries" : 1.25,
        "coke" : 1.50,
        "chips" : 1.00,
        "nachos" : 2.50,
        "banana" : 1.25,
        "water" : 0.50,
        "pretzel" : 1.00}
cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:17} : ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item from the menu (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------- YOUR TOTAL ----------")
print()
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your total is: ${total:.2f}")
print()
print("--------------------------------")