class my_room:
    
    def __init__(self,room,colour,built,person):
        self.room=room
        self.colour=colour
        self.built=built
        self.person=person


    def newPerson(self):
        user_input=input("Whats your name?- ")

        if user_input=="Nabil" :
            print("This is your room so enjoy")
        else:
            print("Welcome to my room")
    
    def oldPerson(self):
        print("You are also welcome even though you are old")

person_one=my_room("big","red",2019,"nabil")

print(person_one.built)

