# checking time
import time
start_time = time.time()

end_time = time.time()
print('time:', end_time - start_time)

# common input strategies:
# 1. input()
# 2. map()
#     -ex)   
#         1. list(map(int, input().split()))
#         2. a,b,c = map(int, input().split())

# 3. sys.stdin.readline().rstrip() -> faster than input()
#     - without rstrip(), exist \n at the end of the output.

import sys
data = sys.stdin.readline().rstrip()

# print output:
# use 'end' for replacing \n at the end of the output

a = 1
b = 2
print(a,b) # with \n
print(7, end = " ") # without \n
print(8, end = " ") # without \n

# use f-string
answer = 7
print(f"answer: {answer}") # need not consider the type


# 'global' keyword
# for using the variable that defined outside of the function, use global

a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) # 10

# without global, function can 'infer' the value
a = 0

def func():
    print(a + 10)

func() # 10

# without global, function can 'infer' the list
array = [1,2,3,4,5]

def func():
    array.append(6)
    print(array)

func() # [1,2,3,4,5,6]

# local vs global -> local 

array = [1,2,3,4,5]

def func():
    array = []
    array.append(6)
    print(array)

func() # [6]


# lambda -> easier method to creating simple function
def add(a,b):
    return a+b

# general add() method
print(add(3,7)) # 10 

# lambda add() method
print((lambda a,b: a+b)(3,7)) # 10 

# another example of usage
array = [('a', 50),('b', 32),('c', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key = my_key)) # [('b', 32), ('a', 50), ('c', 74)]
print(sorted(array, key = lambda x:x[1])) # [('b', 32), ('a', 50), ('c', 74)]

# another example of usage

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b,: a+b, list1, list2)

print(list(result)) # [7,9,11,13,15]

# standard libraries:
# 1. built-in function: essential functions
# 2. itertools: for iterative task
# 3. heapq: provide heap data structure; for building priority queue
# 4. bisect: provide binary seearch functions
# 5. collections: provide deque, counter, etc...
# 6. math: factorial, GCD, etc....


# built-in function

# eval() -> calculating human readable math equations
# result = eval("(3+5)*7")
# print(result) # 56

