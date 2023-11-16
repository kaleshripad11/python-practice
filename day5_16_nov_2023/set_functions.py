# Functions in set
set_demo = {1, 2, 3, "xyz", "a", 'D'}
new_set = {90,20, 45, 79}

# add() => Add a single item to set
set_demo.add("this is a set")
print(set_demo)

# update() => Add multiple items to set
set_demo.update(["this is a demo set", 100, 300])
print(set_demo)

# Get length of set
print(len(set_demo))

# Remove items from the set
# Use remove(item) to remove the specific item. If we try to remove non-existent item from set, will get KeyError
set_demo.remove(100)
print(set_demo)

# Use discard(item) to remove the specific item.
# Only difference in discard() & item is, discard will not throw any error for non-existent item
set_demo.discard(90)
print(set_demo)

# Use pop() to remove the last item
set_demo.pop()
print(set_demo)

# Concatenate sets using union()
print(set_demo.union(new_set))

# Concatenate sets using update()
set_demo.update(new_set)
print(set_demo)

# Use clear() function to clear entire set. It will return the set()
set_demo.clear()
print(set_demo)