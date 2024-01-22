face = ""
cont = ""

def path2(facing):
    global face
    global cont1
    face = facing
    if (face == "north"):
        f3()
        from .p1 import path1
        if (cont1 == "back"):
            print("Okay! You turn back and head down the path.")
            face = "south"
            path1(face)
        elif (cont1 == "left"):
             print("p4")
             loop2()
        elif (cont1 == "right"):
             print("p3")
             loop2()
        elif (cont1 == "quit"):
             exit()
        else :
            print("Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop2()
    elif (face == "west"):
        f4()
        if (cont1 == "left"):
            print("Okay! You continue on the path.")
            face = "south"
            path1(face)
        elif (cont1 == "quit"):
             exit()
        else :
            print("Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop2()
    
    elif (face == "east"):
        f5()
        if (cont1 == "right"):
            print("Okay! You continue on the path.")
            face = "south"
            path1(face)
        elif (cont1 == "quit"):
             exit()
        else :
            print("Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop2()
    else : 
        return("Error")
def f3():
        global cont1
        f = input("You arrive at a 'T' junction. The path continues to the LEFT and to the RIGHT. There is also a path BACK. Where will you go? ")
        cont1 = f.lower()

def f4():
        global cont1
        f = input("You arrive at a 'T' junction. The path continues FORWARD and BACK. There is also a path to the LEFT. Where will you go? ")
        cont1 = f.lower()

def f5():
        global cont1
        f = input("You arrive at a 'T' junction. The path continues FORWARD and BACK. There is also a path to the RIGHT. Where will you go? ")
        cont1 = f.lower()

def loop2():
     path2(face.lower())