import tkinter as tk
from random import randint

score = 0

colors = ["red", "green", "blue", "yellow"]

target_pattern = []
current_pattern = ["green", "blue", "green"]

# 2 - 1 = 1


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry("350x400")
        self.root.resizable(False, False)
        self.root.title("Memory Game")

        self.game()

    def game(self) -> None:
        def add_random_color() -> None:
            global colors, target_pattern

            random_color = colors[randint(0, 3)]
            target_pattern.append(random_color)

        def add_current_pattern(slot: tk.Button) -> None:
            global current_pattern, target_pattern, score

            # Get button color
            slot_color = slot["activebackground"]

            if slot_color == target_pattern[len(current_pattern) - len(target_pattern)]:
                current_pattern.append(slot_color)

                if len(current_pattern) == len(target_pattern):
                    set_button_state("disabled")

                    score += 1
                    self.label.config(text=f"Score: {score}")

                    add_random_color()
                    show_target_pattern()
            else:
                set_button_state("disabled")

                current_pattern.clear()
                target_pattern.clear()

                self.label.config(text=f"You lost! Score: {score}")

                score = 0

                self.start_btn.config(state="normal")  # normal disabled

        def set_button_state(state) -> None:
            for button in self.frame2.winfo_children():

                if state == "disabled":
                    button.configure(background="#e1e1e1")

                elif state == "normal":
                    button.configure(background="SystemButtonFace")

                button.configure(state=state)

        def show_target_pattern() -> None:
            global target_pattern

            if not target_pattern:
                return

            current_pattern.clear()

            def loop(i: int = 0) -> None:
                c = target_pattern[i]
                w = self.__getattribute__(c)

                # print(i, c)

                def reveal(color=c, after_color="#e1e1e1", will_loop=True):
                    slot_bg = self.__getattribute__(color)
                    slot_bg.config(bg=color)

                    slot_bg.after(500, lambda: slot_bg.config(bg=after_color))

                    if will_loop:
                        slot_bg.after(500, lambda: loop(i + 1))

                if i < len(target_pattern) - 1:
                    w.after(500, lambda: reveal(color=c, will_loop=True))
                else:
                    w.after(
                        500,
                        lambda: reveal(color=c, after_color="#e1e1e1", will_loop=False),
                    )
                    w.after(1500, lambda: set_button_state("normal"))

            loop()

        def start() -> None:
            global target_pattern, current_pattern

            self.start_btn.config(state="disabled")
            self.label.config(text=f"Score: {score}")

            target_pattern.clear()
            current_pattern.clear()

            add_random_color()

            set_button_state("disabled")
            show_target_pattern()

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()

        self.label = tk.Label(
            self.frame1, text=f"Score: {score}", font=("Century Gothic", 20), pady=10
        )
        self.label.pack()

        self.start_btn = tk.Button(
            self.frame1, text="Start", padx=8, pady=6, command=start
        )
        self.start_btn.pack(pady=8)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()

        self.red = tk.Button(
            self.frame2,
            activebackground="red",
            width=16,
            height=8,
            command=lambda: add_current_pattern(self.red),
            state="disabled",
        )
        self.red.grid(column=1, row=1)

        self.green = tk.Button(
            self.frame2,
            activebackground="green",
            width=16,
            height=8,
            command=lambda: add_current_pattern(self.green),
            state="disabled",
        )
        self.green.grid(column=2, row=1)

        self.blue = tk.Button(
            self.frame2,
            activebackground="blue",
            width=16,
            height=8,
            command=lambda: add_current_pattern(self.blue),
            state="disabled",
        )
        self.blue.grid(column=1, row=2)

        self.yellow = tk.Button(
            self.frame2,
            activebackground="yellow",
            width=16,
            height=8,
            command=lambda: add_current_pattern(self.yellow),
            state="disabled",
        )
        self.yellow.grid(column=2, row=2)


root = tk.Tk()
App(root)
root.mainloop()
