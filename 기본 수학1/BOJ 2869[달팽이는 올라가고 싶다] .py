#낮에 A만큼 올라가고, 밤에 B만큼 미끄러진다
#정상에 도착 후 미끄러지지 않는다.
#정상에 도달하려면 며칠이 걸리는지 구한다.
#V는 막대의 길이
import sys
A, B, V = map(int, sys.stdin.readline().split())
day = (V-B)/(A-B)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)
