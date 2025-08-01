shopping_list = []

print("Welcome to your shopping list!")
print("Your current list:", shopping_list)

while True:
    print("\nChoose an option:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Quit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number (1-4).")
        continue

    if choice == 1:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' not found in the list.")
    elif choice == 3:
        print("Your current shopping list:", shopping_list)
    elif choice == 4:
        print("Final shopping list:", shopping_list)
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose from 1 to 4.")