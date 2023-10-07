from math import *
import time
import os
import random

# This is the login part
def name_fun(password):
    print("Access granted to the makeshift BOT")
    print("Hello how can i help you?")
    print("Oh yes! Your input password is"+" "+password)
    print("let me check a bit", password.upper().islower(), "oh nvm!")
    print("You can't replace it"+" "+password.replace("chat","ai"))
    print("My age is"+" "+str(24))
    user_input=input("What is your name?"+"-")
    print("Oh i see, your name is"+" "+user_input)
    
    user_gender=input("your gender?-")
    user_height=int(input("your height?-"))
    set_male=False
    set_tall=False
    
    if user_gender=="Male" or user_gender=="male" and user_height>=170:
        set_male=True
        set_tall=True
    elif user_gender=="Male" or user_gender=="male" and user_height<=170:
        set_male=True
        set_tall=False
    elif user_gender=="female" or user_gender=="Female" and user_height>=170:
        set_male=False
        set_tall=True
    else:
        set_male=False
        set_tall=False

    if set_male and set_tall==True:
        print("I know you are tall and a male")
    elif not set_male or set_tall==True:
        print("you are a female and tall")
    elif set_male==True or not set_tall:
        print("You are a short man")
    else:
        print("You are a short unknown species")
# *********************************************************************************************
# # Unsolved looping part
def guess_number(user_guess):

    secret_num="Messi"
    guess_counter=0
    total_guess=3
    print("Okay so you have guessed",user_guess)

    if guess_counter>=total_guess:

        if user_guess==secret_num:        
                print("Correct guess, well done my friend!")
                guess_counter+=1
                print ("You have guessed in", guess_counter,"th time")
                return guess_counter
                
        else:
            print("Nope! Try again!")
            guess_counter+=1
            total_guess-=1
            print("Remaining guesses", total_guess)
    
    else:    
        print("You are out of guesses")

# *********************************************************************************************
#for loop part
def for_loop():
    total_things=(int(input("Okay, How many times do you wanna enter?- ")))
    list_input=[]

    for i in range(0,total_things):
        inputs=(input("Please enter a list of your favourite things!- "))


        list_input.append(inputs)

        if len(list_input)<(total_things):
            print("********")
            print("Your input data are-", list_input)
            print("You may Keep adding")
            print("********\n")

        else:
            print("Processing your list standby-")
            time.sleep(3)
            print("********")
            print("You have reached your input limit which is", total_things, "times")
            print("Finally your list is- ", list_input)
            print("********\n")

# *********************************************************************************************
#nested loops fun

def nested_loops(rows,columns):
    input_user=(input("Enter the symbol- "))
    for i in range (rows):
        for j in range (columns):
            print(input_user,end="")

        
    print("Initialized loop")
            
# *********************************************************************************************    
#break-continue-pass

def state_fun(phoneNo,favNum,favTeam):
    
    while True:
        if phoneNo!="":
            break
        else:
            print("here we go")

            
    for i in favNum:
            if i=="-" or "-" or "+":
                continue
            print("String was found and updated favourite numbers are", i, end="")
                

    if favTeam=="Chelsea" or "chelsea":
        pass
    print("Nice", favTeam, "I love that") 

# *********************************************************************************************    

#list_fun

def list_fun():
    total_things=(int(input("Okay, How many Elements?- ")))
    list_input=[]

    for i in range(0,total_things):
        inputs=(input("Please enter a list of your favourite things!- "))
        list_input.append(inputs)
        print(list_input)

    print("Processing List options....")
    time.sleep(3)
    print("Your first and last item on the list is", "[",list_input[0],"]","and","[",list_input[-1],"]")
    print("List shown")
    time.sleep(2)
    print("Do you wanna change an index? input your index and replacement value")
    user_index=int(input("Enter your index value- "))
    repla_value=(input("Enter replacement value- "))
    list_input[user_index]=repla_value
    print("Updated list input is- ", list_input)

# *********************************************************************************************    
def try_except():
    try:
        user_input_one=(int(input("Enter a number for operation- ")))
        user_input_two=(int(input("Enter another number for operation- ")))
        operator=(input("Enter the operator (+ or - or / or *)- "))

        if operator=="+":
            print("Sum is- ", user_input_two+user_input_two)
        
        elif operator=="-":
            print("Substraction is- ", user_input_one-user_input_two)
        
        elif operator=="*":
            print("Multiplication is- ", user_input_one*user_input_two)
        
        elif operator=="/":
            print("Division is- ", user_input_one/user_input_two)
        
        else:
             print("You've entered an invalid operator :D ")
            
    except ZeroDivisionError:
        print("Not possible! You've entered an infinity problem ")
          
# *********************************************************************************************    

# def file_fun():
#     file_path=(r"C:\Users\USER\Downloads\Test Python")
#     if os.path.exists(file_path):
#         print("Your file has been located! ")
    
#     text=(input("write whatever you want- "))
#     with open((r"C:\Users\USER\Downloads\Test Python"),'w') as file:
#         file.write(text)
        
# *********************************************************************************************    
from anotherTest import testModule,testAnModule
testModule()
testAnModule()

