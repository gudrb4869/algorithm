# 다이나믹 프로그래밍
def solution(money):
    dp = [0] * len(money)
    dp2 = [0] * len(money)
    dp[0] = money[0]
    for i in range(1, len(money)):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])
    return max(dp[-2], dp2[-1])