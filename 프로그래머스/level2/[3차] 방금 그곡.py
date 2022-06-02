import re, heapq

def solution(m, musicinfos):
    heap = []
    m = re.sub('(C|D|F|G|A)#', lambda x : x.group(1).lower(), m)

    for musicinfo in musicinfos:
        start,end,title,melody = musicinfo.split(',')
        time = (int(end[:2]) * 60 + int(end[3:])) - (int(start[:2]) * 60 + int(start[3:]))
        melody = re.sub('(C|D|F|G|A)#', lambda x : x.group(1).lower(), melody)
        div, mod = divmod(time, len(melody))
        result = melody * div + melody[:mod]

        if m in result:
            heapq.heappush(heap, (-time, title))

    return '(None)' if not heap else heap[0][1]