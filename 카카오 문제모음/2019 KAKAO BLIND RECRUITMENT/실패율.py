def solution(N, stages):
    l = [0] * N
    n = len(stages)
    for i in stages:
        if i == N + 1:
            continue
        l[i - 1] += 1
    result = []
    for i, t in enumerate(l):
        result.append((t / n if n else 0, i + 1))
        n -= t
    return [r[1] for r in sorted(result, key=lambda x: -x[0])]