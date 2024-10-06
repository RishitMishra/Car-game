from threading import Timer
import random as ra
import time

def car_crashed():
    print("Car crashed!")
    while True:
        try_again = input("Do you want to try again? (Y/N)\n>").strip().upper()
        if try_again == "Y":
            maingame()
            break
        elif try_again == "N":
            print("Thank you for playing!")
            return
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

def maingame():
    difficulty = input('''Enter difficulty (Easy, Normal, Hard):\n>''').strip().upper()
    if difficulty == "EASY":
        t = 7.0
    elif difficulty == "NORMAL":
        t = 5.0
    elif difficulty == "HARD":
        t = 3.0
    else:
        print("Invalid difficulty. Defaulting to Normal.")
        t = 5.0
    
    current_lane = 1
    max_rounds = 10
    print("Car started")
    
    for round_num in range(max_rounds):
        sle = ra.uniform(t, t + 3.0)
        countdown = Timer(t, car_crashed)
        time.sleep(sle)
        countdown.start()

        command = input("A boulder is coming!!!!\n>").strip().upper()
        countdown.cancel()

        if command == "R":
            current_lane += 1
        elif command == "L":
            current_lane -= 1
        elif command == "STOP":
            print("Thank you for playing!")
            return
        elif command == "B":
            pause_game()
        else:
            print("Invalid choice! You crashed.")
            car_crashed()
            return

        if current_lane < 0 or current_lane > 2:
            print("Went off road!")
            car_crashed()
            return

        t = max(1.0, t - 0.2)  # Decrease timer for increasing difficulty
    
    print("Congratulations! You win!")
    print("You definitely ride it well ;)")

def pause_game():
    print("Car stopped!")
    while True:
        command = input(">").strip().upper()
        if command == "START":
            print("Car started!")
            return
        elif command == "STOP":
            print("Thank you for playing!")
            exit()
        elif command == "HELP":
            print('''
            Instructions:
            - R to move to the right lane
            - L to move to the left lane
            - STOP to quit the game
            - B to pause the game
            ''')
        else:
            print("Invalid choice. Enter 'START' to resume or 'HELP' for instructions.")

def game_start():
    print('''Welcome to the Car Game!
    Instructions:
    - There are three lanes: left, center, and right.
    - A boulder will appear randomly.
    - Use 'L' to move left, 'R' to move right.
    - If you fail to move in time, you will crash.
    - Enter 'B' to pause, 'STOP' to quit, and 'HELP' for more instructions.
    ''')
    
    while True:
        command = input(">").strip().upper()
        if command == "START":
            maingame()
            break
        else:
            print("Car is idle. Enter 'START' to begin.")

if __name__ == "__main__":
    game_start()
