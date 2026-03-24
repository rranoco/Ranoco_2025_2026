product_name = []
product_price = []

def add_product():
    name = input("Enter product name: ")
    while True:
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print("Price cannot be less than or equal to 0!")
            else:
                product_name.append(name)
                product_price.append(price)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_products():
    if len(product_name) == 0:
        print("Add items first!")
    else:
        for i in range(len(product_name)):
            print(str(i + 1) + ".", product_name[i], "-", product_price[i])

def update_price():
    if len(product_name) == 0:
        print("Add items first!")
        return
    name_product = input("Enter item name to update price: ")
    if name_product in product_name:
        index = product_name.index(name_product)
        while True:
            try:
                new_price = float(input("Enter new price: "))
                if new_price <= 0:
                    print("Price cannot be less than or equal to 0!")
                else:
                    product_price[index] = new_price
                    print("Price of", name_product, "updated to ₱", new_price)
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Item not found!")

def search_product():
    if len(product_name) == 0:
        print("Add items first!")
        return
    name = input("Enter item: ")
    if name in product_name:
        index = product_name.index(name)
        print(product_name[index], "-", product_price[index])
    else:
        print("Product not found!")

def menu():
    while True:
        print("[1] Add product")
        print("[2] Display all products")
        print("[3] Update a price")
        print("[4] Search for a product")
        print("[5] Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                add_product()
            elif choice == 2:
                display_products()
            elif choice == 3:
                update_price()
            elif choice == 4:
                search_product()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again")
        except ValueError:
            print("Invalid choice. Please try again")

menu()