# import array
# import array as arr
from array import *


#1 import array   
# var = array.array('i', [1,2,3,4,5,6,7,8,9]) # here typecode is 'i' that is for int, 'd' for double

#2 import array as arr  
# var = arr.array('i', [1,2,3,4,5,6,7,8,9]) # here typecode is 'i' that is for int, 'd' for double

#3 from array import *
var = array('i', [1,2,3,4,5,6,7,8,9]) # here typecode is 'i' that is for int, 'd' for 

print(f"typecode of var is: {var.typecode}")

print("\n")

for i in range(0, len(var)):
    print(i, end=" ")

print("\n")

# best way to print array
for i in var:
    print(i, end=", ")