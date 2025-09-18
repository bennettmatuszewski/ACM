# Hashmap aka dict
myMap = {}
myMap = dict()
myMap["alice"] = 88
myMap["bob"] = 77

print(myMap)
print(len(myMap)) #num keys in hashmap
print(myMap["alice"])
print(myMap.get("alice2", 123123)) #2nd parameter is fallback

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 88, "bob": 77}

#looping
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key,val)

# Tuples like arrays but immutable
tup = (1,2,3)
print(tup)
print(tup[1])
print(tup[-1])
#tup[1] = 1 doesn't work

#tuples mostly used as keys for hashmap/hashset, as lists/arrays can't be used as keys
myMap = {(1,2):3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

#CHALLENGE, given the following array of letters, print out the frequencies of each letter using a hashmap
letters = ["a", "b", "a", "c", "b", "a"]
# a 3
# b 2
# c 1

freq = {}  # dictionary to store counts

for letter in letters:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

# print word counts
for word, count in freq.items():
    print(word, count)

# 