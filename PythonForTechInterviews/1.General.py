import math

a = 0
print(a)
a= "string"
print(a)

#multiple assignments
n, m = 0, "abc"

n = n + 1
n+=1
#n++ doesnt work

# pyhons version of null is None
n = None #null

# don't need brackets
number = 5
if number == 4:
    print("wrong")
elif number == 5:
    print("yay")
else:
    print("wrong")

# different comparison operators
if number < 4:
    print("less than")

if number > 4:
    print("greater than")

if number <= 4:
    print("less than equal")

if number >= 4:
    print("greater than equal")

if number != 4:
    print("not equal")
    

# if statements don't need () unless multi line statements
if (n > 5 and n < 10):
    print("yay")


# loops
while n > 0:
    n-=1
    print(n)

for i in range(5):#0,1,2,3,4 [0,1,2,3,4]
    print(i)
for i in range(2,5):#2,3,4
    print(i)
for i in range(5,1,-1):#5,4,3,2
    print(i)

    #division decimal by default
    print(5/2) #2.5
    print(5//2) #2
    print(10%3) #1
    print(math.floor(3/2)) #1
    print(math.ceil(3/2)) #2
    print(math.sqrt(4)) #2
    print(math.pow(8,2)) #64
    min([5,2,3,1]) #1
    max([5,2,3,1]) #5

# CHALLENGE 
# from numbers 1 to 10, write a for loop to print even if the number is even, and odd if the number is odd
for i in range(1, 11):  # numbers 1 to 10
    if i % 2 == 0:      # check if even
        print("even")
    else:
        print("odd")
