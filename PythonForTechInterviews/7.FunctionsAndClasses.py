def myFunc(n,m):
    return n*m
print(myFunc(3,4))

#classes
class MyClass:
    #constructor
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
    def getLength(self): # MUST PASS IN SELF
        return self.size
    def getDoubleLength(self):
        return self.getLength()*2