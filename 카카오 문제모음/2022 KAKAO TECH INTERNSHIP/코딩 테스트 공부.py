def solution(alp, cop, problems):
    INF = 10**9
    max_alp, max_cop = 0, 0
    for a, c, _, _, _ in problems:
        max_alp, max_cop = max(max_alp, a), max(max_cop, c)
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1 if i > alp else INF, dp[i][j - 1] + 1 if j > cop else INF)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(i + alp_rwd, max_alp), min(j + cop_rwd, max_cop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    return dp[-1][-1]