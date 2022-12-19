from tkinter import *
import mysql.connector as mc
con = mc.connect(host='Localhost',user='root',passwd='cadburychocolate123',db='2playergames')

turn = 0
counter1 = 0
def tictactoe():
    tictactoe_window = Tk()
    tictactoe_window.geometry('1920x1080')
    tictactoe_window.title('TicTacToe')
    Label(text="Tictactoe",font=('Verdana',30,'bold'),fg='red').pack(side='top')

    board_img = PhotoImage(file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\tictactoe.png")
    board = Label(tictactoe_window,image=board_img)
    board.place(x=475,y=200)

    x_img = PhotoImage(file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\x.png")
    x1 = Label(tictactoe_window,image=x_img)
    x1.place(x=100,y=200)
    x2 = Label(tictactoe_window, image=x_img)
    x2.place(x=250, y=200)
    x3 = Label(tictactoe_window, image=x_img)
    x3.place(x=100, y=350)
    x4 = Label(tictactoe_window, image=x_img)
    x4.place(x=250, y=350)
    x5 = Label(tictactoe_window, image=x_img)
    x5.place(x=175, y=500)

    o_img = PhotoImage(file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\o.png")
    o1 = Label(tictactoe_window, image=o_img)
    o1.place(x=1150, y=200)
    o2 = Label(tictactoe_window, image=o_img)
    o2.place(x=1300, y=200)
    o3 = Label(tictactoe_window, image=o_img)
    o3.place(x=1150, y=350)
    o4 = Label(tictactoe_window, image=o_img)
    o4.place(x=1300, y=350)

    bb_img = PhotoImage(file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\backbutton.png")
    back_button = Button(tictactoe_window,image=bb_img,height=51,width=80,bd=0)
    back_button.place(x=0,y=0)

    def which_button(button_press):
        def placement_main(x_o,b):
            if b == ["b1"]:
                x_o.place(x=525, y=250)
            elif b == ["b2"]:
                x_o.place(x=725, y=250)
            elif b == ["b3"]:
                x_o.place(x=925, y=250)
            elif b == ["b4"]:
                x_o.place(x=525, y=425)
            elif b == ["b5"]:
                x_o.place(x=725, y=425)
            elif b == ["b6"]:
                x_o.place(x=925, y=425)
            elif b == ["b7"]:
                x_o.place(x=525, y=600)
            elif b == ["b8"]:
                x_o.place(x=725, y=600)
            elif b == ["b9"]:
                x_o.place(x=925, y=600)


        def placement1():
            x = []
            coords = x1.place_info()
            if int(coords['x']) < 500:
                x1.place_forget()
                x = ["x1"]
                placement_main(x1,button)
            else:
                coords = x2.place_info()
                if int(coords['x']) < 500:
                    x2.place_forget()
                    x = ["x2"]
                    placement_main(x2, button)
                else:
                    coords = x3.place_info()
                    if int(coords['x']) < 500:
                        x3.place_forget()
                        x = ["x3"]
                        placement_main(x3, button)
                    else:
                        coords = x4.place_info()
                        if int(coords['x']) < 500:
                            x4.place_forget()
                            x = ["x4"]
                            placement_main(x4, button)
                        else:
                            coords = x5.place_info()
                            if int(coords['x']) < 500:
                                x5.place_forget()
                                x = ["x5"]
                                placement_main(x5, button)
            if button == ["b1"]:
                b1.destroy()
            elif button == ["b2"]:
                b2.destroy()
            elif button == ["b3"]:
                b3.destroy()
            elif button == ["b4"]:
                b4.destroy()
            elif button == ["b5"]:
                b5.destroy()
            elif button == ["b6"]:
                b6.destroy()
            elif button == ["b7"]:
                b7.destroy()
            elif button == ["b8"]:
                b8.destroy()
            elif button == ["b9"]:
                b9.destroy()



        def placement2():
            x = []
            coords = o1.place_info()
            if int(coords['x']) > 1125:
                o1.place_forget()
                x = ["o1"]
                placement_main(o1, button)
            else:
                coords = o2.place_info()
                if int(coords['x']) > 1125:
                    o2.place_forget()
                    x = ["o2"]
                    placement_main(o2, button)
                else:
                    coords = o3.place_info()
                    if int(coords['x']) > 1125:
                        o3.place_forget()
                        x = ["o3"]
                        placement_main(o3, button)
                    else:
                        coords = o4.place_info()
                        if int(coords['x']) > 1125:
                            o4.place_forget()
                            x = ["o4"]
                            placement_main(o4, button)
            if button == ["b1"]:
                b1.destroy()
            elif button == ["b2"]:
                b2.destroy()
            elif button == ["b3"]:
                b3.destroy()
            elif button == ["b4"]:
                b4.destroy()
            elif button == ["b5"]:
                b5.destroy()
            elif button == ["b6"]:
                b6.destroy()
            elif button == ["b7"]:
                b7.destroy()
            elif button == ["b8"]:
                b8.destroy()
            elif button == ["b9"]:
                b9.destroy()

        def winner(pl, t):
            winner_txt = Label(tictactoe_window, fg='green', font=('Verdana', 20))

            def check(x_coord1, x_coord2, y_coord1, y_coord2):
                global counter1
                counter1 = 0
                for img in pl:
                    info = img.place_info()
                    if int(info['x']) in range(x_coord1, x_coord2 + 1) and int(info['y']) in range(y_coord1, y_coord2 + 1):
                        counter1 += 1
                return counter1

            if check(500, 950, 200, 300) == 3:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(500, 950, 400, 450) == 3:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(500, 950, 550, 650) == 3:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(500, 550, 200, 650) == 3:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(700, 750, 200, 650) == 3:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(900, 950, 200, 650) == 3:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(500, 550, 200, 300) == 1 and check(700, 750, 400, 450) == 1 and check(900, 950, 550, 650) == 1:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
            elif check(900, 950, 200, 300) == 1 and check(700, 750, 400, 450) == 1 and check(500, 550, 550, 650) == 1:
                if t % 2 == 0:
                    winner_txt.config(text='Player1 has won the game!')
                else:
                    winner_txt.config(text='Player2 has won the game!')
                winner_txt.place(x=600, y=150)
                return ''
        def button_destruction():
            if b1.winfo_exists():
                b1.destroy()
            if b2.winfo_exists():
                b2.destroy()
            if b3.winfo_exists():
                b3.destroy()
            if b4.winfo_exists():
                b4.destroy()
            if b5.winfo_exists():
                b5.destroy()
            if b6.winfo_exists():
                b6.destroy()
            if b7.winfo_exists():
                b7.destroy()
            if b8.winfo_exists():
                b8.destroy()
            if b9.winfo_exists():
                b9.destroy()

        button = [button_press]
        global turn
        if turn%2==0:
            placement1()
            winner([x1,x2,x3,x4,x5],turn)
            if winner([x1,x2,x3,x4,x5],turn) == '':
                button_destruction()
        else:
            placement2()
            winner([o1,o2,o3,o4],turn)
            if winner([o1,o2,o3,o4],turn) == '':
                button_destruction()
        turn+=1

    b1 = Button(tictactoe_window,height=1,width=1,command=lambda m="b1": which_button(m))
    b1.place(x=575,y=287.5)
    b2 = Button(tictactoe_window,height=1,width=1,command=lambda m="b2": which_button(m))
    b2.place(x=775, y=287.5)
    b3 = Button(tictactoe_window,height=1,width=1,command=lambda m="b3": which_button(m))
    b3.place(x=975, y=287.5)
    b4 = Button(tictactoe_window,height=1,width=1,command=lambda m="b4": which_button(m))
    b4.place(x=575, y=462.5)
    b5 = Button(tictactoe_window,height=1,width=1,command=lambda m="b5": which_button(m))
    b5.place(x=775, y=462.5)
    b6 = Button(tictactoe_window,height=1,width=1,command=lambda m="b6": which_button(m))
    b6.place(x=975, y=462.5)
    b7 = Button(tictactoe_window,height=1,width=1,command=lambda m="b7": which_button(m))
    b7.place(x=575, y=637.5)
    b8 = Button(tictactoe_window,height=1,width=1,command=lambda m="b8": which_button(m))
    b8.place(x=775, y=637.5)
    b9 = Button(tictactoe_window,height=1,width=1,command=lambda m="b9": which_button(m))
    b9.place(x=975, y=637.5)

    Label(tictactoe_window, text='Player1', font=('Verdana', 30, 'bold'), fg='black').place(x=125, y=100)

    Label(tictactoe_window, text='Player2', font=('Verdana', 30, 'bold'), fg='white',bg='black').place(x=1200, y=100)
    mainloop()
tictactoe()