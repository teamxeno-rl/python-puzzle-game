face = ""
cont = ""

def path3(facing):
    global face
    global cont
    face = facing
    if (face == "east"):
        f1()
        from .p2 import path2
        if (cont == "back"):
            print("\n Okay! You turn back and head down the path.")
            face = "west"
            path2(face)
        elif (cont == "forward"):
             print("\n Okay! You continue up the path.")
             print("\n p5")
             loop1()
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    elif (face == "west"):
        f1()
        from .p2 import path2
        if (cont == "back"):
            print("\n Okay! You turn back down the path.")
            print("\n p5")
        elif (cont == "forward"):
             print("\n Okay! You continue up the path.")
             face = "west"
             path2(face)
        elif (cont == "quit"):
             exit()
        else :
            print("\n Sorry, I didn't understand. Perhaps this isn't possible here? \n")
            loop1()
    else : 
        return("Error")
def f1():
        global cont
        f = input("\n The path continues both FORWARD and BACK. Where will you go? ")
        cont = f.lower()

def loop1():
     path3(face.lower())