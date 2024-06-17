#guess the word game
import random

print()
print("-------------------------------- Software Development ----------------------------------")
print("This is Guess the Word Game presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("-------------------------------- AIH Higher Education ----------------------------------")
print()
print("Welocome to Guess the Word Game, Lets start !!")
n = input("Input your name? ")
print("Good Luck ! ", n) 
w = ['hardcore', 'society', 'computer', 'coding',
         'cyanide', 'maths', 'lotus', 'loophole',
         'house', 'drainage', 'telephone', 'batman']
wd = random.choice(w) 
print("Can you guess the word ?") 
guesses = ''
t = 12 #specify turns
while t > 0: #while turns is more than 0 condition
    fail = 0
    for char in wd:
        if char in guesses:
            print(char, end=" ")            
        else:
            print("_")
            print(char, end=" ")
            fail += 1
    if fail == 0:
        print("Winner Winner Chicken Dinner !!")
        break
    print()
    g = input("Can you guess the character:") #guess as g
    guesses += g #specifiy guess number 
    if g not in wd: 
        t -= 1
        print("Wrong")
        print("You have", + t, 'chances')
        if t == 0:
            print("Dont Stress, You can try better next time.")
            print("Sorry you can try later, its: ", wd)