
from .test import test
from .b1 import main as b1
from .b1 import paths 

def start():
    starter = input("You got it! First, what is your name? ")

    if (starter.lower() == "test"):
        num = input("What's the number? ")
        numsol = test.addone(num)
        return(numsol)
    
    else:
        name = starter
        msg1 = b1.entrance(name)
        print(msg1)
        face = "North"
        msg2 = paths(face.lower())
        return(msg2)

    