# Возвращает функцию, которая обрезает строку (первый заданный аргумент),
# если она длиннее максимальной длины строки (второй заданный аргумент). Результат также должен заканчиваться на "..."
# Эти точки в конце также увеличивают длину строки.
# Итак, в приведенном выше примере trim("Creating kata is fun", 14)должно вернуться"Creating ka..."
# Если строка меньше или равна 3 символам, то длина точек не добавляется к длине строки.
# например trim("He", 1), должен вернуться"H..."
# Если строка меньше или равна максимальной длине строки, просто верните строку без обрезки или точек.
# например trim("Code Wars is pretty rad", 50), должен вернуться"Code Wars is pretty rad"

# https://www.codewars.com/kata/563fb342f47611dae800003c/train/python


def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'

# Завершите метод/функцию, чтобы она преобразовывала слова, разделенные тире/подчеркиванием, в верблюжий регистр.
# Первое слово в выводе должно быть написано с заглавной буквы только в том случае, если исходное слово было написано
# с заглавной буквы (известный как верхний верблюжий регистр, также часто называемый регистром Паскаля).
# Следующие слова всегда должны быть написаны с большой буквы.
#
# Примеры
# "the-stealth-warrior"превращается в "theStealthWarrior"
# "The_Stealth_Warrior"превращается в"TheStealthWarrior"

# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    final_i = []
    if "-" in text:
        text_n = text.replace("-", ",")
        text_n = text_n.split(",")
        for i in text_n:
            i = i.strip()
            text_n = i.capitalize()
            final_i.append(text_n)
    elif "_" in text:
        text_n = text.replace("_", ",")
        text_n = text_n.split(",")
        for i in text_n:
            i = i.strip()
            text_n = i.capitalize()
            final_i.append(text_n)
    final_text = "".join(final_i)
    if text[:1].isupper():
        return final_text[:1].upper() + final_text[1:]
    elif text[:1].islower():
        return final_text[:1].lower() + final_text[1:]
    else:
        return final_text

# Задача на Codewars написана не корректно. Помимо того, что указано в test, в проверке есть тесты со смежными символами
# подчеркивания и тире. Думаю, что можно решить все тесты с помощью словаря, но у меня не получилось.


# Цифровой корень — это рекурсивная сумма всех цифр числа.
# Учитывая n, возьмите сумму цифр n. Если это значение имеет более одной цифры, продолжайте уменьшать таким образом,
# пока не будет получено однозначное число. Ввод будет неотрицательным целым числом.
# Примеры
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python


def digital_root(n):
    s = str(n)
    while len(s) > 1:
        n = 0
        for i in s:
            n += int(i)
        s = str(n)
    return int(s)


