# def trim(phrase, size):
#     if len(phrase) < 3 and size < 3 and len(phrase) < size:
#         return phrase[:size - len(phrase)] + "..."
#     elif size == 1:
#         return phrase[:1] + "..."
#     elif size == 2 and len(phrase) > 2:
#         return phrase[:2] + "..."
#     elif len(phrase) == 3:
#         return phrase
#     elif size == 3 and len(phrase) > 3:
#         return phrase[:3] + "..."
#     # elif len(phrase) == size:
#     #     return phrase
#     elif len(phrase) > size:
#         return phrase[:size - 3] + "..."
# #         return "".join(phrase[:11] + "...")
# #         return phrase.replace("ta is fun", "...")
#     elif len(phrase) <= size:
#         return phrase
#
#
# def trim(phrase, size):
#     return phrase if len(phrase) >= size else phrase[:size if len(phrase) < 4 or size < 4 else (size - 3)] + "..."
#
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
#
# def digital_root(n):
# 	return n%9 or n and 9

# def bool_to_word(boolean):
# #     if boolean == True:
# #         return "Yes"
# #     else:
# #         return "No"
#
#     return "Yes" if boolean == True else "No"
#
#
# print(bool_to_word(True))


# def dna_to_rna(dna):
#     return dna.replace("T", "U")
#     # return n_dna
#
# print(dna_to_rna("GSAT"))

# def positive_sum(arr):
#     pos_sum = 0
#     for i in arr:
#         if i > 0:
#             pos_sum += i
#     return pos_sum
# def positive_sum(arr):
#     L = []
#     for i in arr:
#         if (i > 0):
#             L.append(i)
#     return (sum(L))
#
# print(positive_sum([1,-4,7,12]))

# def greet(name):
#     return f'Hello, {name} how are you doing today?'
#
# greet(input())

# def traffic_lights(road, n):
#     for i in range(len(road)):
#         if i == n:
#             print(road[:n] + "C" + road[n: - 1])
#             print(len(road[:n] + "C" + road[n: - 1]))


# def traffic_lights(road, n):
#     for i in range(len(road)):
#         x = (road[:n * "."] + road[n * ".":])
#         while i == n:
#             print(i)
#
# traffic_lights(21 * ".", 10)

# def time_correct(t):
#     new_t = t.split(':')
#     h = int(new_t[0])
#     m = int(new_t[1])
#     s = int(new_t[2])
#     if h > 23 and m > 59 and s > 59:
#         return f'0{str(h - 24)}:0{str(m - 59)}:00'
#     elif m > 59 and s > 59:
#         return f'{str(h + 1)}:{str(m - 60 +  1)}:0{str(s // 60)}'
#     elif m > 59:
#         return f'0{str(h + 1)}:00:{str(s)}'
#     elif s > 59:
#         return f'0{str(h)}:0{str(m + 1)}:00'
#     else:
#         return t
# #
# #     if t[-2:] == 'AM' and t[:2] == '12':
# #         return '00' + t[2:-2]
# #     elif t[-2:] == 'AM':
# #         return t[:-2]
# #     elif t[-2:] == 'PM' and t[:2] == '12':
# #         return t[:-2]
# #     elif int(t[:-2]) > 60:
# #         return '00'
# #     else:
# #         return str(int(t[:2]) + 12) + t[2:8]
# #
# #
# print(time_correct('09:10:2400'))

# def setTime(string):
#     hour_minute_sec = string.split(':')
#     hour, minute, second = hour_minute_sec
#     if second[0] == '0':
#         second = int(second[1])
#         else:
#         second = int(second)    if minute[0] == '0':
#             minute = int(minute[1])
#             else:
#             minute = int(minute)    if hour[0] == '0':
#                 hour = int(hour[1])
#                 else:
#                 hour = int(hour)
#                 while True:
#                     if second > 59:
#                         second -= 60
#                         minute += 1
#                         else:
#                         break
#                         while True:
#                             if minute > 59:
#                                 minute -= 60
#                                 hour += 1
#                                 else:
#                                 break
#                                 while True:
#                                     if hour > 23:
#                                         hour -= 24
#                                         else:
#                                         break
#                                         result = ''
#                                         if hour < 10:
#                                             result += f'0{hour}:'
#                                             else:
#                                             result += f'{hour}:'
#                                             if minute < 10:
#                                                 result += f'0{minute}:'
#                                                 else:
#                                                 result += f'{minute}:'
#                                                 if second < 10:
#                                                     result += f'0{second}'
#                                                     else:
#                                                     result += f'{second}'
#                                                     return result# print(setTime("19:99:99"))


# def time_correct(t):
#     if not t: return t
#     try:
#         h, m, s = map(int, t.split(':'))
#         if s >= 60: s -= 60; m += 1
#         if m >= 60: m -= 60; h += 1
#         return '%02d:%02d:%02d' % (h % 24, m, s)
#     except: pass

