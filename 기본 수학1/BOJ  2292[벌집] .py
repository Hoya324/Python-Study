def bee():
    N = int(input())
    #1 2-7(6) 8-19(12) 20-37(18) 38-61(24) 
    count = 1
    hive = 1
    while N > hive:
        hive += count*6
        count += 1
    if N == 1:
        count =1
    return count

print(bee())
