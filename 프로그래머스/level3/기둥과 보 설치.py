def impossible(result):
    for x, y, a in result:
        if a == 0:
            if not (y == 0 or (x, y - 1, 0) in result or (x - 1, y, 1) in result or (x, y, 1) in result):
                return True
        else:
            if not ((x, y - 1, 0) in result or (x + 1, y - 1, 0) in result or ((x - 1, y, 1) in result and (x + 1, y, 1) in result)):
                return True
    return False

def solution(n, build_frame):
    result = set()

    for *items, b in build_frame:
        items = tuple(items)
        if b:
            result.add(items)
            if impossible(result):
                result.remove(items)
        else:
            result.remove(items)
            if impossible(result):
                result.add(items)
                
    return sorted(list(result))