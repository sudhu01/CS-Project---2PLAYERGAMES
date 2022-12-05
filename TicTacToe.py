print("Welcome to the Tic Tac Toe Game! ")
print('*'*100,'\n','RULES:','\n','The game is to be played by two players','\n','Each player moves in alternate turns','\n','First one to reach three in a row horizontally, vertically or diagonally is the winner')
print('*'*100)
def welcome():
    turn = ''
    while turn != 'X' or turn != 'O':
        turn = input("Player1 do you want to be X or O: ")
        if turn == 'X':
            return {'Player1': 'X', 'Player2': 'O'}
        elif turn == 'O':
            return {'Player1': 'O', 'Player2': 'X'}
        else:
            print('Enter a valid value')
sign = welcome()
def whole():
    board1 = '[1,2,3]'
    board2 = '[4,5,6]'
    board3 = '[7,8,9]'
    print(board1,board2,board3, sep='\n')

    def cmds():
        new = ()
        counter = 1
        x = board1
        y = board2
        z = board3
        while counter <= 10:
            p = input("Enter the position: ")
            if p.isdigit():
                p = int(p)
                if p in range(1, 10) and p not in new:
                    new += (p,)
                    if p == 1:
                        if counter % 2 != 0:
                            if counter == 1:
                                x = board1.replace(board1[1], sign['Player1'], 1)
                            else:
                                x = x.replace(board1[1], sign['Player1'], 1)
                        else:
                            x = x.replace(board1[1], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 2:
                        if counter % 2 != 0:
                            if counter == 1:
                                x = board1.replace(board1[3], sign['Player1'], 1)
                            else:
                                x = x.replace(board1[3], sign['Player1'], 1)
                        else:
                            x = x.replace(board1[3], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 3:
                        if counter % 2 != 0:
                            if counter == 1:
                                x = board1.replace(board1[5], sign['Player1'], 1)
                            else:
                                x = x.replace(board1[5], sign['Player1'], 1)
                        else:
                            x = x.replace(board1[5], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 4:
                        if counter % 2 != 0:
                            if counter == 1:
                                y = board2.replace(board2[1], sign['Player1'], 1)
                            else:
                                y = y.replace(board2[1], sign['Player1'], 1)
                        else:
                            y = y.replace(board2[1], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 5:
                        if counter % 2 != 0:
                            if counter == 1:
                                y = board2.replace(board2[3], sign['Player1'], 1)
                            else:
                                y = y.replace(board2[3], sign['Player1'], 1)
                        else:
                            y = y.replace(board2[3], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 6:
                        if counter % 2 != 0:
                            if counter == 1:
                                y = board2.replace(board2[5], sign['Player1'], 1)
                            else:
                                y = y.replace(board2[5], sign['Player1'], 1)
                        else:
                            y = y.replace(board2[5], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 7:
                        if counter % 2 != 0:
                            if counter == 1:
                                z = board3.replace(board3[1], sign['Player1'], 1)
                            else:
                                z = z.replace(board3[1], sign['Player1'], 1)
                        else:
                            z = z.replace(board3[1], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 8:
                        if counter % 2 != 0:
                            if counter == 1:
                                z = board3.replace(board3[3], sign['Player1'], 1)
                            else:
                                z = z.replace(board3[3], sign['Player1'], 1)
                        else:
                            z = z.replace(board3[3], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    elif p == 9:
                        if counter % 2 != 0:
                            if counter == 1:
                                z = board3.replace(board3[5], sign['Player1'], 1)
                            else:
                                z = z.replace(board3[5], sign['Player1'], 1)
                        else:
                            z = z.replace(board3[5], sign['Player2'], 1)
                        print(x, y, z, sep='\n')
                    if (sign['Player1'] == x[1] == x[3] == x[5]) or (sign['Player1'] == y[1] == y[3] == y[5]) or (
                            sign['Player1'] == z[1] == z[3] == z[5]):
                        return 'Player1 won the game!!!'
                    elif (sign['Player1'] == x[1] == y[1] == z[1]) or (sign['Player1'] == x[3] == y[3] == z[3]) or (
                            sign['Player1'] == x[5] == y[5] == z[5]):
                        return 'Player1 won the game!!!'
                    elif (sign['Player1'] == x[1] == y[3] == z[5]) or (sign['Player1'] == x[5] == y[3] == z[1]):
                        return 'Player1 won the game!!!'
                    elif (sign['Player2'] == x[1] == x[3] == x[5]) or (sign['Player2'] == y[1] == y[3] == y[5]) or (
                            sign['Player2'] == z[1] == z[3] == z[5]):
                        return 'Player2 won the game!!!'
                    elif (sign['Player2'] == x[1] == y[1] == z[1]) or (sign['Player2'] == x[3] == y[3] == z[3]) or (
                            sign['Player2'] == x[5] == y[5] == z[5]):
                        return 'Player2 won the game!!!'
                    elif (sign['Player2'] == x[1] == y[3] == z[5]) or (sign['Player2'] == x[5] == y[3] == z[1]):
                        return 'Player2 won the game!!!'
                    counter += 1
                    if counter == 10:
                        return 'The game ends in a draw...'
                else:
                    print("Enter a proper value")
            else:
                print("Enter a proper value")

    print(cmds())
whole()