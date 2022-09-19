def solution(n, t, m, timetable):
    timetable = [int(t[:2]) * 60 + int(t[3:]) for t in sorted(timetable)]
    cur = result = 540
    i = 0
    for _ in range(n):
        num = 0
        while i < len(timetable) and num < m:
            time = timetable[i]
            if time > cur:
                break
            i += 1
            num += 1
        if num < m:
            result = cur
        else:
            result = time - 1
        cur += t
    h, m = divmod(result, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)