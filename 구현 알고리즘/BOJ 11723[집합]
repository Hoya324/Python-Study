from sys import stdin

m = int(input())
s = set()

for _ in range(m):
    cmd = stdin.readline().split()

    if cmd[0] == "add":
        s.add(cmd[1])
    elif cmd[0] == "remove":
        if cmd[1] in s:
            s.remove(cmd[1])
        else:
            pass
    elif cmd[0] == "check":
        if cmd[1] in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if cmd[1] in s:
            s.discard(cmd[1])
        else:
            s.add(cmd[1])
    elif cmd[0] == "all":
        s = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif cmd[0] == "empty":
        s.clear()
