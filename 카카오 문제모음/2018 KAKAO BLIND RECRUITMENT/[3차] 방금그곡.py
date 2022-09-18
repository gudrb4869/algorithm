def convert(s):
    stack = []
    for c in s:
        if c == '#':
            stack.append(stack.pop().lower())
        else:
            stack.append(c)
    return ''.join(stack)

def solution(m, musicinfos):
    result = []
    m = convert(m)
    for i in range(len(musicinfos)):
        start, end, title, info = musicinfos[i].split(',')
        info = convert(info)
        start = int(start[:2]) * 60 + int(start[3:])
        end = int(end[:2]) * 60 + int(end[3:])
        time = end - start
        div, mod = divmod(time, len(info))
        melody = info * div + info[:mod]
        if m in melody:
            result.append([time, i, title])
    result.sort(key=lambda x: (-x[0], x[1]))
    return result[0][2] if result else '(None)'