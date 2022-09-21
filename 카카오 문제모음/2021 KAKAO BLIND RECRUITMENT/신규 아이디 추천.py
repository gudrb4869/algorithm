import re

def solution(new_id):
    new_id = re.sub('[^0-9a-z-_.]', '', new_id.lower())
    new_id = re.sub('[.]{2,}', '.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id