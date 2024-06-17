# 4. Напишите программу которая умеет добавлять.
# единицу к числу и возращает список. Число хранится в виде списка.
# Например число 123 будет храниться в виде списка: [1, 2, 4].

# [9] => [10]
# [1,2,3] => [1,2,4]
# [1,1,9] => [1,2,0]
# [9,9,9] => [1,0,0,0]

def number_as_list(numbers: list):

    number_as_string = ""
    for i in numbers:
        number_as_string = number_as_string + str(i)
    number_as_string = int(number_as_string) + 1
    new_digit_list = []
    for digit in str(number_as_string):
        new_digit_list.append(digit)
    return new_digit_list


print(number_as_list([9]))
print(number_as_list([1, 2, 3]))
print(number_as_list([1, 1, 9]))
print(number_as_list([9, 9, 9]))
