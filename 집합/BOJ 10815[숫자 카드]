해시 테이블은 연관배열 구조를 이용하여 키(key)에 결과 값(value)을 저장하는 자료구조라고 한다.
이때 연관배열 구조(associative array)란 키(key) 1개와 값(value) 1개가 1:1로 연관되어 있는 자료구조이다.
따라서 키(key)를 이용하여 값(value)을 도출할 수 있다.
이때 검색의 경우 1) 키로 hash를 구한다. 2) hash로 값(value)를 찾는다. 라는 과정을 수행하므로 대부분의 경우 시간복잡도 O(1)을 가지게 된다.



#set
from sys import stdin

N = int(input())
user_card = set(map(int, stdin.readline().split()))
M = int(input())
check_card = list(map(int, stdin.readline().split()))

def solution():
  result = ""
  for i in check_card:
    if i in user_card:
      result += "1 "
    else:
      result += "0 "
  
  return result

print(solution())
-------------------
# 이분탐색

from sys import stdin

N = int(input())
user_card = list(map(int, stdin.readline().split()))
user_card.sort()
user_card.insert(0, 0)
M = int(input())
check_card = list(map(int, stdin.readline().split()))


def binary_search(start, end, num, array):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] < num:
      start = mid + 1
    else:
      end = mid - 1

    if user_card[start] == num:
      return "1 "
  return "0 "
  
result = ""
for n in check_card:
  result += binary_search(1, N-1, n, user_card)

print(result)

------------------
# dictionary

from sys import stdin

N = int(input())
user_card = list(map(int, stdin.readline().split()))
M = int(input())
check_card = list(map(int, stdin.readline().split()))

check_list = {}

for i in user_card:
  check_list[i] = 1

result=""
for i in check_card:
  if i in check_list:
    result += "1 "
  else:
    result += "0 "

print(result)
