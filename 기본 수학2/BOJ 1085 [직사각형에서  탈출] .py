# 1
.pyfrom sys import stdin

x, y, w, h = map(int, stdin.readline().split())

if w - x > x:
    a = x
else:
    a = w - x

if h - y > y:
    b = y
else:
    b = h - y

if a > b:
    print(b)
else:
    print(a)
    
    
    
# 2
from sys import stdin

x, y, w, h = map(int, stdin.readline().split())
print(min(x,y,w-x,h-y))
