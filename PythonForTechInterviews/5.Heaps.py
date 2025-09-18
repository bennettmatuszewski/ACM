import heapq

# heaps good for min and max
# arrays under the hood, default is minheap
# O(log(n)) push and pop

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0]) # min always index 0 

while len(minHeap):
    print(heapq.heappop(minHeap))

# no max heap by default
# use min heap and multiply by -1 when push and pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

#max at index 0
print(-1*maxHeap[0])

#build heap from initial values
arr = [2,1,8,4,5]
heapq.heapify(arr) # creates heap in O(n) instead of O(nlog(n))

# heap sort, time complexity: O(n log(n)), space complexity: O(n)
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0] * n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list

# CHALLENGE 
# Given the followijng array, print the 3 smallest numbers
arr = [7, 2, 9, 4, 1, 6, 3]
heapq.heapify(arr)  # turn list into min heap

for i in range(3):  # extract 3 smallest numbers
    print(heapq.heappop(arr))