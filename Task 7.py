# Напишите функцию, преобразующую входную строку в выходную как в примерах,
# Пусть s = "abcdef...xyz", тогда вывод будет таким:
# f(s, 1) => "a"
# f(s, 2) => "aba"
# f(s, 3) => "abcba"
# f(s, 4) => "abcdcba"

def funny_func(long_word, iterations):

    funny_index = 0
    text_to_return = ""

    for i in range(iterations):
        text_to_return += long_word[funny_index]
        funny_index += 1
    funny_index -= 1
    for i in range(iterations - 1):
        text_to_return += long_word[funny_index - 1]
        funny_index -= 1
    return text_to_return


assert funny_func("abcdefghijklmnopqrstuvwxyz", 1) == "a"
assert funny_func("abcdefghijklmnopqrstuvwxyz", 2) == "aba"
assert funny_func("abcdefghijklmnopqrstuvwxyz", 3) == "abcba"
assert funny_func("abcdefghijklmnopqrstuvwxyz", 4) == "abcdcba"