# import re
#
#
# def time_correct(t):
#     if not t:
#         return t
#
#     if not re.match("\d\d:\d\d:\d\d$", t):
#         return None
#
#     hours, minutes, seconds = [int(x) for x in t.split(':')]
#
#     if seconds >= 60:
#         minutes += 1
#         seconds -= 60
#     if minutes >= 60:
#         hours += 1
#         minutes -= 60
#     if hours >= 24:
#         hours = hours % 24
#
#     return "{0:0>2}:{1:0>2}:{2:0>2}".format(hours, minutes, seconds)

# def time_correct(t):
#     if not t: return t
#     try:
#         h, m, s = map(int, t.split(':'))
#         return '%02d:%02d:%02d' %((h + (m + s//60)//60) % 24, (m + s//60) % 60, s % 60)
#     except: return None

# def time_correct(t):
#     try : h, m, s = [int(e) for e in t.split(':')]
#     except : return '' if t=='' else None #
#     if len(t)!=8 or any(c not in '0123456789:' for c in t): return None
#     m += s//60
#     s = s%60
#     h += m//60
#     m = m%60
#     h = h%24
#     return f'{h:02d}:{m:02d}:{s:02d}'

# ???? ???????????? ???????????????? ??????????????, ?????????????? ???????????????? ?? ???????????????????? ?????????????????? ?????????????? ???? ???????????? ??????????????????.
# ?????? ?????????????????????????????? ???????????? (?????? ????????????) ?????????????????????????? ??????. ???????????????? ???????????? ???????? ???????????????????????? ???????????????????? ??????????,
# ?????????????????? ?? ?????????????? (???????????? ??????????????), ?? ???????????????????? ??????????, ?????????????????? ???? ???????????????? (???????????? ??????????????) ???? ???????????????????? ??????????????????.
# ???????? ???????????? ??? ?????????????? ???????????????????? ??????????, ?????????????? ?????? ?????????????????? ?? ???????????????? ?????????? ?????????????????? ???????????????????? ??????????????????
# (?????????? ???????????????????? ??????????????). ???????????????? ???? ????, ?????? ?????? ?????????????????? ???????????????????? ??????????????????, ?????????????? ?????????? ???????? ???? ????????????,
# ?? ?????????????????? ???????? ?????? ?????? ?????????? ???????? ???????????? ????????????????, ??????, ????????????????, ???????? ?????? :D
# ?????????????????? ???? ????????-??????????.
# ???????????? ?? ????????, ?????? ???????????????? ?????????????? ??????????????????????, ?????? ???????????????????? ?????????? ?? ???????????????? ???????????? >= 0.
# ?????????? ??????????????, ???????????????????????? ?????????? ?????????? ???? ?????????? ???????? ??????????????????????????.
# ???????????? ???????????????? ?? ???????????? ???????? ?????????????? ?????????? 0, ?????? ?????? ???? ???????????? ?????????????????? ?????????????? ????????????.

# def number(bus_stops):
#     res = 0
#     for i, element in bus_stops:
#         res += i - element
#     print(int(res))
#
#
# number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])
#
# def number(bus_stops):
#     return sum(on - off for on, off in bus_stops)
#
# def number(bus_stops):
#     sum=0
#     for i in bus_stops:
#         sum+=i[0]-i[1]
#     return sum


# ???? ???????????? ?????????????? ???????????????? ???????????????? ?????? ??????????????. ?????? ???????????? ???????? ?????????????? ?????????????? ???????????? ???????????????????????? ??????????,
# ?????????????? ?????? ???????????????? ?????????????? ?????????????? ???? a to m.
# ??????????, ???????????????????????? ??????????????????, ???????????????????????? ?? ?????????????????????? ????????????. ????????????????,
# "??????????????" ?????????????????????? ???????????? ?????????? aaabbbbhaijjjm????????????????, ?????? ?????????????? ?????????????????????? ?????? ???????? ???????? a, ???????????? ???????? ???????? b,
# ???????? ?????? ???????? h, ?? ?????????? ???????? ?????? ???????? a...
# ???????????? ?????????????????? ????????????????: ???????????????????? ????????????, ?????????????????????? ???????? ?? ???????????????? "????????????" ?????????????????????? ????????????,
# ????????????????, aaaxbbbbyyhwawiwjjjwwm?? ?????????????? ???? ???? a to m.
# ???? ???????????? ???????????????? ?????????????? printer_error, ?????????????? ???? ???????????????? ???????????? ?????????? ???????????????????? ?????????????? ???????????? ???????????????? ?? ???????? ????????????,
# ???????????????????????????? ???????????????????????? ??????????, ?????????????????? ???????????????? ??? ???????????????????? ????????????, ?? ?????????????????????? ??? ?????????? ?????????????????????? ????????????.
# ???? ???????????????????? ?????? ?????????? ???? ?????????? ???????????????? ??????????????????.
# ???????????? ?????????? ?????????? ???????????? ?????? ???????????? ?????????????? ?? ???????????????? ???????????? ?????????? ???? a???? z.
# ??????????????:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"
# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

