from array import *

var = array('i', [1,2,3,4,5,6,7,8,9])
print("Original array: ", end="")
for i in var:
    print(i, end=" ")
print("\n")

#array reverse
#insert(index, value)                               (insert value at index)
#append(value)                                      (append to last)
#var[index] = value                                 (change value on that index)
#index(value)                                       (index of that value)
#pop()                                              (delete value from last)
#pop(index)                                         (delete value of that index)
#var[starting index : ending index]                 (slice the array (include start & exclude end)
#var[::-1]                                          (Reversing the array using slice)
#array input


#array reverse
var.reverse()
print("Array after reverse: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


#insert(index, value) 
var.insert(2, 100)
print("Insert 100 at index 2: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


#append(value) 
var.append(300)
print("append 300 (append->at last): ", end="")
for i in var:
    print(i, end=" ")
print("\n")


#var[index] = value 
var[4] = 200
print("change to 200 at index 4: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


#index(value)
print("Print the value of index 2: ", var.index(2))
print("\n")


#pop() 
var.pop()
print("after removing value from last index: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


#pop(index) 
var.pop(7)
print("after removing value from 7th index: ", end="")
for i in var:
    print(i, end=" ")
print("\n")


#var[starting index : ending index]
var1 = var[2:5]
print("after slicing [2:5]: ", end="")
for i in var1:
    print(i, end=" ")
print("\n")


#var[starting index : ending index]
var1 = var[1:-2]
print("after slicing [1:-2]: ", end="")
for i in var1:
    print(i, end=" ")
print("\n")


#var[::-1] 
var1 = var[::-1]
print("after reversing the array using slice [::-1]: ", end="")
for i in var1:
    print(i, end=" ")
print("\n")

#array input
new_arr = array('i', [] )
n = int(input("How many number do you want to add: "))
for i in range(0, n):
    new_arr.append(int(input(f"Enter the {i+1} number: ")))

print("Your input array is: ", end="")

for i in new_arr:
    print(i, end=" ")