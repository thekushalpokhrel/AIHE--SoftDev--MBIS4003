#hangman game
import random
word = ['Cesar', 'America', 'Kushal', 'German', 'Coding', 'Rocks']
randWord = random.choice(word)
count = 0
gList = []

print()
print("---------------------------- Software Development ----------------------------------")
print("This is Hangman program presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("---------------------------- AIH Higher Education ----------------------------------")
print()
print("\nHangman Game Start")
while True: #ask to input repeatedly
    g1 = str(input("Input a letter:  "))
    g1 = g1.lower()
    if g1 not in gList:
        if g1 in randWord:  #checks input if random words
            print("Ok, Good. Try Next One")
        else:                          
            count += 1
            print("Sorry, Attempt: %d" % count)
            if count > 5:                   
                print("Max Attempt Reached")
                print("You Lose")
                break            
    else:
        print("Input Already Given {}. Once More ?".format(g1))
        print(set(gList))
        
    gList.append(g1)