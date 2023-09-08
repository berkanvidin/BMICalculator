from logging import root
from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=200)

def isNumber():
    try:
        if weight_entry.get() == "" or height_entry.get()=="":
            result_label.config(text="Do not allow null")
        else:
            my_weight = int(weight_entry.get())
            my_height = int(height_entry.get())
            my_bmi = my_weight / (my_height/100)**2
            if my_bmi <= 18.4 :
                result_label.config(text=f"Your BMI = {my_bmi:.1f}.  You are underweight")
            elif 18.5<= my_bmi <= 24.9:
                result_label.config(text=f"Your BMI = {my_bmi:.1f}.  You are normal")
            elif 25.0 <= my_bmi <= 39.9:
                result_label.config(text=f"Your BMI = {my_bmi:.1f}.  You are overweight")
            elif my_bmi>=40.0:
                result_label.config(text=f"Your BMI = {my_bmi:.1f}.  You are obesse")
    except ValueError:
        result_label.config(text="Height or weight is not number. Please Control !")

weight_label = Label(window,text="Enter your weight(kg)")
weight_label.pack()
weight_entry = Entry(window)
weight_entry.pack(pady=20)

height_label = Label(text="Enter your height(cm)")
height_label.pack(pady=20)
height_entry = Entry(window)
height_entry.pack(pady=20)

calculate_btn = Button(text="Calculate",command=isNumber)
calculate_btn.pack(pady=20)

result_label = Label(window,text='')
result_label.pack(pady=20)






window.mainloop()