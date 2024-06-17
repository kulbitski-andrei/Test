# Напишите функцию, которая принимает строку и возвращает кол-во заглавных и строчных букв.
# 'The quick Brow Fox' => Upper case characters:
# 3, Lower case characters: 12

def upper_lower(text_string):
    upper_c = 0
    lower_c = 0
    for i in text_string:
        if i.isupper():
            upper_c += 1
        elif i.islower():
            lower_c += 1
    return f"Upper ase characters: {upper_c}, Lower case characters: {lower_c}"


print(upper_lower('The quick Brow Fox'))
print(upper_lower("Hello World!"))