# *********************************************************************************************    
import random
def game_hand():
    while True:

        all_choices = ["rock", "paper", "scissors"]
        com_choice = random.choice(all_choices)
        user_choice = None
        game_counter=0

        while user_choice not in all_choices:
            user_choice = input("Rock, paper, or scissors?- ").lower()

        print("You chose:", user_choice)
        print("AI chose:", com_choice)

        if user_choice==com_choice:
            print("The game is a tie because you picked{} and AI picked{}").format(user_choice,com_choice)
            game_counter+=1
            print("You have played", game_counter, "times")

        elif user_choice=="paper":
            if com_choice=="scissor":
                print("You have lost because you picked{} and AI picked{}").format(user_choice,com_choice)
                game_counter+=1
                print("You have played", game_counter, "times")
            elif com_choice=="rock":
                print("You won because you picked{} and AI picked{}").format(user_choice,com_choice)
                game_counter+=1
                print("You have played", game_counter, "times")
        
        elif user_choice=="rock":
            if com_choice=="scissor":
                print("You won you picked{} and AI picked{}").format(user_choice,com_choice)
                game_counter+=1
                print("You have played", game_counter, "times")

            elif com_choice=="paper":
                print("You lost because you picked{} and AI picked{}").format(user_choice,com_choice)
                game_counter+=1
                print("You have played", game_counter, "times")

        elif user_choice=="rock":
            if com_choice=="scissor":
                print("You wont because you picked{} and AI picked{}").format(user_choice,com_choice)
                game_counter+=1
                print("You have played", game_counter, "times")
            elif com_choice=="paper":
                print("you picked{} and AI picked{}").format(user_choice,com_choice)
                game_counter+=1
                print("You have played", game_counter, "times")
            
            play_again=input("play again?- ")

        if play_again!="yes":
            break

        print("Good bye")
        

# ********************************************************************************************* 
# from ObjectOriented import my_room

# room_1=my_room("Big","white",2020,"Nabil")

# print("Your room is", room_1.room)
# print("Your room colour is", room_1.colour)

# room_1.newPerson()

# ********************************************************************************************* 
#parent class child and method overriding

# class university:

#     study=True
#     def students(self):
#         print("They are studying")

#     def teachers(self):
#         print("They are teaching")

#     def campus(self):
#         print("It is mandatory")

# class Bracu(university):
#     def printbracu(self):
#         print("I also wanna print please")
#     def campus(self):
#         print("No campus for me because i overrided the method")
#         user_input=input("permanent?- ")
#         if user_input=="Yes".lower():
#             print("In your dreams")
#         else:
#             print('Thats nice')

# class Nsu(university):
#     def printnsu(self):
#         print("Me too please")

# bracu=Bracu()
# nsu=Nsu()

# bracu.campus()

    
# ********************************************************************************************* 

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

# class square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length, width)
    
#     def area(self):

# class cube(Rectangle):

#     def __init__(self, length, width,height):
#         super().__init__(length, width)
#         self.height=height
    
#     def vol(self):
#         return self.length*self.width.self.height

# ********************************************************************************************* 
# class Car:
#     color=None

# def change_color(car,color):
#     car.color=color

# car_one=Car()
# car_two=Car()

# change_color(car_one,(input("Your car one color?- ")))
# change_color(car_two,(input("Your car two color?- ")))

# print("Your car one colour is",car_one.color)
# print("Your car two colour is",car_two.color)

# ********************************************************************************************* 

# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))
# z = float(input("Enter third number: "))

# add = lambda x, y, z: x + y + z
# multiply = lambda x, y, z: x * y * z

# add_result = add(x, y, z)
# multiply_result = multiply(x, y, z)

# print("Added result is:", add_result)
# print("Multiplied result is:", multiply_result)

# ********************************************************************************************* 
# row_input = int(input("Enter the number of rows:"))
# column_input = int(input("Enter the number of columns:"))
# user_list = [[(input("Enter your items-")) for x in range (column_input)] for y in range(row_input)]
# print("Your produced list is-", user_list)

# to_taka=lambda data:(data[1])*(100)

# tk_show=list(map(to_taka,user_list))

# for x in tk_show:
#     print("Loading")
#     time.sleep(2)
#     print("Price of your items are- ",x)

# custom_question= input("Do you wanna filter?- ").lower()
# if custom_question=="yes":
#     cost_one=lambda data:data[1]<=1000
#     low_cost=(filter(cost_one,tk_show))
#     for i in low_cost:
#         print("Low cost items are-",i) 
#     cost_two=lambda data:data[1]>1000
#     high_cost=(filter(cost_two,tk_show))
#     for i in high_cost:
#         print("High cost items are-", i)
# else:
#     print("Goodbye then")
    
    
# ********************************************************************************************* 
# random_numbers_input = input("Give inputs of list separated by commas: ")
# store_numbers = random_numbers_input.split(',')

# given_string = input("Grade? Money? Price? - ").lower()

# if given_string == "grade":
#     good_grades = [x if int(x) >= 50 else ("You failed",x) for x in store_numbers]
#     print(good_grades)
#     #can be customized later
# ********************************************************************************************* 

def main():
    x=input("Write something- ")
    print(x)

if __name__=="__main__":
    main()











    
            


        
    
    



    





        
# *********************************************************************************************
# # calling functions
# name_fun(input("Enter password to login-"))
# guess_number(input("Enter your GOAT name- "))
# for_loop()
# nested_loops(int(input("Enter your row numbers- ")),int(input("Enter your column numbers- ")))
# state_fun((input("Please enter phone no with country code- ")),(input("Enter your favourite numbers- ")),(input("Enter your favourite club- ")))
# list_fun()
# try_except()
# file_fun()
# game_hand()

