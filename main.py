from tkinter import *

window = Tk()
window.title("BMI CALCULATOR")
window.config(width=300,height=300)

label_1 = Label(text="Enter your weight (kg)")
label_1.place(x=85,y=50)

entry_1 = Entry()
entry_1.config(width=16)
entry_1.place(x=95,y=80)

label_2 = Label()
label_2.config(text="Enter your height (cm)")
label_2.place(x=85,y=130)

entry_2 = Entry()
entry_2.config(width=16)
entry_2.place(x=95,y=160)

label_3 = Label()


def entry_1get():
    user_inp = entry_1.get()
    return user_inp

def entry_2get():
    user_inp = entry_2.get()
    return user_inp

def between(bmi):
    if bmi < 18.5:
        label_3.config(text=f"Your BMI is {bmi}. You are under weight")
    elif 24.9 >= bmi >= 18.5:
        label_3.config(text=f"Your BMI is {bmi}. You are normal weight")
    elif 29.9 >= bmi >= 25:
        label_3.config(text=f"Your BMI is {bmi}. You are over weight")
    elif 34.9 >= bmi >= 30:
        label_3.config(text=f"Your BMI is {bmi}. You are obesity class 1")
    elif 39.9 >= bmi >= 35:
        label_3.config(text=f"Your BMI is {bmi}. You are obesity class 2")
    elif bmi >= 40:
        label_3.config(text=f"Your BMI is {bmi}. You are extreme obesity")

def Calculate():

    try:

        user_input_1 = entry_1get()
        user_input_2 = entry_2get()
        squareinp = float(user_input_2) ** 2


        if 3 > float(user_input_2) > 0:
            bmi_1 = float(user_input_1) / squareinp
            bmi_1 = round(bmi_1,1)
            between(bmi_1)
            label_3.place(x=40, y=240)

        elif 300 > float(user_input_2) > 0:
            new_input_2 = float(user_input_2) / 100
            new_input_square = new_input_2 ** 2
            bmi_2 = float(user_input_1) / new_input_square
            bmi_2 = round(bmi_2,1)
            between(bmi_2)
            label_3.place(x=40, y=240)

    except ValueError:
        label_3.config(text="Please log correct number!!")
        label_3.place(x=61, y=240)

button = Button()
button.config(text="Calculate",width=7,command=Calculate)
button.place(x=115,y=195)


window.mainloop()