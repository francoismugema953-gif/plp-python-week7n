# Shopping List Manager

- `list_warmup.py`: Practices basic list creation, indexing, appending, removing elements, and tracking length.
- `shopping_list.py`: An interactive, robust console program that lets users add, remove, show, or quit a dynamic shopping list without crashing on missing items.
- `list_report.py`: Analyzes a predefined list to print numbered items, count items with names longer than four characters, and find the longest item name manually using a loop.

### Why is it safer to check `in` before calling `.remove()`?
Checking if an item exists in the list using the `in` keyword before calling `.remove()` prevents Python from throwing a `ValueError`. If you try to remove an item that isn't present in the list, Python halts execution and crashes your program, whereas a membership check lets you handle the missing item safely with custom feedback.
