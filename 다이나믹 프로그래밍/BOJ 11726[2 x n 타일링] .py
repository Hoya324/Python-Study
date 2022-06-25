# 1

n = int(input())

dp = [0] * (n+1)


if n > 2:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

else:
    dp[n] = n

        
print(dp[n]%10007)

# 2

count = n-1
if n == 2:
    count *= 2
else:
    for i in range(2, n//2+1):
        u = 1
        d = 1
        t = n - i
        if i < (n + i)//2:
            for j in range(i):
                u *= t - j
            for j in range(1, i + 1):
                d *= j
        else:
            for j in range(t - i):
                u *= t - j
            for j in range(1, t - i + 1):
                d *= j
        count += u // d
    count += 1

print(count % 10007)
