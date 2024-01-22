face = ""
cont = ""

def path1(facing):
    global face
    global cont
    face = facing
    if (face == "north"):
        f1()
        from .p2 import path2
        if (cont == "yes"):
            print("\n Okay! You continue on the path.")
            path2("north")
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    if (face == "south"):
        f2()
        from .p2 import path2
        if (cont == "yes"):
            print("\n Okay! You continue on the path.")
            path2("north")
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    else : 
        return("Error")
def f1():
        global cont
        f = input("\n You appear to be at the center of a hedge maze. There is a path ahead, and impassable hedges on all other sides. Continue down the path? ")
        cont = f.lower()

def f2():
        global cont
        f = input("\n You arrive at a dead end. There is a path behind you, and impassable hedges on all other sides. Turn down the path behind you? ")
        cont = f.lower()

def loop1():
     path1(face.lower())