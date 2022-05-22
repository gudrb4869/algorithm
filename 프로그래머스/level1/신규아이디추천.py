import re

def solution(new_id):
    p = new_id.lower()
    p = re.sub('[^a-z0-9\-_.]', '', p)
    p = re.sub('\.+', '.', p)
    p = re.sub('^[.]|[.]$', '', p)
    p = 'a' if len(p) == 0 else p[:15]
    p = re.sub('^[.]|[.]$', '', p)
    p = p if len(p) > 2 else p + ''.join(p[-1] for i in range(3 - len(p)))
    
    return p