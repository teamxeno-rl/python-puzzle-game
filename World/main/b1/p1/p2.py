face = ""
cont = ""

def path2(facing):
    global face
    global cont
    face = facing
    if (face == "north"):
        f1()
        from .p1 import path1
        if (cont == "back"):
            print("\n Okay! You turn back and head down the path.")
            face = "south"
            path1(face)
        elif (cont == "left"):
             print("\n p4")
             loop1()
        elif (cont == "right"):
             print("\n p3")
             loop1()
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    elif (face == "west"):
        f2()
        if (cont == "left"):
            print("\n Okay! You continue on the path.")
            face = "south"
            path1(face)
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    
    elif (face == "east"):
        f3()
        if (cont == "right"):
            print("\n Okay! You continue on the path.")
            face = "south"
            path1(face)
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    else : 
        return("Error")
def f1():
        global cont
        f = input("\n You arrive at a 'T' junction. The path continues to the LEFT and to the RIGHT. There is also a path BACK. Where will you go? ")
        cont = f.lower()

def f2():
        global cont
        f = input("\n You arrive at a 'T' junction. The path continues FORWARD and BACK. There is also a path to the LEFT. Where will you go? ")
        cont = f.lower()

def f3():
        global cont
        f = input("\n You arrive at a 'T' junction. The path continues FORWARD and BACK. There is also a path to the RIGHT. Where will you go? ")
        cont = f.lower()

def loop1():
     path2(face.lower())