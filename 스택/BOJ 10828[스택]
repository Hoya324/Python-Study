import sys
T = int(sys.stdin.readline())
stack= []

for _ in range(T):
    data = sys.stdin.readline().split()
    #입력어가 push일 경우
    if data[0] == 'push' :
        stack.append(data[1])
       # print(stack)
    #입력어가 pop일 경우    
    elif data[0] == 'pop':
        #print(stack)
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    #입력어가 size일 경우
    elif data[0] == 'size':
        print(len(stack))
    #입력어가 empty일 경우
    elif data[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    #입력어가 top일 경우
    elif data[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