# def printer_error(s):
#
#     errors = 0
#     colors = 'abcdefghijklm'
#     color = 0
#     for i in colors:
#         for j in s:
#             if i == j:
#                 color += 1
#                 if i != j:
#                     errors += 1
#     return f'{len(s) - color}/{len(s)}'
#
#
# from re import sub
# def printer_error(s):
#     return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
#
# def printer_error(s):
#     return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
#
# def printer_error(s):
#     errors = 0
#     count = len(s)
#     for i in s:
#         if i > "m":
#             errors += 1
#     return str(errors) + "/" + str(count)
#
# def printer_error(s):
#     good_colors = "abcdefghijklm"
#     counter = 0
#     for i in s:
#         if i not in good_colors:
#             counter += 1
#     return str(counter) + "/" + str(len(s))
#
#
# printer_error('aaaxbbbbyyhwawiwjjjwwm')


# ???????? ???????????? ??? ?????????????? ??????????????, ?????????????? ?????????????????? ???????????? ???????????????? ???????????????????????????? ????????????????.
# ?????????????? ???????????? ?????????????????? ?????? ?????????????????? - ????????????????(????????????/????????????), ????????????????1(??????????), ????????????????2(??????????).
# ?????????????? ???????????? ???????????????????? ???????????????? ?????????????????? ?????????? ???????????????????? ?????????????????? ????????????????.
# ??????????????(????????????????, ????????????????1, ????????????????2) --> ??????????
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

# def basic_op(operator, value1, value2):
#     if operator == '+':
#         return value1 + value2
#     if operator == '-':
#         return value1 + value2
#     if operator == '*':
#         return value1 * value2
#     if operator == '/':
#         return value1 / value2
#
# def basic_op(operator, value1, value2):
#     return eval("{}{}{}".format(value1, operator, value2))
#
# def basic_op(operator, value1, value2):
#     return eval(f'{value1}{operator}{value2}')
#
#
# basic_op('+', 4, 7)

# def get_sum(a, b):
#     sum = 0
#     if a == 1 and b == 1:
#         return f'1 since both are same'
#     elif a < b:
#         for i in range(a, b + 1):
#             sum += i
#         print(sum)
#     elif a > b:
#         return a + b
#     else:
#         return a + b
# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))
#
# get_sum(-1, 4)

# def get_sum(a,b):
#     soma=0
#     if a==b:
#         return a
#     elif a > b:
#         for i in range(b,a+1):
#             soma += i
#         return soma
#     else:
#         for i in range(a,b+1):
#             soma += i
#         return soma
#
# def get_sum(a,b):
#     if a>b : a,b = b,a
#     return sum(range(a,b+1))

# ???????????????? ??????????????, ?????????????? ??????????????????, ?????????????? ???? ?????????? ???? ?????? ?????????? x AND y.
# ?????? ?????????????? ???????????? ???????????????? ????????????????????????????, ???????????????????? ??????????????.
#
# Examples:
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7

# def is_divisible(n, x, y):
#     if n % x == 0 and n % y == 0:
#         print(True)
#     else:
#         print(False)
#
# is_divisible(4, 2, 3)

# def is_divisible(n,x,y):
#     print(n % x == 0 and n % y == 0)
#
# is_divisible(4, 2, 2)

# ???????????????? ??????????????, ???????????????????? shortcut?????? ???????????????? ???????????????? ?????????????? ( a, e, i, o, u) ?? ???????????????? ????????????.
#
# ??????????????
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"

# def shortcut(s):
#     string = ''
#     glas = 'aeiouy'
#     for i in range(len(s)):
#         if s[i] not in glas:
#             string += s[i]
#     print(string)
#
#
#
# shortcut('hello')

# def encode(message, key):
#     list_alfa = []
#     list_key = []
#     alfs = 'abcdefghijklmnopqrstuvwxyz'
#     nums = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
#     alfs_nums = dict(zip(alfs, nums))
#     for i in range(len(message)):
#         for key1, value in alfs_nums.items():
#             if key == message[i]:
#                 list_alfa.append(value)
#     for j in range(1, key + 1):
#         list_key.append(key)
#         print(list_key + list_alfa)
#
#
# encode('aaaa', 1001)

# def get_sum_of_digits(num):
#     sum = 0
#     digits = str(num)
#     for x in range(len(digits)):
#         sum += int(digits[x])
#     print(sum)
#
# get_sum_of_digits(123)

# def get_sum_of_digits(num):
#     return sum(map(int, str(num)))

# def GetSumStr(a, b):
#     if a == '':
#         sum_a = 0
#         return sum_a + int(b)
#     elif b == '':
#         sum_b = 0
#         return sum_b + int(a)
#     else:
#         a = int(a)
#         b = int(b)
#         return str(int(a) + int(b))
# print(GetSumStr('34',''))

# def sum_str(a, b):
#     sum = 0
#     number1 = int(a)
#     number2 = int(b)
#     sum += int(number1 + number2)
#     return str(sum)

# class Warrior:
#     def __init__(self,n ame):
#         self.name = name
#         self.health = 100
#
#     def strike(self, swings, health):
#         self.health = health
#         try:
#             assert health > 0
#         except:
#             health = 0
#         else:
#            health = max([-1,self.health-(swings*10)])
#
# Warrior = ['Hattori Hanzo','Sasuke Sarutobi','Jubei Kibagami','Kotaro Fuma']
# print(Warrior.health)