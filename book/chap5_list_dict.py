# a = list()
# a = []
# a = [1, 2, 3]
# print(a)
# a.append(4)
# print(a)
# a.insert(3, 5)
# print(a)
# a.append('안녕')
# a.append(True)
# print(a)
# print(a[3])
# print(a[1:3])
# print(a[:3])
# print(a[4:])
# print(a[1:4])
# print(a[1:4:2])
# try:
#     print(a[9])
# except IndexError:
#     print('존재하지 않는 인덱스')
# del a[1]
# print(a)
# a.remove(3)
# print(a)
# a.pop(3)
# print(a)

# a = dict()
# a = {}
# a = {'key1':'value1', 'key2':'value2'}
# print(a)
# a['key3'] = 'value3'
# print(a)
# print(a['key1'])
# try:
#     print(a['key4'])
# except KeyError:
#     print('존재하지 않는 키')

# if 'key4' in a:
#     print('존재하는 키')
# else:
#     print('존재하지 않는 키')

# for k,v in a.items():
#     print(k,v)

# del a['key1']
# print(a)

import collections

# a = collections.defaultdict(int)
# a['A'] = 5
# a['B'] = 4
# print(a)
# a['C'] += 1
# print(a)

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b)
print(type(b))
print(b.most_common(2))