import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break

    if c * c == a * a + b * b:
        print("right")
    elif b * b == a * a + c * c:
        print("right")
    elif a * a == c * c + b * b:
        print("right")
    else:
        print("wrong")
