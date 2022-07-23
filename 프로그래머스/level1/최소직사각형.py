def solution(sizes):
    sizes = [[w, h] if w > h else [h, w] for w, h in sizes]
    return max(s[0] for s in sizes) * max(s[1] for s in sizes)