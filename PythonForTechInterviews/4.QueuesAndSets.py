from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

#can pop from front with queue in constant time
queue.popleft()
print(queue)

queue.appendleft(1)
queue.pop()

# Sets, search and insert in constant time, no duplicates
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)
print(3 not in mySet)

mySet.remove(2)
print(2 in mySet)

#pass in list to initialize set with values
mySet = set([1,2,3])
print(mySet)

# can also initialize like loops
mySet = {i for i in range(5) }

#CHALLENGE
# given the array, arr = [1, 2, 2, 3, 4, 4, 5], add each value to a queue, ONLY IF the value is a unique value (hasn't been seen before)
queue = deque()
seen = set()

nums = [1, 2, 2, 3, 4, 4, 5]

for n in nums:
    if n not in seen:   # check if it's new
        queue.append(n) # add to queue
        seen.add(n)  

print(queue)