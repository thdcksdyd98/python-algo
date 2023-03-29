# 구현: 시뮬레이션과 완전 탐색

# 구현 유형의 문제: 풀이는 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제
# 구현 유형의 예시:
#               1. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
#               2. 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
#               3. 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
#               4. 적절한 라이브러리를 찾아서 사용해야 하는 문제

# 구현 문제에서 2차원 공간은 행렬의 의미로 사용
'''
for i in range(5):
    for j in range(5):
        print('(',i,',',j,')',end = ' ')
    print()
'''

# 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용
'''
#     동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치 
x,y = 2,2

for i in range(4):
    # 다음 위치 
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
'''

# [문제] 상하좌우: 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로
# 나누어져 있다. 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다. A는 상, 하, 좌, 우
# 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1) 이다. A의 이동은 계획서에 따라 행해진다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D중 하나의 문자가 반복적으로 적혀있다. 각 문자의 의미는 다음과 같다

# L: 왼쪽으로 한 칸 이동. 
# R: 오른쪽으로 한 칸 이동. 
# U: 위로 한 칸 이동.
# D: 아래로 한 칸 이동. 

n = int(input())
move = list(map(str, input().split()))
x,y = 1,1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_type = ['R','U','L','D']

# 입력받은 이동 계회을 확인
for m in move:
    # 이동후의 좌표 구하기
    # 사전에 정의된 움직임에 따른 좌표값의 변화값을 인덱스값으로 입력받은 이동 계획과 비교하여 좌표값 업데이트
    for mt in range(len(move_type)):
        if m == move_type[mt]:
            nx = x + dx[mt]
            ny = y + dy[mt]
    # 공간을 벗어나는 케이스 
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x,y)

# [문제] 시각: 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에 3이 하나라도 포함되는 
# 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로
# 세어야 하는 시각 입니다. 

# 00시 00분 03초
# 00시 13분 30초

# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각 입니다. 

# 00시 02분 55초
# 01시 27분 45초

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# [문제] 왕실의 나이트: 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를
# 출력하는 프로그램을 작성하시오. 왕실의 정원에서 행 위치를 표현할 대는 1부터 8로 표현하며, 열 위치를 표현할 때는 
# a부터 h로 표현합니다.

init = list(map(str, input()))
x_board = ['a','b','c','d','e','f','g','h']
count = 0

for i in range(len(x_board)):
    if init[0] == x_board[i]:
        x = int(i) + 1

y = int(init[1])

move_x = [-1,-2,-2,-1,1,2,2,1]
move_y = [2,1,-1,-2,-2,-1,1,2]

for j in range(len(x_board)):
    nx = x + move_x[j]
    ny = y + move_y[j]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
      continue
    count += 1
  
print(count)

# ************************  [책 해답]  **************************************

# uni-code로 변환하여서 입력받은 column값을 숫자로 변경
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
print(row, column)

# 나이트가 이동할 수 있는 8가지 방향에 대해서 좌푣값으로 한꺼번에 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


# [문제] 문자열 재정렬: 알파벳 대문자와 숫자 (0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을
# 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

input_data = input()
number = ['0','1','2','3','4','5','6','7','8','9']

count = 0

for j in input_data:
  if j in number:
    j = int(j)
    count += j
    
letter = sorted([i for i in input_data if i not in number]).append(str(count))

result = ''.join(map(str, letter))

print(type(count))

# ************************  [책 해답]  **************************************

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))