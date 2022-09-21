def str_to_int(time):
    h,m,s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def int_to_str(i):
    h, mod = divmod(i, 3600)
    m, s = divmod(mod, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)

def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    dp = [0] * (play_time + 1)
    
    for log in logs:
        start, end = log.split('-')
        start, end = str_to_int(start), str_to_int(end)
        dp[start] += 1
        dp[end] -= 1
        
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
        
    max_time = 0
    answer = 0
    for i in range(1, play_time + 1):
        if i >= adv_time:
            if max_time < dp[i] - dp[i - adv_time]:
                max_time = dp[i] - dp[i - adv_time]
                answer = i - adv_time + 1
        else:
            if max_time < dp[i]:
                max_time = dp[i]
    return int_to_str(answer)