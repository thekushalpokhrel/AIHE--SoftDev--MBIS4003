# Random Lottery Game
import random

victor = ['Cesar', 'Kushal', 'Suman', 'Garry', 'Harry', 'Monica', 'Pablo', 'Rodrigo', 'Milano', 'Titan', 'Rancho', 'Peter', 'Lola', 'Harrison']
print()
print("---------------------------- Software Development ----------------------------------")
print("This is Lottery Program presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("---------------------------- AIH Higher Education ----------------------------------")
print()
print("Lets Play Lottery")
print()
print("\nList of Lottery Players:\nCesar\nKushal\nSuman\nGarry\nHarry\nMonica\nPablo\nRodrigo\nMilano\nTitan\nRancho\nPeter\nLola\nHarrison\n")
ans = input('\nGuess, Which player is the winner: ')
if ans == random.choice(victor):
    print("What a guess, youre a champion thats correct", ans, "is the winner")
else:
    print('\nBad Guess, And the winner is', random.choice(victor))
