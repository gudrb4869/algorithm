def solution(survey, choices):
    answer = list('RCJA')
    p = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for s, c in zip(survey, choices):
        if c > 4:
            p[s[1]] += c - 4
        else:
            p[s[0]] += 4 - c
    if p['R'] < p['T']:
        answer[0] = 'T'
    if p['C'] < p['F']:
        answer[1] = 'F'
    if p['J'] < p['M']:
        answer[2] = 'M'
    if p['A'] < p['N']:
        answer[3] = 'N'
    return ''.join(answer)