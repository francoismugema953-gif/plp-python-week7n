# list_warmup.py

# 1. Create a list of 5 initial items
shopping_list = ["apples", "milk", "bread", "eggs", "cheese"]

# 2. Print the first and last items using indexing
print("First item:", shopping_list[0])
print("Last item:", shopping_list[-1])

# 3. Add a new item using .append()
shopping_list.append("coffee")

# 4. Remove an item using .remove()
if "bread" in shopping_list:
    shopping_list.remove("bread")

# 5. Check membership with 'in' before acting
item_to_check = "milk"
if item_to_check in shopping_list:
    print(f"Yes, '{item_to_check}' is in the shopping list.")
else:
    print(f"No, '{item_to_check}' is not in the shopping list.")

# 6. Loop through the list to summarize what is inside
print("\nCurrent Shopping List:")
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")
