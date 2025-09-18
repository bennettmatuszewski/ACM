arr = [5,4,7,3,8]
arr.sort() # do not do arr = arr.sort() or sort(arr)
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

#custom sort by length of string
arr.sort(key=lambda x: len(x))

arr = [i for i in range(5)]
print(arr)

arr = [i+1 for i in range(5)]
print(arr)

# 2d lists
arr = [[0] * 4 for i in range(4)]
print(arr)


# strings are similar to arrays
s = "abc"
print(s[0])
print(s[0:2])
# can't do s[1] = h
s+="def" # creates new stirng in O(n) time

strings = ["ab","cd","ef"]
print(": ".join(strings))

string = "ab_cd_ef"
print(string.split("_"))

# create an array in one line with values from 2, 7, then sort the array in descending order
arr = [i for i in range(2,8)]
arr.sort(reverse=True)
print(arr)