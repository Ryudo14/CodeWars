# Дана строка и массив целых чисел, представляющих индексы, сделать все буквы в этих индексах заглавными.
# Например:
# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF". Индекса 100 нет.
# Входными данными будет строчная строка без пробелов и массив цифр.
# Удачи!
# Обязательно попробуйте также:
def capitalize(s, ind):
    new_string = ''
    for i, element in enumerate(s):
        if i in ind:
            new_string += element.capitalize()
        else:
            new_string += element
    print(new_string)

    return ''.join(c.upper() if i in ind else c for i, c in enumerate(s))



capitalize("abcdef", [1, 2, 5])