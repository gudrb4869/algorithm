def solution(n, info):
    answer = [-1]
    diff = 0
    min_val = 0
    dic = [0] * 11

    def func(cnt, idx):
        nonlocal answer, diff, min_val
        if cnt == n:
            apache, lion = 0, 0
            for i in range(11):
                if info[i] == 0 and dic[i] == 0:
                    continue
                if dic[i] > 0: temp = i
                if info[i] >= dic[i]:
                    apache += 10 - i
                else:
                    lion += 10 - i
            if lion > apache and diff <= lion - apache:
                if diff == lion - apache and min_val > temp:
                    return
                diff = lion - apache
                min_val = temp
                answer = dic[:]
            return

        for i in range(idx, 11):
            dic[i] = info[i] + 1 if info[i] + 1 < n - cnt else n - cnt
            func(cnt + dic[i], i + 1)
            dic[i] = 0

    func(0, 0)
    return answer