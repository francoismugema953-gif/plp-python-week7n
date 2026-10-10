# shopping_list.py

def main():
    # Start with an empty list
    shopping_list = []
    
    print("Welcome to the Shopping List Manager!")
    
    while True:
        # Show menu options
        action = input("\nWould you like to (add / remove / show / done)? ").strip().lower()
        
        if action == "add":
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added.")
            else:
                print("Item name cannot be empty.")
                
        elif action == "remove":
            item = input("Enter the item to remove: ").strip()
            # Check membership with 'in' before removing to prevent crashes
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print("That item is not on your list.")
                
        elif action == "show":
            print("\nCurrent Shopping List:")
            if not shopping_list:
                print("Your list is empty.")
            else:
                for item in shopping_list:
                    print(item)
                    
        elif action == "done":
            print("Goodbye! Thanks for using the Shopping List Manager.")
            break
            
        else:
            print("Invalid choice. Please type: add, remove, show, or done.")

if __name__ == "__main__":
    main()
