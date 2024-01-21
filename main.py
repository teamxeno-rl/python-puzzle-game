import World.main.strt as main

start = input("Hello! Would you like to start? ")
num = 0

if(start.lower() == "yes") :
    print(main.start())

else :
    print("error in main.py")
    exit()