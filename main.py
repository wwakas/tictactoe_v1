a = '         '
temp_list = list(a)  # temp list to change values in string a
blank = ' '
character = 'X'

print(f"---------\n| {a[0]} {a[1]} {a[2]} |\n| {a[3]} {a[4]} {a[5]} |\n| {a[6]} {a[7]} {a[8]} |\n---------")

# iterating till list has an empty places
while blank in a:
    numbers = ['1', '2', '3']
    move = input('Enter the coordinates: ')
    temp_a = ""

    if len(move.split(' ')) == 2:  # condition that verify if user passed two coordinates
        x, y = move.split(' ')

        if x in numbers or y in numbers:  # check if coordinates are in range 1 - 3

            if 1 <= int(x) <= 3 and 1 <= int(y) <= 3:

                # block that checking input and replace proper list elements
                if (move == "1 1" and a[0] == blank) or (move == "1 2" and a[1] == blank) or \
                        (move == "1 3" and a[2] == blank) or (move == "2 1" and a[3] == blank) or \
                        (move == "2 2" and a[4] == blank) or (move == "2 3" and a[5] == blank) or \
                        (move == "3 1" and a[6] == blank) or (move == "3 2" and a[7] == blank) or \
                        (move == "3 3" and a[8] == blank):

                    if move == "1 1":
                        temp_list[0] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "1 2":
                        temp_list[1] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "1 3":
                        temp_list[2] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "2 1":
                        temp_list[3] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "2 2":
                        temp_list[4] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "2 3":
                        temp_list[5] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "3 1":
                        temp_list[6] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "3 2":
                        temp_list[7] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                    elif move == "3 3":
                        temp_list[8] = character
                        for k in temp_list:
                            temp_a += k
                            a = temp_a

                else:
                    print('This cell is occupied! Choose another one!')
                    continue

            else:
                print('Coordinates should be from 1 to 3!')
                continue

        else:
            print('You should enter numbers!')
            continue

    else:
        print('You should enter numbers!')
        continue

    print(f"---------\n| {a[0]} {a[1]} {a[2]} |\n| {a[3]} {a[4]} {a[5]} |\n| {a[6]} {a[7]} {a[8]} |\n---------")

    # win conditions
    wc1 = (a[0] == a[1] == a[2] and blank not in (a[0], a[1], a[2])) or (a[0] == a[3] == a[6] and blank not in
                                                                         (a[0], a[3], a[6])) or \
          (a[0] == a[4] == a[8] and blank not in (a[0], a[4], a[8]))
    wc2 = (a[3] == a[4] == a[5] and blank not in (a[3], a[4], a[5])) or (a[1] == a[4] == a[7] and blank not in
                                                                         (a[1], a[4], a[7])) or \
          (a[2] == a[4] == a[6] and blank not in (a[2], a[4], a[6]))
    wc3 = (a[6] == a[7] == a[8] and blank not in (a[6], a[7], a[8])) or (a[2] == a[5] == a[8] and blank not in
                                                                         (a[2], a[5], a[8]))

    if wc1 and wc2 or wc1 and wc3 or wc2 and wc3:
        print("Impossible")
        break
    elif wc1:
        print(a[0], "wins")
        break
    elif wc2:
        print(a[4], "wins")
        break
    elif wc3:
        print(a[8], "wins")
        break
    elif blank not in a:
        print("Draw")
        break

    if character == 'X':
        character = 'O'
    elif character == 'O':
        character = 'X'