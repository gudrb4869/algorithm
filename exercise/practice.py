fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(*fruits)

def f(*params):
    print(params)

f('a', 'b', 'c')

a, *b = [1,2,3,4]
print(a)
print(b)
*a, b = [1,2,3,4]
print(a)
print(b)

date_info = {'year': '2020', 'month': '01', 'day': '7'}
new_info = {**date_info, 'day': "14"}
print(new_info)