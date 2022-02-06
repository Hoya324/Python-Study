#N이 1이 될 때까지 1을 빼거나 K로 나눌 때 가장 적은 수로 1을 만든 횟수를 출력한다.

N, K = map(int, input().split())
count = 0

while True:
    target = (N//K)*K 
    count += (N-target)
    N = target
    if N < K:
        break 
    
    count += 1
    N //= K

#남은 수 1씩 빼기
count += (N-1)
    
print(count)
