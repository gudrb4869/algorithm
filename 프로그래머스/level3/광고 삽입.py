def strToInt(time):
    h,m,s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def intToStr(time):
    h, time = divmod(time, 3600)
    m, s = divmod(time, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)

def solution(play_time, adv_time, logs):
    play_time = strToInt(play_time)
    adv_time = strToInt(adv_time)
    dp = [0] * (play_time + 1)
    
    for log in logs:
        start, end = log.split('-')
        start, end = strToInt(start), strToInt(end)
        dp[start] += 1
        dp[end] -= 1
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
    for i in range(1, play_time + 1):
        dp[i] += dp[i - 1]
    answer = 0
    most_view = dp[adv_time]
    for start in range(1, play_time):
        end = play_time if start + adv_time >= play_time else start + adv_time
        if most_view < dp[end] - dp[start]:
            most_view = dp[end] - dp[start]
            answer = start + 1
        
    return intToStr(answer)