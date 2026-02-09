inventory = {"apple": 10, "banana": 5, "milk": 2}

print("1. Add item")
print("2. Sell item")
choice = int(input("Enter choice: "))

if choice == 1:
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    inventory[item] = inventory.get(item, 0) + qty

elif choice == 2:
    item = input("Enter item name: ")
    qty = int(input("Enter quantity to sell: "))
    if item in inventory and inventory[item] >= qty:
        inventory[item] -= qty
    else:
        print("Not enough stock")

print("Low stock items (<3):")
for item, qty in inventory.items():
    if qty < 3:
        print(item, ":", qty)
