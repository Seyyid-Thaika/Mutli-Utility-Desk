from turtle import *
from tkinter import *
from datetime import datetime
import tkinter.messagebox
import pickle
import random
import string



print("---------------------------------------------------------------------------------------------------------------------------")

print("Welcome! Choose any Utility Applications from the following:")

print("---------------------------------------------------------------------------------------------------------------------------")

print("0. Quit the Program")
print("1. Body Mass Index")
print("2. Random Password Generator")
print("3. Calculator")
print("4. Clock")
print("5. Temperature Conversion")
print("6. Stopwatch")
print("7. Create a Time Table")

print("---------------------------------------------------------------------------------------------------------------------------")


a=1


while a!=0:

    a = int(input("Enter an option"))

    if a==1:

        print("BMI Calculator Selected")

        root = tkinter.Tk()
        root.title("BMI Calculator")


        def calculate_bmi():
           kg = float(entry_kg.get())
           height = float(entry_height.get())
           bmi = round(kg / (height ** 2), 2)
           label_result['text'] = f"BMI: {bmi}"


        label_kg = tkinter.Label(root, text="Weight (in KG): ")
        label_kg.grid(column=0, row=0)

        entry_kg = tkinter.Entry(root)
        entry_kg.grid(column=1, row=0)

        label_height = tkinter.Label(root, text="Height (in meters): ")
        label_height.grid(column=0, row=1)

        entry_height = tkinter.Entry(root)
        entry_height.grid(column=1, row=1)

        button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi)
        button_calculate.grid(column=0, row=2)

        label_result = tkinter.Label(root, text="BMI: ")
        label_result.grid(column=1, row=2)

        root.mainloop()




    if a==2:

        print("Random Password Generator Selected")

        def generate_password():
           password = []
           for i in range(5):
               alpha = random.choice(string.ascii_letters)
               symbol = random.choice(string.punctuation)
               numbers = random.choice(string.digits)
               password.append(alpha)
               password.append(symbol)
               password.append(numbers)

           y = "".join(str(x) for x in password)
           lbl.config(text=y)


        root = Tk()
        root.title("PASSWORD GENERATOR")
        root.geometry("250x200")
        btn = Button(root, text="Generate Password", command=generate_password)
        btn.grid(row=2, column=2)
        lbl = Label(root, font=("times", 15, "bold"))
        lbl.grid(row=4, column=2)
        root.mainloop()






    if a==3:

        print("Calculator Selected")

        root = tkinter.Tk()
        root.title("Calculator")

        expression = ""


        def add(value):
           global expression
           expression += value
           label_result.config(text=expression)


        def clear():
           global expression
           expression = ""
           label_result.config(text=expression)


        def calculate():
           global expression
           result = ""
           if expression != "":
               try:
                   result = eval(expression)
               except:
                   result = "error"
                   expression = ""
           label_result.config(text=result)
           expression = str(result)



        def key_handler(event):
           global expression
           if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
               add(event.keysym)
           elif event.keysym == "plus":
               add("+")
           elif event.keysym == "minus":
               add("-")
           elif event.keysym == "asterisk":
               add("*")
           elif event.keysym == "slash":
               add("/")
           elif event.keysym in ("c", "C"):
               clear()
           elif event.keysym == "period":
               add(".")
           elif event.keysym in ("Return", "equal"):
               calculate()
           elif event.keysym == "BackSpace":
               expression = expression[0:len(expression) - 1]
               label_result.config(text=expression)


        root.bind("<Key>", key_handler)

        label_result = tkinter.Label(root, text="")
        label_result.grid(row=0, column=0, columnspan=4)

        button_1 = tkinter.Button(root, text="1", command=lambda: add("1"))
        button_1.grid(row=1, column=0)

        button_2 = tkinter.Button(root, text="2", command=lambda: add("2"))
        button_2.grid(row=1, column=1)

        button_3 = tkinter.Button(root, text="3", command=lambda: add("3"))
        button_3.grid(row=1, column=2)

        button_divide = tkinter.Button(root, text="/", command=lambda: add("/"))
        button_divide.grid(row=1, column=3)

        button_4 = tkinter.Button(root, text="4", command=lambda: add("4"))
        button_4.grid(row=2, column=0)

        button_5 = tkinter.Button(root, text="5", command=lambda: add("5"))
        button_5.grid(row=2, column=1)

        button_6 = tkinter.Button(root, text="6", command=lambda: add("6"))
        button_6.grid(row=2, column=2)

        button_multiply = tkinter.Button(root, text="*", command=lambda: add("*"))
        button_multiply.grid(row=2, column=3)

        button_7 = tkinter.Button(root, text="7", command=lambda: add("7"))
        button_7.grid(row=3, column=0)

        button_8 = tkinter.Button(root, text="8", command=lambda: add("8"))
        button_8.grid(row=3, column=1)

        button_9 = tkinter.Button(root, text="9", command=lambda: add("9"))
        button_9.grid(row=3, column=2)

        button_subtract = tkinter.Button(root, text="-", command=lambda: add("-"))
        button_subtract.grid(row=3, column=3)

        button_clear = tkinter.Button(root, text="C", command=lambda: clear())
        button_clear.grid(row=4, column=0)

        button_0 = tkinter.Button(root, text="0", command=lambda: add("0"))
        button_0.grid(row=4, column=1)

        button_dot = tkinter.Button(root, text=".", command=lambda: add("."))
        button_dot.grid(row=4, column=2)

        button_add = tkinter.Button(root, text="+", command=lambda: add("+"))
        button_add.grid(row=4, column=3)

        button_equals = tkinter.Button(root, text="=", width=16, command=lambda: calculate())
        button_equals.grid(row=5, column=0, columnspan=4)

        root.mainloop()




    if a==4:

        print("Clock Selected")

        def jump(distanz, winkel=0):
           penup()
           right(winkel)
           forward(distanz)
           left(winkel)
           pendown()


        def hand(laenge, spitze):
           fd(laenge * 1.15)
           rt(90)
           fd(spitze / 2.0)
           lt(120)
           fd(spitze)
           lt(120)
           fd(spitze)
           lt(120)
           fd(spitze / 2.0)


        def make_hand_shape(name, laenge, spitze):
           reset()
           jump(-laenge * 0.15)
           begin_poly()
           hand(laenge, spitze)
           end_poly()
           hand_form = get_poly()
           register_shape(name, hand_form)


        def clockface(radius):
           reset()
           pensize(7)
           for i in range(60):
               jump(radius)
               if i % 5 == 0:
                   fd(25)
                   jump(-radius - 25)
               else:
                   dot(3)
                   jump(-radius)
               rt(6)


        def setup():
           global second_hand, minute_hand, hour_hand, writer
           mode("logo")
           make_hand_shape("second_hand", 125, 25)
           make_hand_shape("minute_hand", 130, 25)
           make_hand_shape("hour_hand", 90, 25)
           clockface(160)
           second_hand = Turtle()
           second_hand.shape("second_hand")
           second_hand.color("gray20", "gray80")
           minute_hand = Turtle()
           minute_hand.shape("minute_hand")
           minute_hand.color("blue1", "red1")
           hour_hand = Turtle()
           hour_hand.shape("hour_hand")
           hour_hand.color("blue3", "red3")
           for hand in second_hand, minute_hand, hour_hand:
               hand.resizemode("user")
               hand.shapesize(1, 1, 3)
               hand.speed(0)
           ht()
           writer = Turtle()
           # writer.mode("logo")
           writer.ht()
           writer.pu()
           writer.bk(85)


        def wochentag(t):
           wochentag = ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday", "Sunday"]
           return wochentag[t.weekday()]


        def datum(z):
           monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                    "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
           j = z.year
           m = monat[z.month - 1]
           t = z.day
           return "%s %d %d" % (m, t, j)


        def tick():
           t = datetime.today()
           sekunde = t.second + t.microsecond * 0.000001
           minute = t.minute + sekunde / 60.0
           stunde = t.hour + minute / 60.0
           try:
               tracer(False)  # Terminator can occur here
               writer.clear()
               writer.home()
               writer.forward(65)
               writer.write(wochentag(t),
                            align="center", font=("Courier", 14, "bold"))
               writer.back(150)
               writer.write(datum(t),
                            align="center", font=("Courier", 14, "bold"))
               writer.forward(85)
               tracer(True)
               second_hand.setheading(6 * sekunde)  # or here
               minute_hand.setheading(6 * minute)
               hour_hand.setheading(30 * stunde)
               tracer(True)
               ontimer(tick, 100)
           except Terminator:
               pass


        def main():
           tracer(False)
           setup()
           tracer(True)
           tick()
           return "EVENTLOOP"


        if __name__ == "__main__":
           mode("logo")
           msg = main()
           print(msg)
           mainloop()

    if a==5:

        def main():
           temp = input("Input the temperature you like to convert? (102F or 33C): ")
           degree = int(temp[:-1])
           i_convention = temp[-1]

           if i_convention.upper() == "C":
               result = int(round((9 * degree) / 5 + 32))
               o_convention = "Fahrenheit"
           elif i_convention.upper() == "F":
               result = int(round((degree - 32) * 5 / 9))
               o_convention = "Celsius"
           else:
               print("Input proper convention.")
               quit()
           print("The temperature in", o_convention, "is", result, "degrees.")


        main()



    if a==6:

        print("Stopwatch Selected")

        counter = -1
        running = False


        def counter_label(label):
           def count():
               if running:
                   global counter
                   if counter == -1:
                       display = "Starting..."
                   else:
                       display = str(counter)

                   label['text'] = display

                   label.after(1000, count)
                   counter += 1

           count()


        def Start(label):
           global running
           running = True
           counter_label(label)
           start['state'] = 'disabled'
           stop['state'] = 'normal'
           reset['state'] = 'normal'


        def Stop():
           global running
           start['state'] = 'normal'
           stop['state'] = 'disabled'
           reset['state'] = 'normal'
           running = False


        def Reset(label):
           global counter
           counter = -1
           if running == False:
               reset['state'] = 'disabled'
               label['text'] = 'Welcome!'
           else:
               label['text'] = 'Starting...'


        root = tkinter.Tk()
        root.title("Stopwatch")

        root.minsize(width=250, height=70)
        label = tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
        label.pack()
        start = tkinter.Button(root, text='Start', width=15, command=lambda: Start(label))
        stop = tkinter.Button(root, text='Stop', width=15, state='disabled', command=Stop)
        reset = tkinter.Button(root, text='Reset', width=15, state='disabled', command=lambda: Reset(label))
        start.pack()
        stop.pack()
        reset.pack()
        root.mainloop()

    if a==7:

        print("Time Table Creator Selected")

        root = tkinter.Tk()
        root.title("Time Table")


        def add_task():
           task = entry_task.get()
           if task != "":
               listbox_tasks.insert(tkinter.END, task)
               entry_task.delete(0, tkinter.END)
           else:
               tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


        def delete_task():
           try:
               task_index = listbox_tasks.curselection()[0]
               listbox_tasks.delete(task_index)
           except:
               tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


        def load_tasks():
           try:
               tasks = pickle.load(open("tasks.dat", "rb"))
               listbox_tasks.delete(0, tkinter.END)
               for task in tasks:
                   listbox_tasks.insert(tkinter.END, task)
           except:
               tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


        def save_tasks():
           tasks = listbox_tasks.get(0, listbox_tasks.size())
           pickle.dump(tasks, open("tasks.dat", "wb"))


        frame_tasks = tkinter.Frame(root)
        frame_tasks.pack()

        listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
        listbox_tasks.pack(side=tkinter.LEFT)

        scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
        scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=listbox_tasks.yview)

        entry_task = tkinter.Entry(root, width=50)
        entry_task.pack()

        button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
        button_add_task.pack()

        button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
        button_delete_task.pack()

        button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
        button_load_tasks.pack()

        button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
        button_save_tasks.pack()

        root.mainloop()

print("Thank you.")

print("-------------------------------------------------------------------------------------------------------------------------")
