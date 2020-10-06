# ARRAY
from array import *

arr = array('i', [20, 1, 23, 4, 72])
for i in arr:
    print(i)
print(arr)
# print(sorted(arr))
val = int(input("Searching value: "))
print(arr.index(val))
