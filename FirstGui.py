from tkinter import *

window = Tk()
window.geometry("640x480")
window.title("Nabil's world")
window.config(background="#FFFFFF")

counter = 0

def calculator():
    global counter
    user_input_one=int(input("Enter number one- "))
    user_input_two=int(input("Enter number two- "))    
    operator=input("Enter operator + or - or * or / - ")
    result=""
    if operator=="+":
        result=(user_input_one)+(user_input_two)
    elif operator=="-":
        result=user_input_one-user_input_two
    elif operator=="*":
        result=user_input_one*user_input_two 
    elif operator=="/" and user_input_two!=0:
        result=user_input_one/user_input_two
        result=user_input_one*user_input_two 
    elif operator=="/" and user_input_two==0:
        print("Invalid input")
           
    counter += 1
    print("Your result is ",result)
    print(f"You clicked {counter} times.")

def submit():
    username=entry_box.get()
    print("Welcome",username)
    
def delete():
    entry_box.delete(0,END)
    print("Your text has been deleted")

def backspace():
    entry_box.delete(len(entry_box.get())-1,END )
    
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

button_app = Button(
    window,
    text="Calculator",
    font=('Comic Sans', 20),
    fg='#1CD802',
    padx=15,
    pady=10,
    command=calculator,
    activebackground='#FFFFFF',
    activeforeground='#EE0909',
    relief=RAISED
)
entry_box=Entry(
    window,
    font=('arial',15),
    bg='#1BDD00',
    fg="#020A00",
    relief=RAISED
)
submit_button=Button(
    window,
    command=submit,
    text="submit",
    relief=RAISED
)
delete_button=Button(
    window,
    text='Delete',
    command=delete,
    relief=RAISED
)
backspace_button=Button(
    window,
    text='Backspace',
    command=backspace,
    relief=RAISED 
)
#entry,check,list,message,textbox

#packing
app_label.pack()
button_app.pack() 
entry_box.pack(side='left')
submit_button.pack(side='right')
delete_button.pack(side='right')
backspace_button.pack(side='right')

window.mainloop()
