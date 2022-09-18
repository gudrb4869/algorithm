def find_head(s):
    for i in range(1, len(s)):
        if s[i].isdigit():
            break
    return s[:i].lower(), i

def find_number(s):
    for i in range(6):
        if i >= len(s) or not s[i].isdigit():
            break
    return int(s[:i])

def solution(files):
    l = []
    for i, file in enumerate(files):
        head, k = find_head(file)
        print(file[k:])
        number = find_number(file[k:])
        l.append((head, number, i, file))
    return [t[3] for t in sorted(l)]