#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
#단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징이다.

import sys
N, M, K = list(map(int, sys.stdin.readline().split())) #N은 배열의 크기
data = [int(x) for x in input().split()]
data.sort() #주어진 배열을 정렬한다.
result = 0
count = 0
first = data[-1]
second = data[-2]
#가장 큰 수가 더해진 값
count = int(M//(K+1))*K
count += M%(K+1)
result = count*first
result += (M-count)*second

print(result)
