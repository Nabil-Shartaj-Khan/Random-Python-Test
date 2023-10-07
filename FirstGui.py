from tkinter import *

window = Tk()
window.geometry("640x480")
window.title("Nabil's world")
window.config(background="#FFFFFF")

counter = 0

def calculator():
    global counter
    counter += 1
    print(f"You clicked {counter} times.")

app_label = Label(
    window,
    text="Welcome to my app",
    font=("Arial", 35, 'bold'),
    fg='#EE0909',
    bg='black',
    bd=15,
    padx=15,
    pady=15
)

app_label.pack()  # First, pack the label to appear at the top

button_app = Button(
    window,
    text="Calculator",
    font=('Comic Sans', 20),
    fg='#1CD802',
    command=calculator,
    activebackground='#FFFFFF',
    activeforeground='#EE0909',
    relief=RAISED
)

button_app.pack()  
window.mainloop()
