import tkinter

button_values = [
    ["AC","+/-","%","/"],
    ["7","8","9","x"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","\u221A","="]
]
right_symbols = ["+","x","-","/","="]
top_symbols = ["AC","+/-","%"]

row_count = len(button_values)#5
column_count = len(button_values[0])#4

color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "#ffffff"

#A+B , A-B ,A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
    global A,B,operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        return str(int(num))
    else:
        return str(num)


def button_clicked(value):
    global right_symbols,top_symbols,label,A,B,operator
    if value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
          result = float(label["text"]) * -1
          label["text"] = remove_zero_decimal(result)
        elif value == "%":
           result = float(label["text"]) / 100
           label["text"] = remove_zero_decimal(result)
        return
    if  value == "\u221A":
         result = float(label["text"]) ** 0.5
         label["text"] = remove_zero_decimal(result)
         return

    if value == ".":
        if "." not in label["text"]:
            label["text"] += value
        return

    if value in "0123456789":
        if label["text"] == "0":
            label["text"] = value
        else:
            label["text"] += value
        return


    if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "x":
                    label["text"] = remove_zero_decimal(numA * numB)

                elif operator == "/":
                    label["text"] = remove_zero_decimal(numA / numB)

            clear_all()
    elif value in ["+", "-", "x", "/"]:
        A = label["text"]
        label["text"] = "0"
        B = "0"
        operator = value


#window_setup
window = tkinter.Tk()#create a window
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0",font=("Arial", 45),background=color_black,foreground=color_white, anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky ="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value,font=("Arial", 30),width=4,height=1 ,command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.configure(background=color_dark_grey, foreground=color_orange)
        elif value in right_symbols:
            button.configure(background=color_orange, foreground=color_white)
        else:
            button.configure(background=color_dark_grey, foreground=color_white)

        button.grid(row=row+1,column=column)
frame.pack()

#center the window
window.update() #update the window with new set dimensions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w) *(h)+(x)+(y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



window.mainloop()
