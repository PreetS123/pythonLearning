# A list stores multiple items in order.
# It is mutable in nature i.e value can be modified afterwards

fruits = ["apple", "banana", "cherry"]


# Accessing items
# print(fruits[0])
# print(fruits[-1])

# Modifying items
# fruits[1] = "mango"
# print(fruits)

# Adding items
fruits.append("orange")
fruits.insert(1, "kiwi")

# Removing items
fruits.remove("apple")
popped_item = fruits.pop()
del fruits[0]

# print(len(fruits))
# print("mango" in fruits)


# tuples
# A tuple is like a list but cannot be changed after creation.

# coordinates = (10, 20)
# print(coordinates[0])

# x, y = coordinates
# print(x, y)


# Sets -- Unordered & Unique
# A set stores unique items only.
# Good for removing duplicates.

numbers = {1, 2, 3, 3, 4, 2, 1}
print(numbers)

numbers.add(4)
numbers.remove(2)

# print(numbers)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
