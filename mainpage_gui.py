from tkinter import *
#from tkinter.ttk import *

import mysql.connector as mc
con = mc.connect(host='Localhost',user='root',passwd='cadburychocolate123',db='2playergames')

window = Tk()
window.geometry('1920x1080')
window.title('2playergames')

title = Label(window,text='TWOPLAYERGAMES',font=('Verdana',30)).place(x=600,y=200)
loginbuttonimg = PhotoImage(file=r'C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\loginbutton.png')
signupbuttonimg = PhotoImage(file=r'C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\signupbutton.png')

def login_page():
    window.destroy()
    login = Tk()
    login.geometry('1920x1080')
    login.title('Login')

    loginbuttonimg = PhotoImage(
        file=r'C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\loginbutton.png')
    signupbuttonimg = PhotoImage(
        file=r'C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\signupbutton.png')

    unvalue1 = StringVar()
    unvalue2 = StringVar()
    pwvalue1 = StringVar()
    pwvalue2 = StringVar()

    login_txt = Label(login,text='LOGIN',font=('Verdana',30,'bold'),fg='green').pack(side='top')

    player1_txt = Label(login,text='Player1',font=('Verdana',30,'bold'),fg='red').place(x=100,y=100)

    player2_txt = Label(login, text='Player2', font=('Verdana', 30, 'bold'),fg='blue').place(x=1200, y=100)

    username1 = Label(login, text='Username', font=('Verdana', 10)).place(x=50, y=175)
    user1_input = Entry(login,bg="light yellow",textvariable=unvalue1).place(x=125,y=175)

    password1 = Label(login, text='Password', font=('Verdana', 10)).place(x=50, y=225)
    pass1_input = Entry(login,bg="light yellow",textvariable=pwvalue1).place(x=125, y=225)

    username2 = Label(login, text='Username', font=('Verdana', 10)).place(x=1150, y=175)
    user2_input = Entry(login, bg="light yellow",textvariable=unvalue2).place(x=1225, y=175)

    password2 = Label(login, text='Password', font=('Verdana', 10)).place(x=1150, y=225)
    pass2_input = Entry(login, bg="light yellow",textvariable=pwvalue2).place(x=1225, y=225)

    invalid_username1 = Label(login, text='User does not exist', font=('Verdana', 10), fg='red')
    invalid_username2 = Label(login, text='User does not exist', font=('Verdana', 10), fg='red')
    invalid_password1 = Label(login, text='Wrong password', font=('Verdana', 10), fg='red')
    invalid_password2 = Label(login, text='Wrong password', font=('Verdana', 10), fg='red')
    same_username1 = Label(login, text='Same user entered twice', font=('Verdana', 10), fg='red')
    same_username2 = Label(login, text='Same user entered twice', font=('Verdana', 10), fg='red')

    def registration_page():
        login.destroy()
        register = Tk()
        register.geometry('1920x1080')
        register.config()
        register.title('Registration')

        backtologin_img = PhotoImage(
            file=r'C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\backtologinbutton.png')

        unvalue = StringVar()
        pwvalue1 = StringVar()
        pwvalue2 = StringVar()

        login_txt = Label(register, text='SIGN UP', font=('Verdana', 30, 'bold'), fg='green').pack(side='top')

        username = Label(register, text='Username', font=('Verdana', 10)).place(x=50, y=225)
        user_input = Entry(register, bg="light yellow", textvariable=unvalue).place(x=125, y=225)

        password = Label(register, text='Password', font=('Verdana', 10)).place(x=550, y=225)
        pass_input = Entry(register, bg="light yellow", textvariable=pwvalue1).place(x=625, y=225)

        password_reenter = Label(register, text='Re-Enter Password', font=('Verdana', 10)).place(x=1050, y=225)
        passreenter_input = Entry(register, bg="light yellow", textvariable=pwvalue2).place(x=1185, y=225)

        username_exists = Label(register, text='Username already taken', font=('Verdana', 10), fg='red')
        username_must_be_7chars = Label(register, text='Username must be between 7 and 20 chars',
                                        font=('Verdana', 10), fg='red')
        pass_must_be_7chars = Label(register, text='Password must be between 7 and 20 chars',
                                    font=('Verdana', 10), fg='red')
        pass_match = Label(register, text='Passwords do not match', font=('Verdana', 10), fg='red')

        def getvals1():
            values = (unvalue.get(), pwvalue1.get(), pwvalue2.get())

            def verification(u, p1, p2):
                cur = con.cursor()
                a = cur.execute("select * from bank")
                a = cur.fetchall()
                count = 0
                for user in a:
                    if user[0] == u:
                        count += 1
                if count == 0:
                    if len(u) in range(7,21):
                        count += 1
                    if count == 1:
                        if len(p1) in range(7,21):
                            count += 1
                        if count == 2:
                            if p1 == p2:
                                count += 1
                            if count == 3:
                                return 'W'
                            else:
                                return 'L4'
                        else:
                            return 'L3'
                    else:
                        return 'L2'
                else:
                    return 'L1'

            if verification(values[0], values[1], values[2]) == 'L1':
                username_exists.place(x=250, y=225)
                username_must_be_7chars.place_forget()
                pass_must_be_7chars.place_forget()
                pass_match.place_forget()

            elif verification(values[0], values[1], values[2]) == 'L2':
                username_exists.place_forget()
                username_must_be_7chars.place(x=250, y=225)
                pass_must_be_7chars.place_forget()
                pass_match.place_forget()

            elif verification(values[0], values[1], values[2]) == 'L3':
                username_exists.place_forget()
                username_must_be_7chars.place_forget()
                pass_must_be_7chars.place(x=750, y=225)
                pass_match.place_forget()

            elif verification(values[0], values[1], values[2]) == 'L4':
                username_exists.place_forget()
                username_must_be_7chars.place_forget()
                pass_must_be_7chars.place_forget()
                pass_match.place(x=1310, y=225)

            elif verification(values[0], values[1], values[2]) == 'W':
                cur = con.cursor()
                cur.execute('insert into bank values(%s,%s,%s,%s)', (values[0], values[1], 1000, 0))
                con.commit()
                register.destroy()
                login_page()

        back_to_login = Button(register, image=backtologin_img, height=32, width=100, bd=0,
                               command=getvals1).place(x=700, y=400)
        mainloop()


    def getvals():
        values = (unvalue1.get(),pwvalue1.get(),unvalue2.get(),pwvalue2.get())

        def validity(u,p):
            cur = con.cursor()
            a = cur.execute("select * from bank")
            a = cur.fetchall()
            count = 0
            for user in a:
                if user[0] == u:
                    count += 1
            if count == 1:
                for user in a:
                    if user[1] == p and user[0] == u:
                        count += 1
                if count == 2:
                    return 'W'
                else:
                    return 'L2'
            else:
                return 'L1'

        if validity(values[0], values[1]) == 'L1' and validity(values[2], values[3]) == 'L1':
            invalid_username1.place(x=250, y=175)
            invalid_username2.place(x=1350, y=175)
            invalid_password1.place_forget()
            invalid_password2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'L2' and validity(values[2], values[3]) == 'L1':
            invalid_password1.place(x=250, y=225)
            invalid_username2.place(x=1350, y=175)
            invalid_username1.place_forget()
            invalid_password2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'L1' and validity(values[2], values[3]) == 'L2':
            invalid_username1.place(x=250, y=175)
            invalid_password2.place(x=1350, y=225)
            invalid_password1.place_forget()
            invalid_username2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'L2' and validity(values[2], values[3]) == 'L2':
            invalid_password1.place(x=250, y=225)
            invalid_password2.place(x=1350, y=225)
            invalid_username1.place_forget()
            invalid_username2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif values[0] == values[2]:
            same_username1.place(x=250, y=175)
            same_username2.place(x=1350, y=175)
            invalid_username1.place_forget()
            invalid_username2.place_forget()
            invalid_password1.place_forget()
            invalid_password2.place_forget()

        elif validity(values[0], values[1]) == 'W' and validity(values[2], values[3]) == 'L1':
            invalid_username2.place(x=1350, y=175)
            invalid_password1.place_forget()
            invalid_username1.place_forget()
            invalid_password2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'W' and validity(values[2], values[3]) == 'L2':
            invalid_password2.place(x=1350, y=175)
            invalid_password1.place_forget()
            invalid_username1.place_forget()
            invalid_username2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'L1' and validity(values[2], values[3]) == 'W':
            invalid_username1.place(x=1350, y=175)
            invalid_password1.place_forget()
            invalid_username1.place_forget()
            invalid_password2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'L2' and validity(values[2], values[3]) == 'W':
            invalid_password1.place(x=1350, y=175)
            invalid_username2.place_forget()
            invalid_username1.place_forget()
            invalid_password2.place_forget()
            same_username1.place_forget()
            same_username2.place_forget()

        elif validity(values[0], values[1]) == 'W' and validity(values[2], values[3]) == 'W':
            login.destroy()
            homepage()

    def homepage():
        games = Tk()
        games.geometry('1920x1080')
        games.config(bg='black')
        games.title('Games')
        bg = PhotoImage(
            file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\mainscreen_wallpaper.png")
        label1 = Label(games, image=bg, bd=0)
        label1.place(x=0, y=0)

        catalogue = Label(games, text='Catalogue', font=('Verdana', 40), fg='red', bg='black').place(x=650, y=200)

        war_icon = PhotoImage(file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\war.png")
        war_btn = Button(games, image=war_icon, height=131, width=250, bg='green').place(x=200, y=400)

        player1 = Label(games, text='Player1', font=('Verdana', 20), fg='blue', bg='red').place(x=125, y=40)
        player2 = Label(games, text='Player2', font=('Verdana', 20), fg='yellow', bg='green').place(x=1400, y=40)

        coin_icon1 = PhotoImage(
            file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\coin_icon.png")
        label2 = Label(games, image=coin_icon1, height=35, width=50, bd=0)
        label2.place(x=50, y=100)

        coin_icon2 = PhotoImage(
            file=r"C:\Users\Sudharsan Balajee\PycharmProjects\TwoPlayerGames\pictures\coin_icon.png")
        label3 = Label(games, image=coin_icon2, height=35, width=50, bd=0)
        label3.place(x=1325, y=100)

        mainloop()


    login_btn1 = Button(login, image=loginbuttonimg, height=24, width=100, bd=0, command=getvals).place(x=700,y=400)
    signup_btn1 = Button(login, image=signupbuttonimg, height=25, width=63, bd=0,command=registration_page).place(x=850, y=400)
    mainloop()


login_btn = Button(window,image=loginbuttonimg,height= 24, width=100,command=login_page).place(x=750,y=400)

mainloop()