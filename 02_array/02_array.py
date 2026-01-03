from array import *

# Create an integer array
var = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Print original array
print("Original array: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# ---------------- ARRAY OPERATIONS ----------------

# reverse() → Reverse the array in-place
var.reverse()
print("Array after reversing: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# insert(index, value) → Insert value at a specific index
var.insert(2, 100)
print("After inserting 100 at index 2: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# append(value) → Add value at the end of the array
var.append(300)
print("After appending 300 at the end: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# var[index] = value → Change value at a specific index
var[4] = 200
print("After changing value at index 4 to 200: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# index(value) → Get index of a given value
print("Index of value 2 is:", var.index(2))
print("\n")


# pop() → Remove last element from the array
var.pop()
print("After removing the last element: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# pop(index) → Remove element from a specific index
var.pop(7)
print("After removing the element at index 7: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


# Slicing [start : end] → Start included, end excluded
var1 = var[2:5]
print("Array slice [2:5]: ", end="")
for i in var1:
    print(i, end=" ")
print("\n")


# Slicing with negative index
var1 = var[1:-2]
print("Array slice [1:-2]: ", end="")
for i in var1:
    print(i, end=" ")
print("\n")


# Reverse array using slicing
var1 = var[::-1]
print("Reversed array using slicing [::-1]: ", end="")
for i in var1:
    print(i, end=" ")
print("\n")


# ---------------- USER INPUT ARRAY ----------------

# Create an empty integer array
new_arr = array('i', [])

# Take number of elements from user
n = int(input("How many numbers do you want to add? "))

# Take array elements from user
for i in range(n):
    new_arr.append(int(input(f"Enter number {i + 1}: ")))

# Print user input array
print("Your input array is: ", end="")
for i in new_arr:
    print(i, end=" ")
