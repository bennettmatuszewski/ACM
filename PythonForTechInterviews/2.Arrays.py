# arrays in python are dynamic by defafult, and called listsin python

arr = [1,2,3]

# can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
arr.pop(1) # removes at index 1
print(arr)

arr.insert(1, 7) # inserts 7 at index 1
arr.remove(1) # removes the first "1" in the list
print(arr)

arr[0] = 0

size = 5
arr2 = [1] * size
print(arr2)

print(arr[-1]) # gets last value
print(arr[-2]) # gets 2nd to last value

print(arr[1:3]) # slices array, non-inclusive

print(arr[:3]) # slices array, first 3

print(arr[1:]) # slices array, after index 1, inclusive

# unpacking
a,b,c= [1,2,3]
print(a,b,c)

#looping
for i in range(len(arr)):
    print(arr[i])

#without index
for n in arr:
    print(n)

# with index and value
for i, n in enumerate(arr):
    print(i,n)

# CHALLENGE 
# Given the array arr = [1,2,3,4,5], reverse the array and add it to a new list
arr = [1, 2, 3, 4, 5]
reversed_arr = []

while arr:                 # keep going until arr is empty
    value = arr.pop()      # take the last element out
    reversed_arr.append(value)  # add it to the new list

print(reversed_arr)

# ORRRR
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])