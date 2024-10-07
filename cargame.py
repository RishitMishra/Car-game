from threading import Timer
import random as ra
import time

sle = None
countdown = None
midlane = None
leftlane = None
rightlane = None
currentlane = None 
i = None
t = None
def car_crashed():
    print("Car crashed!")
    while True:
        time.sleep(1.0)
        tryaga = input("Do you want to Try again?(Y/N)\n>")
        if tryaga == "Y":
            maingame()
            break
        elif tryaga == "N":
            print("Thank you for playing")
            exit()
        else:
            print("Invalid choice\n.\n.\n.\n")

def game_process():
    global sle , countdown , currentlane , middlelane , rightlane , leftlane , i , t
    time.sleep(sle)
    Timer.start(countdown)
    command = str(input("A boulder is coming!!!!\n>"))
    if command.upper() == "R":
        currentlane += 1 
        Timer.cancel(countdown)
        t -= 0.2
        i += 1
        if currentlane != leftlane and currentlane != rightlane:
            print("Went off road!")
            car_crashed()
            
    elif command.upper() == "L":
        currentlane -= 1
        Timer.cancel(countdown)
        t -= 0.2
        i += 1
        if currentlane != leftlane and currentlane != rightlane:
            print("Went off road!")
            car_crashed()
            
    elif command.upper() == "STOP":
        print("Thank you for playing")
        exit()
    elif command.upper() == "B":            # pause menu
        print("Car stopped!")
        Timer.cancel(countdown)
        while True:
            command = str(input(">"))
            if command.upper() == "START":
                print("Car started")
                break
            elif command.upper() == "STOP":
                print("Thank you for playing")
                exit()
            elif command.upper() == "HELP":
                print('''
                There are three lanes left, centre and right
                A boulder will come randomly under or equal to 8 seconds
                You need to enter if u want to change to left lane or right lane
                If you fail to change lanes in given time (time to change lessens every level) you crash 
                If you go off the road your car crashes  
                Enter Start to start the car
                Enter Stop to stop the car
                Enter R to turn the car in right lane
                Enter L to turn the car in left lane
                
                ''')
            else:
                print("Invalid choice\n.\n.\n.\n")
    else:
        print("Invalid choice\n.\n.\n.\n")
        car_crashed()
        

       
    
def maingame():
    global sle , countdown , currentlane , middlelane , rightlane , leftlane , i , t
    diffi = str(input('''                           
    Enter difficulty -->

    Easy
    Normal
    Hard


    >'''))
    if diffi.upper() == "EASY":                         #difficulty settings
        t = 7.0
        sle = ra.choice([7.0, 7.2, 7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10.0])
    elif diffi.upper() == "NORMAL":
        t = 5.0
        sle = ra.choice([5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0])
    elif diffi.upper() == "HARD":
        t = 3.0
        sle = ra.choice([3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0])

    print("Car started")
    midlane = 1
    leftlane = 0
    rightlane = 2
    currentlane = 1 
    i = 1
    while i <= 10:
        countdown = Timer(t,car_crashed)
        if currentlane == 1:
            game_process()
        elif currentlane == 0:
            game_process()
        elif currentlane == 2:
            game_process()
    else:
        print('''.\n.\n.\n.\n.
        Congratulations!!!!
        YOU WIN!!!!!!!!!!!
        You definitely ride it well ;)
        ''')
                

                    
            


                
def game_start():
    while True:
        print('''
        There are three lanes left, centre and right
        A boulder will come randomly under or equal to 8 seconds
        You need to enter if u want to change to left lane or right lane
        If you fail to change lanes in given time (time to change lessens every level) you crash 
        If you go off the road your car crashes  
        Enter Start to start the car
        Enter Stop to stop the car
        Enter B(brake) to pause the car
        Enter R to turn the car in right lane
        Enter L to turn the car in left lane
        Enter Help while the car is stopped to read the instructions 
        ''')
        command = str(input(">"))

        if command.upper() == "START":
            maingame()
            break
        else:
            print("Car is idle")

game_start()
        
        

    
    
    