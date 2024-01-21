def paths(facing):
    if (facing == "north"):
        if (f1() == "yes"):
            return("Okay! You continue on the path.")
        else :
            return("Sorry, I didn't understand. Perhaps this isn't possible here? \n" + b1())
    else : 
        return("Error")
def f1():
        f = input("You appear to be at the center of a hedge maze. There is a path ahead, and impassable hedges on all other sides. Continue down the path? ")
        return(f.lower())