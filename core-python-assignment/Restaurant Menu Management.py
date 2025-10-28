def display_menu():
    print("\n--- Restaurant Menu Management ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Check Item Availability")
    print("4. View Menu")
    print("5. Exit")

def add_item(menu):
    item = input("Enter the item name to add: ").strip()
    if item:
        if item not in menu:
            menu.append(item)
            print(f"'{item}' has been added to the menu.")
        else:
            print(f"'{item}' is already in the menu.")
    else:
        print("Item name cannot be empty.")

def remove_item(menu):
    item = input("Enter the item name to remove: ").strip()
    if item:
        if item in menu:
            menu.remove(item)
            print(f"'{item}' has been removed from the menu.")
        else:
            print(f"'{item}' is not in the menu.")
    else:
        print("Item name cannot be empty.")

def check_item(menu):
    item = input("Enter the item name to check availability: ").strip()
    if item:
        if item in menu:
            print(f"'{item}' is available in the menu.")
        else:
            print(f"'{item}' is not available in the menu.")
    else:
        print("Item name cannot be empty.")

def view_menu(menu):
    if menu:
        print("\nCurrent Menu:")
        for idx, item in enumerate(menu, 1):
            print(f"{idx}. {item}")
    else:
        print("The menu is currently empty.")

def main():
    menu = ["Pizza", "Burger", "Pasta", "Salad"] 

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                add_item(menu)
            elif choice == 2:
                remove_item(menu)
            elif choice == 3:
                check_item(menu)
            elif choice == 4:
                view_menu(menu)
            elif choice == 5:
                print("Exiting the menu management system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-5).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
