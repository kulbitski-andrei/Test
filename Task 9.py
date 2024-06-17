# Реализуйте игру "Крестики-нолики" для двух игроков.
# Программа должна позволять игрокам сделать свои ходы,
# проверять правильность хода и определять победителя.

# Сделал что успел

victory = False
player_1 = True
line_1 = [".", ".", "."]
line_2 = [".", ".", "."]
line_3 = [".", ".", "."]

while not victory:

    if player_1 == True:
        print("Ход первого игрока (крестики)")
    else:
        print("Ход второго игрока (нолики)")

    print(line_1)
    print(line_2)
    print(line_3)
    current_line = None

    print("Выберите РЯД куда Вы хотите поставить крестик-нолик в формате: {1-3}")

    position_1 = int(input())

    print("Выберите СТОЛБЕЦ куда Вы хотите поставить крестик-нолик в формате: {1-3}")

    # position_2 = int(input())
    position_2 = int(input()) - 1

    if position_1 == 1:
        current_line = line_1
    if position_1 == 2:
        current_line = line_2
    if position_1 == 3:
        current_line = line_3

    print(current_line[position_2])
    if current_line[position_2] == "." and player_1 == True:
        current_line[position_2] = "X"
    if current_line[position_2] == "." and player_1 == False:
        current_line[position_2] = "O"
    else:
        print("Неправильный ввод! Повторите")
        continue

    print("Ход сделан:")

    print(line_1)
    print(line_2)
    print(line_3)



    player_1 = False
    break