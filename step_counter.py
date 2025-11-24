import random
import time

"""
This is my step counter program 
It pretends like you are walking and counts your steps
It also tells you how many calories you burned
Sometimes it gives you nice messages to keep you going
"""

print("My Step Counter Program ")
print("Hi! This program will act like you are walking and count your steps.")
print()

''' Ask for the user's name'''
name = input("What is your name? ")
'''Ask for user goal for the day'''
goal = input("How many steps do you want to walk today? ")

"""
I need to make sure the step goal is a number
If it's not a number, the program will crash
So I use try and except to catch the error
"""
try:
    goal = int(goal)
except:
    print("Oops! You need to enter a number for the steps. Please try again.")
    exit()

print()
print("Okay " + name + "! Let's start walking! ")
print("I'm counting your steps now... (if you want to stop, press CTRL + C)")
print()

'''These variables keep track of everything'''
steps = 0
calories = 0

"""
I made a list of happy messages to show while walking
The program will pick one randomly sometimes
I think this makes it more fun
"""
motivation_quotes = [
    "You're doing great! Keep going! ",
    "Every step makes you healthier! ",
    "Wow, you're amazing! ",
    "Don't stop now! You can do it! ",
    "You're walking so fast! ",
    "Your body will thank you later! "
]

"""
This is the main part that does the counting
It keeps adding steps until we reach the goal
Or until the user stops it
"""
try:
    while steps < goal:
        
        new_steps = random.randint(5, 25)
        steps += new_steps
        # It calculate calories 
        calories += new_steps * 0.04

        # Don't go over the goal
        if steps > goal:
            steps = goal

        # Its shows how many steps remains to walk
        print("Steps so far:", steps)

        """
        Sometimes show a happy message
        I set it to 35% chance each time
        So about 1 out of 3 times it shows a message
        """
        if random.random() < 0.35:
            print(random.choice(motivation_quotes))

        '''it will take 0.5 seconds to add new input'''
        time.sleep(0.5)

    """
    When we finish all the steps, show success message
    This part runs when the while loop ends
    """
    print()
    print("Yay! You did it!")
    print("Total steps walked:", steps)
    print("Calories burned:", round(calories, 2))

except KeyboardInterrupt:
    """
    This part runs if the user presses CTRL+C
    It means they want to stop early
    """
    print()
    print("You stopped walking early")
    print("You walked this many steps:", steps)
    print("You burned this many calories:", round(calories, 2))



