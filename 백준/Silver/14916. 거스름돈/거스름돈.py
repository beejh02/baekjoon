n = int(input())

dp = [-1] * (n+6)
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    if(dp[i-2] != -1):
        dp[i] = dp[i-2] + 1


    if(dp[i-5] != -1):
        if(dp[i] == -1 or dp[i] > dp[i-5] + 1):
            dp[i] = dp[i-5] + 1

print(dp[n])