import tkinter as tk

selected_option = "speed"
result = 0


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry("300x320")
        self.root.title("Speed/Distance/Time Calculator")
        self.root.resizable(False, False)

        self.calculator()

    def calculator(self):
        def select(option):
            global selected_option

            self.__getattribute__(f"{selected_option}_btn").config(state="normal")
            selected_option = option
            self.__getattribute__(f"{selected_option}_btn").config(state="disabled")

            update_input_labels()

        def update_input_labels():
            global selected_option

            match selected_option:
                case "speed":
                    self.first_label.config(text="Distance")
                    self.second_label.config(text="Time")
                case "distance":
                    self.first_label.config(text="Speed")
                    self.second_label.config(text="Time")
                case "time":
                    self.first_label.config(text="Distance")
                    self.second_label.config(text="Speed")

        def calculate():
            global selected_option, result, result_fraction

            f_i = self.first_input.get()
            s_i = self.second_input.get()

            first = float(f_i)
            second = float(s_i)

            match selected_option:
                case "speed":
                    result = first / second
                case "time":
                    result = first / second
                case "distance":
                    result = first * second

            if result.is_integer():
                result = str(int(result))
                # Converts 'result' from Float -> Integer -> String
            else:
                result = str(round(result, 3))
                # Rounds 'result' by 3 digits
                # Example: 2.8639567 -> 2.864

            self.result_label.config(text=result)
            self.fraction_label.config(text=result_fraction)

        # Input validation
        def check_input(P):
            if P == "":
                return True

            try:
                float(P)
                return True

            except ValueError:
                return False

        # Option selection

        self.select_frame = tk.Frame(self.root)
        self.select_frame.pack(pady=15)

        self.select_label = tk.Label(self.select_frame, text="Find:")

        self.speed_btn = tk.Button(
            self.select_frame,
            text="Speed",
            state="disabled",
            disabledforeground="red",
            padx=7,
            pady=5,
            command=lambda: select("speed"),
        )

        self.distance_btn = tk.Button(
            self.select_frame,
            text="Distance",
            disabledforeground="red",
            padx=7,
            pady=5,
            command=lambda: select("distance"),
        )

        self.time_btn = tk.Button(
            self.select_frame,
            text="Time",
            disabledforeground="red",
            padx=7,
            pady=5,
            command=lambda: select("time"),
        )

        self.select_label.grid(row=1, column=1, padx=5)
        self.speed_btn.grid(row=1, column=2)
        self.distance_btn.grid(row=1, column=3)
        self.time_btn.grid(row=1, column=4)

        # Inputs

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=30)

        self.first_label = tk.Label(self.input_frame, width=10, text="Distance")
        self.first_input = tk.Entry(
            self.input_frame,
            validate="key",
            validatecommand=(root.register(check_input), "%P"),
        )
        self.first_equal_label = tk.Label(self.input_frame, text="=", width=5)

        self.second_label = tk.Label(self.input_frame, width=10, text="Time")
        self.second_input = tk.Entry(
            self.input_frame,
            validate="key",
            validatecommand=(root.register(check_input), "%P"),
        )
        self.second_equal_label = tk.Label(self.input_frame, text="=", width=5)

        self.first_label.grid(column=1, row=1)
        self.first_input.grid(column=3, row=1)
        self.first_equal_label.grid(column=2, row=1)

        self.second_label.grid(column=1, row=2)
        self.second_input.grid(column=3, row=2)
        self.second_equal_label.grid(column=2, row=2)

        # Calculation

        self.calculate_frame = tk.Frame(self.root)
        self.calculate_frame.pack()

        self.calculate_btn = tk.Button(
            self.calculate_frame, text="Calculate", padx=7, pady=5, command=calculate
        )
        self.calculate_btn.pack()

        self.result_label = tk.Label(
            self.calculate_frame, text="0", font=("Century Gothic", 24)
        )
        self.result_label.pack(pady=8)

        # self.fraction_label = tk.Label(
        #     self.calculate_frame, font=("Century Gothic", 18)
        # )
        # self.fraction_label.pack(pady=5)


root = tk.Tk()
App(root)
root.mainloop()
