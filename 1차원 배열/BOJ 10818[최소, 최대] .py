import sys
input = sys.stdin.readline
N = int(input())
integer = [int(x) for x in input().split()]
integer.sort()
print(integer[0],integer[-1])
