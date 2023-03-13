# Добро пожаловать.
# В этой ката вы должны, учитывая строку, заменить каждую букву ее позицией в алфавите.
# Если что-то в тексте не является буквой, игнорируйте это и не возвращайте.
# "a" = 1, "b" = 2, и т.д.

# alphabet_position("The sunset sets at twelve o' clock.")
# --> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    if type(text) == str:
        text = text.lower()
        for i in text:
            if i.isalpha() == True:
                result = result + " " + str(alphabet.index(i) + 1)
        return result.strip(" ")

# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# def alphabet_position(text):
#     upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lower_alpha = "abcdefghijklmnopqrstuvwxyz"
#     l = []
#
#     for i in text:
#         if i in upper_alpha:
#             index = upper_alpha.index(i) + 1
#             l.append(str(index))
#         elif i in lower_alpha:
#             index = lower_alpha.index(i) + 1
#             l.append(str(index))
#     return " ".join(l)

import string

def alphabet_position(text):
    return " ".join([str(string.lowercase.index(letter.lower())+1) for letter in list(text) if letter.isalpha()])


print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))