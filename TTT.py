import tkinter as tk

turn = "X"

red = "#ff0000"
blue = "#0000ff"


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x620")
        self.root.resizable(False, False)
        self.root.title("Tic Tac Toe (X/O)")

        self.game()

    def game(self):
        for i in self.root.winfo_children():
            i.destroy()

        def win():
            for buttons in self.frame2.winfo_children():
                buttons.configure(state="disabled")

            self.again = tk.Button(
                self.frame3,
                text="Play again",
                padx=18,
                pady=13,
                font=("Century Gothic", 18),
                command=reset,
            )

            self.again.pack(pady=15)

        def reset():
            global turn

            turn = "X"

            for buttons in self.frame2.winfo_children():
                buttons.configure(state="normal", text="")

            self.again.destroy()

            self.turn_label.config(
                text=f"Turn: {turn}",
                fg="#ff0000" if turn == "X" else "#0000ff",
            )

        def check():
            # X

            # Y-axis
            if self.c1r1["text"] == self.c2r1["text"] == self.c3r1["text"] == "X":
                self.turn_label.config(text="X Wins: Row 1", fg=red)

                self.c1r1.config(disabledforeground=red)
                self.c2r1.config(disabledforeground=red)
                self.c3r1.config(disabledforeground=red)

                win()

            elif self.c1r2["text"] == self.c2r2["text"] == self.c3r2["text"] == "X":
                self.turn_label.config(text="X Wins: Row 2", fg=red)

                self.c1r2.config(disabledforeground=red)
                self.c2r2.config(disabledforeground=red)
                self.c3r2.config(disabledforeground=red)

                win()

            elif self.c1r3["text"] == self.c2r3["text"] == self.c3r3["text"] == "X":
                self.turn_label.config(text="X Wins: Row 3", fg=red)

                self.c1r3.config(disabledforeground=red)
                self.c2r3.config(disabledforeground=red)
                self.c3r3.config(disabledforeground=red)

                win()

            # X-axis
            elif self.c1r1["text"] == self.c1r2["text"] == self.c1r3["text"] == "X":
                self.turn_label.config(text="X Wins: Column 1", fg=red)

                self.c1r1.config(disabledforeground=red)
                self.c1r2.config(disabledforeground=red)
                self.c1r3.config(disabledforeground=red)

                win()

            elif self.c2r1["text"] == self.c2r2["text"] == self.c2r3["text"] == "X":
                self.turn_label.config(text="X Wins: Column 2", fg=red)

                self.c2r1.config(disabledforeground=red)
                self.c2r2.config(disabledforeground=red)
                self.c2r3.config(disabledforeground=red)

                win()

            elif self.c3r1["text"] == self.c3r2["text"] == self.c3r3["text"] == "X":
                self.turn_label.config(text="X Wins: Column 3", fg=red)

                self.c3r1.config(disabledforeground=red)
                self.c3r2.config(disabledforeground=red)
                self.c3r3.config(disabledforeground=red)

                win()

            # Diagonals
            elif self.c1r1["text"] == self.c2r2["text"] == self.c3r3["text"] == "X":
                self.turn_label.config(text="X Wins: Diagonal", fg=red)

                self.c1r1.config(disabledforeground=red)
                self.c2r2.config(disabledforeground=red)
                self.c3r3.config(disabledforeground=red)

                win()

            elif self.c3r1["text"] == self.c2r2["text"] == self.c1r3["text"] == "X":
                self.turn_label.config(text="X Wins: Diagonal", fg=red)

                self.c3r1.config(disabledforeground=red)
                self.c2r2.config(disabledforeground=red)
                self.c1r3.config(disabledforeground=red)

                win()

            # O

            # Y-axis
            if self.c1r1["text"] == self.c2r1["text"] == self.c3r1["text"] == "O":
                self.turn_label.config(text="O Wins: Row 1", fg=blue)

                self.c1r1.config(disabledforeground=blue)
                self.c2r1.config(disabledforeground=blue)
                self.c3r1.config(disabledforeground=blue)

                win()

            elif self.c1r2["text"] == self.c2r2["text"] == self.c3r2["text"] == "O":
                self.turn_label.config(text="O Wins: Row 2", fg=blue)

                self.c1r2.config(disabledforeground=blue)
                self.c2r2.config(disabledforeground=blue)
                self.c3r2.config(disabledforeground=blue)

                win()

            elif self.c1r3["text"] == self.c2r3["text"] == self.c3r3["text"] == "O":
                self.turn_label.config(text="O Wins: Row 3", fg=blue)

                self.c1r3.config(disabledforeground=blue)
                self.c2r3.config(disabledforeground=blue)
                self.c3r3.config(disabledforeground=blue)

                win()

            # X-axis
            elif self.c1r1["text"] == self.c1r2["text"] == self.c1r3["text"] == "O":
                self.turn_label.config(text="O Wins: Column 1", fg=blue)

                self.c1r1.config(disabledforeground=blue)
                self.c1r2.config(disabledforeground=blue)
                self.c1r3.config(disabledforeground=blue)

                win()

            elif self.c2r1["text"] == self.c2r2["text"] == self.c2r3["text"] == "O":
                self.turn_label.config(text="O Wins: Column 2", fg=blue)

                self.c2r1.config(disabledforeground=blue)
                self.c2r2.config(disabledforeground=blue)
                self.c2r3.config(disabledforeground=blue)

                win()

            elif self.c3r1["text"] == self.c3r2["text"] == self.c3r3["text"] == "O":
                self.turn_label.config(text="O Wins: Column 3", fg=blue)

                self.c3r1.config(disabledforeground=blue)
                self.c3r2.config(disabledforeground=blue)
                self.c3r3.config(disabledforeground=blue)

                win()

            # Diagonals
            elif self.c1r1["text"] == self.c2r2["text"] == self.c3r3["text"] == "O":
                self.turn_label.config(text="O Wins: Diagonal", fg=blue)

                self.c1r1.config(disabledforeground=blue)
                self.c2r2.config(disabledforeground=blue)
                self.c3r3.config(disabledforeground=blue)

                win()
            elif self.c3r1["text"] == self.c2r2["text"] == self.c1r3["text"] == "O":
                self.turn_label.config(text="O Wins: Diagonal", fg=blue)

                self.c3r1.config(disabledforeground=blue)
                self.c2r2.config(disabledforeground=blue)
                self.c1r3.config(disabledforeground=blue)

                win()

        def place(slot):
            global turn

            if slot["text"]:
                return

            slot.config(text=turn)

            if turn == "X":
                turn = "O"
                self.turn_label.config(fg="#0000ff")
                slot.config(fg="#ff0000")
            else:
                turn = "X"
                self.turn_label.config(fg="#ff0000")
                slot.config(fg="#0000ff")

            self.turn_label.config(text=f"Turn: {turn}")
            check()

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()

        self.turn_label = tk.Label(
            self.frame1,
            text=f"Turn: {turn}",
            fg="#ff0000" if turn == "X" else "#0000ff",
            font=("Century Gothic", 36),
            pady=23,
        )

        self.turn_label.pack()

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()

        # Row 1

        self.c1r1 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c1r1)
        )
        self.c1r1.grid(column=1, row=1)

        self.c2r1 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c2r1)
        )
        self.c2r1.grid(column=2, row=1)

        self.c3r1 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c3r1)
        )
        self.c3r1.grid(column=3, row=1)

        # Row 2

        self.c1r2 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c1r2)
        )
        self.c1r2.grid(column=1, row=2)

        self.c2r2 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c2r2)
        )
        self.c2r2.grid(column=2, row=2)

        self.c3r2 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c3r2)
        )
        self.c3r2.grid(column=3, row=2)

        # Row 3

        self.c1r3 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c1r3)
        )
        self.c1r3.grid(column=1, row=3)

        self.c2r3 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c2r3)
        )
        self.c2r3.grid(column=2, row=3)

        self.c3r3 = tk.Button(
            self.frame2, width=16, height=8, command=lambda: place(self.c3r3)
        )
        self.c3r3.grid(column=3, row=3)

        # Play again button

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        check()


root = tk.Tk()
App(root)
root.mainloop()
