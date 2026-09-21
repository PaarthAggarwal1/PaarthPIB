def find_duplicates(items):
    duplicates = []
    for item in items:
        if items.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
    return duplicates

items_list = [1, 2, 3, 2, 4, 1, 5, 2]
duplicates = find_duplicates(items_list)
print(duplicates)