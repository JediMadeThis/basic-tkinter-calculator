import tkinter as tk

"""
    Example of 3 + 2

    3 -> left_side
    + -> action/operator
    2 -> right_side

    and then, 7 would be the 'result'.
"""

left_side = "0"
action = ""
right_side = ""
result = 0


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x400")
        self.master.title("Calculator")
        self.master.resizable(False, False)

        self.calculator()

    def calculator(self):

        # Makes these variables global instead of local.
        global left_side, action

        # First frame for elements that uses .pack()
        self.frame1 = tk.Frame(self.master)
        self.frame1.pack()

        # Second frame for elements that uses .grid()
        # (Grid is basically a table, specifying where to place elements with rows and columns)
        self.frame2 = tk.Frame(self.master)
        self.frame2.pack()

        # Function for putting new number into the expression.
        def add_number(number: str) -> None:

            # Makes these variables global.
            global left_side, right_side, action

            # Checks if the operator is selected.
            if action and right_side and right_side[0] == "0" and len(right_side) == 1:
                right_side = number

            elif action and right_side and right_side[0] != "0":
                right_side += number

            elif action and right_side and right_side[0] == "0" and len(right_side) > 1:
                right_side += number

            elif not action and left_side and left_side[0] == "0" and len(left_side) == 1:
                left_side = number

            elif action and left_side and not right_side:
                right_side += number

            elif not action and not right_side:
                left_side += number

            print(left_side, action, right_side)
            self.label.config(text=f"{left_side or "0"} {action} {right_side}")

            update_sign_bg()

        # Function for adding decimals.
        def add_decimal() -> None:

            # Makes these variables global.
            global left_side, right_side, action

            # Checks if the value of the right side doesn't already have a decimal point,
            # preventing having two decimal points in a value.
            if right_side and not right_side.__contains__("."):
                right_side += "."

                print(left_side, action, right_side)

            # Same for here, but for the left side.
            elif left_side and not left_side.__contains__("."):
                left_side += "."

                print(left_side, action, right_side)

            else:
                print(left_side, action, right_side)

            self.label.config(text=f"{left_side} {action} {right_side}")

            update_sign_bg()

        def update_sign_bg():
            global action

            default_color = self.master['background']
            color = "#aaaaff"

            self.add.config(bg=default_color)
            self.subtract.config(bg=default_color)
            self.multiply.config(bg=default_color)
            self.divide.config(bg=default_color)

            match action:
                case '+':
                    self.add.config(bg=color)
                case '-':
                    self.subtract.config(bg=color)
                case '*':
                    self.multiply.config(bg=color)
                case '/':
                    self.divide.config(bg=color)

        # Function for updating the operator/sign.
        def update_sign(sign: str) -> None:

            # Makes these variables global.
            global left_side, right_side, action

            # Checks if there's any values in left side.
            if left_side:

                # Store operator in variable 'action'.
                action = sign

            print(left_side, action, right_side)
            self.label.config(text=f"{left_side} {action} {right_side}")

            update_sign_bg()

        # Deletes last character from expression,
        # like the backspace key on your keyboard.
        def delete_last() -> None:

            # Makes these variables global.
            global left_side, right_side, action

            # Removes operator, if nothing is on right side.
            if action and right_side == "":
                action = ""

            elif action:
                right_side = right_side[:-1]

            elif not action and left_side and len(left_side) == 1:
                left_side = "0"

            elif not action and left_side and left_side[0] != "0":
                left_side = left_side[:-1]

            

            print(left_side, action, right_side)
            self.label.config(text=f"{left_side} {action} {right_side}")

            update_sign_bg()

        # Function for clearing evorithing!!
        def clear_evorithing() -> None:

            # Makes these variables global.
            global left_side, right_side, action

            # Clears evorithing!
            right_side = action = ""
            left_side = "0"

            print(left_side, action, right_side)
            self.label.config(text=f"{left_side} {action} {right_side}")

            update_sign_bg()

        # Function for calculation
        def calculate() -> None:

            # Makes these variables global.
            global left_side, right_side, action, result

            # Checks if the expression is complete.
            # (includes left side, right side, and operator)
            if left_side and action and right_side:

                # Converting values into float. (from string)

                f_left_side = float(left_side)
                f_right_side = float(right_side)

                # Check for each operator.
                match action:

                    # Adding
                    case "+":

                        # Store answer in variable 'result'.
                        res = f_left_side + f_right_side
                        result = res.__round__(10)

                    # Subtracting
                    case "-":

                        # Store answer in variable 'result'.
                        res = f_left_side - f_right_side
                        result = res.__round__(10)

                    # Multiplying
                    case "*":

                        # Store answer in variable 'result'.
                        res = f_left_side * f_right_side
                        result = res.__round__(10)

                    # Dividing
                    case "/":

                        # Store answer in variable 'result'.
                        res = f_left_side / f_right_side
                        result = res.__round__(10)

                """
                    Below, clears operator and right side,
                    leaving only the left side. (which is the result)

                    Example:

                    -> 5 + 2
                    -> 7

                    '5' is the left side
                    '2' is the right side
                    '+' is the operator
                    '7' is the result

                    See that the result ends up being on the left side,
                    so we can do further calculations.
                """
                action = right_side = ""

                if result.is_integer():
                    left_side = str(int(result))
                else:
                    left_side = str(result)

                # Prints the result
                print(left_side)

            else:
                print(left_side, action, right_side)

            self.label.config(text=f"{left_side} {action} {right_side}")

            update_sign_bg()

        # Label that shows current expression.
        self.label = tk.Label(
            self.frame1,
            text="0",
            font=("Century Gothic", 24),
            width=20,
            anchor="w",
            padx=15,
            pady=20,
        )
        self.label.grid(row=1, column=0)

        # 0
        self.zero = tk.Button(
            self.frame2, text="0", width=4, height=2, command=lambda: add_number("0")
        )
        self.zero.grid(row=5, column=2)

        # 1
        self.one = tk.Button(
            self.frame2, text="1", width=4, height=2, command=lambda: add_number("1")
        )
        self.one.grid(row=4, column=1)

        # 2
        self.two = tk.Button(
            self.frame2, text="2", width=4, height=2, command=lambda: add_number("2")
        )
        self.two.grid(row=4, column=2)

        # 3
        self.three = tk.Button(
            self.frame2, text="3", width=4, height=2, command=lambda: add_number("3")
        )
        self.three.grid(row=4, column=3)

        # 4
        self.four = tk.Button(
            self.frame2, text="4", width=4, height=2, command=lambda: add_number("4")
        )
        self.four.grid(row=3, column=1)

        # 5
        self.five = tk.Button(
            self.frame2, text="5", width=4, height=2, command=lambda: add_number("5")
        )
        self.five.grid(row=3, column=2)

        # 6
        self.six = tk.Button(
            self.frame2, text="6", width=4, height=2, command=lambda: add_number("6")
        )
        self.six.grid(row=3, column=3)

        # 7
        self.seven = tk.Button(
            self.frame2, text="7", width=4, height=2, command=lambda: add_number("7")
        )
        self.seven.grid(row=2, column=1)

        # 8
        self.eight = tk.Button(
            self.frame2, text="8", width=4, height=2, command=lambda: add_number("8")
        )
        self.eight.grid(row=2, column=2)

        # 9
        self.nine = tk.Button(
            self.frame2, text="9", width=4, height=2, command=lambda: add_number("9")
        )
        self.nine.grid(row=2, column=3)

        # Decimal point
        self.decimal_point = tk.Button(
            self.frame2, text=".", width=4, height=2, command=add_decimal
        )
        self.decimal_point.grid(row=5, column=3)

        # Equal (Calculate)
        self.equal = tk.Button(
            self.frame2, text="=", width=4, height=2, bg="#aaffaa", command=calculate
        )
        self.equal.grid(row=5, column=4)

        # Addition
        self.add = tk.Button(
            self.frame2, text="+", width=4, height=2, command=lambda: update_sign("+")
        )
        self.add.grid(row=4, column=4)

        # Subtraction
        self.subtract = tk.Button(
            self.frame2, text="-", width=4, height=2, command=lambda: update_sign("-")
        )
        self.subtract.grid(row=3, column=4)

        # Multiplication
        self.multiply = tk.Button(
            self.frame2, text="x", width=4, height=2, command=lambda: update_sign("*")
        )
        self.multiply.grid(row=2, column=4)

        # Division
        self.divide = tk.Button(
            self.frame2, text="/", width=4, height=2, command=lambda: update_sign("/")
        )
        self.divide.grid(row=1, column=4)

        # Del (deletes last character)
        self.delete = tk.Button(
            self.frame2, text="Del", width=4, height=2, command=delete_last
        )
        self.delete.grid(row=1, column=3)

        # Clears evorithinggg
        self.clear = tk.Button(
            self.frame2, text="C", width=4, height=2, bg="#ffaaaa", command=clear_evorithing
        )
        self.clear.grid(row=1, column=2)

        for widget in self.frame2.winfo_children():
            widget.config(font=("Century Gothic", 12))

root = tk.Tk()
App(root)
root.mainloop()

"""
    v4

    THIS PATCH:
    - Made every button the same font. (Century Gothic)
    - Added colors for C, operators, and equal buttons.
    - Window is now NOT resizable.
"""

#    I hope you understand this, once again, and again, and again ;-;
