# list_report.py

# Start with the exact required list
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

print("=== NUMBERED SHOPPING LIST ===")
# Loop through the list and print each item numbered (1-indexed)
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# Count how many item names have more than 4 letters using a loop + an if
count_more_than_four = 0
for item in items:
    if len(item) > 4:
        count_more_than_four += 1

print(f"\nItems with more than 4 letters: {count_more_than_four}")

# Find and print the longest item name using a loop comparison (no shortcuts like max())
longest_name = items[0]  # Assume the first item is the longest initially
for item in items:
    if len(item) > len(longest_name):
        longest_name = item

print(f"Longest item name: {longest_name}")
