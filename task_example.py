# The code provided is supposed return a person's Full Name given their first and last names.
#
# But it's not working properly.
#
# Notes
# The first and/or last names are never null, but may be empty.
#
# Task
# Fix the bug so we can all go home early.
# https://www.codewars.com/kata/52f3eeb274c7e693a600288e/train/python

# def insert_at_indexes(phrase, word, indexes):
#     counter = 0
#     for i in indexes:
#         phrase = phrase[:i+counter] + word + phrase[i+counter:]
#         counter += len(word)
#     return phrase


def insert_at_indexes(phrase, word, indexes):
    for i in indexes[::-1]:
        phrase = phrase[:i] + word + phrase[i:]
    return phrase


print(insert_at_indexes("I like codewars! It makes me happy.", " really", [1, 28]))
print(insert_at_indexes('I really like codewars! It makes me really happy.', "'d", [1, 26]))
print(insert_at_indexes("'I' write a wi said Phi", "ll", [3, 14, 24]))

# "I like codewars! It makes me happy."," really",[1, 28] -->  "I really like codewars! It makes me really happy."
# "I really like codewars! It makes me really happy.","'d",[1, 26] --> "I'd really like codewars! It'd makes me really happy."
# "'I' write a wi said Phi", "ll", [3, 14, 24]), --> "'I'll write a will said Phill"


