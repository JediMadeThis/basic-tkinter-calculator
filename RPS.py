import tkinter as tk
import random

options = ["Rock", "Paper", "Scissors"]
app_chosen_option = ""
user_chosen_option = ""
app_won = False
user_wins = 0


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x130")
        self.root.title("Rock, paper, scissors")
        self.root.resizable(False, False)

        self.game()

    def game(self):
        global user_wins

        for i in self.root.winfo_children():
            i.destroy()

        self.root.geometry("300x130")

        def app_choose():
            global options, app_chosen_option
            app_chosen_option = options[random.randint(0, 2)]

        def user_choose(option):
            global user_chosen_option
            user_chosen_option = option

            self.result()

        app_choose()

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()

        self.wins = tk.Label(
            self.frame1, text=f"Wins: {user_wins}", anchor="nw", width=50
        )
        self.wins.pack(padx=4, pady=5)

        self.label1 = tk.Label(self.frame1, text="Select your option", pady=7)
        self.label1.pack()

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()

        # Options

        self.rock = tk.Button(
            self.frame2,
            text="Rock",
            padx=7,
            pady=5,
            command=lambda: user_choose("Rock"),
        )
        self.rock.grid(column=1, row=0, padx=3)

        self.paper = tk.Button(
            self.frame2,
            text="Paper",
            padx=7,
            pady=5,
            command=lambda: user_choose("Paper"),
        )
        self.paper.grid(column=2, row=0, padx=3)

        self.scissors = tk.Button(
            self.frame2,
            text="Scissors",
            padx=7,
            pady=5,
            command=lambda: user_choose("Scissors"),
        )
        self.scissors.grid(column=3, row=0, padx=3)

    def result(self):
        for i in self.root.winfo_children():
            i.destroy()

        self.root.geometry("300x185")

        def check():
            global app_chosen_option, user_chosen_option, app_won, user_wins

            print(app_chosen_option, user_chosen_option)

            if app_chosen_option == "Rock" and user_chosen_option == "Scissors":
                app_won = True
                print("condi 1")
            elif app_chosen_option == "Paper" and user_chosen_option == "Rock":
                app_won = True
                print("condi 2")
            elif app_chosen_option == "Scissors" and user_chosen_option == "Paper":
                app_won = True
                print("condi 3")
            elif app_chosen_option == user_chosen_option:
                app_won = "Draw"
                print("condi 4")
            else:
                print("condi 5")

            if app_won == False:
                user_wins += 1

                self.wins1.config(text=f"Wins: {user_wins}")

        def reset():
            global app_chosen_option, user_chosen_option, app_won

            app_chosen_option = user_chosen_option = ""
            app_won = False

            self.game()

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        self.wins1 = tk.Label(
            self.frame3, text=f"Wins: {user_wins}", anchor="nw", width=50
        )
        self.wins1.pack(padx=4, pady=5)

        check()

        self.result_label = tk.Label(self.frame3)

        if app_won == True:
            self.result_label.config(text="You lost!", fg="#cc8888")
        elif app_won == False:
            self.result_label.config(text="You won!", fg="#00cc00")
        else:
            self.result_label.config(text="Draw!", fg="#000000")

        self.result_label.pack(pady=15)

        self.user_chose = tk.Label(self.frame3, text=f"You chose: {user_chosen_option}")
        self.user_chose.pack()

        self.app_chose = tk.Label(self.frame3, text=f"App chose: {app_chosen_option}")
        self.app_chose.pack()

        self.again = tk.Button(
            self.frame3, text="Play again", padx=7, pady=5, command=reset
        )
        self.again.pack(pady=10)


root = tk.Tk()
App(root)
tk.mainloop()
