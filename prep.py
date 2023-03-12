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
