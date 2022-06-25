#회의의 수 입력
import sys
N = int(input())

#회의 시간 입력(정렬 전)
schedule_list = []
for i in range(N): 
    start, last = map(int, sys.stdin.readline().split())
    schedule_list.append([start, last])

#회의 시간을 끝나는 시간을 기준으로 정렬
schedule_list.sort(key = lambda x: (x[1], x[0]))
#print(schedule_list)
#가장 먼저 끝나는 회의를 기준으로 그 다음 회의는 먼저한 회의의 끝나는 시간과 같거나 큰 다음 회의로 선정.
#선정된 회의의 끝나는 시간이 다시 기준이 됨
                   
count = 1
last = schedule_list[0][1]
for k in range(1,N):
    if last <= schedule_list[k][0]:
        last = schedule_list[k][1] 
        count += 1
print(count)
