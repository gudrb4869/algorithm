# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result

# # a = FourCal()
# # b = FourCal()
# # a.setdata(4,2)
# # b.setdata(3,8)
# # print(a.add())
# a = FourCal(4, 2)
# print(a.first)
# print(a.second)

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second

# a = SafeFourCal(4, 0)
# a.div()

# class Family:
#     lastname = "김"

# print(Family.lastname)

# a = Family()
# b = Family()
# id(Family.lastname)
# id(a.lastname)
# id(b.lastname)
# Family.lastname = "박"
# print(a.lastname)
# print(b.lastname)

# import mod1
# print(mod1.add(3,4))
# print(mod1.sub(4,2))

# from mod1 import *
# print(add(3, 4))
# print(sub(4,2))

# import mod2
# print(mod2.PI)
# a = mod2.Math()
# print(a.solv(2))

# print(mod2.add(mod2.PI, 4.4))

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# try:
#     age=int(input('나이를 입력하세요: '))
# except:
#     print("입력이 정확하지 않습니다.")
# else:
#     if age <= 18:
#         print('미성년자는 출입금지입니다.')
#     else:
#         print('환영합니다.')
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagle = Eagle()
# eagle.fly()

# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않는 별명입니다."

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)
# try:
#     say_nick('천사')
#     say_nick('바보')
# except MyError as e:
#     print(e)

# a = [1,2,3,4,5]
# del a[0]
# print(a)
# a.remove(1)
# print(a)

# print(all([0]))

# import pickle
# f = open("test.txt", 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()

# import pickle
# f = open("test.txt", 'rb')
# data = pickle.load(f)
# print(data)

# import os
# print(os.environ)

# import time
# print(time.asctime(time.localtime(time.time())))
# print(time.ctime())
# print(time.strftime('%x', time.localtime(time.time())))
# print(time.strftime('%c', time.localtime(time.time())))

# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)

# import calendar
# print(calendar.calendar(2022))
# calendar.prcal(2022)
# print(calendar.prmonth(2022, 1))
# print(calendar.weekday(2022, 1, 16))
# print(calendar.monthrange(2022, 1))

# import random
# def random_pop(data):
#     number = random.randint(0, len(data)-1)
#     return data.pop(number)

# if __name__ == "__main__":
#     data = [1, 2, 3, 4, 5]
#     while data:
#         print(random_pop(data))
# import random
# def random_pop(data):
#     number = random.choice(data)
#     data.remove(number)
#     return number

# import random
# data = [1,2,3,4,5]
# random.shuffle(data)
# print(data)
# import webbrowser
# webbrowser.open("http://google.com")
# webbrowser.open_new("http://google.com")