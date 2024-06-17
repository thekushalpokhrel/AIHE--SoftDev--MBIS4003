#Arcade Mixgame program three levels 1,2,3
import random
import matplotlib.pyplot as plt
import statistics
import numpy as np
#define global variables
#levelwise quiz result
correct1=0 #level 1 correct result
incorrect1=0 #level 1 incorrect result
correct2=0 #level 2 correct result
incorrect2=0 #level 2 incorrect result
correct3=0 #level 3 correct result
incorrect3=0 #level 3 incorrect result
#create a logo of game by iteration-------------
for i in range(1,6):
    for j in range(6,-i):
        print(" " , end = " ")
    for j in range(1,i):
        print(random.choice(['A','X','O','Y']), end =" ")
    for j in range(i,0,-1):
        print('A', end= " ")
    for j in range(i,1,-2):
        print('Z', end= " ")
    print()
#print name of the game as mix and match cards game--------
print("---------------------------- Software Development ----------------------------------")
print("This is Arcade Mix Game Program presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("---------------------------- AIH Higher Education ----------------------------------")
print()
print("*"*20+'Welcome To Arcade Mix Games'+"*"*20+'\n')
print('There are three levels to the game')
print('Pass each game to move to next round')
for i in range(8):
    for j in range(i+2):
        print(" " ,end = " ")
    for j in range(1,7-i):
        print('G',end= " " )
    for j in range(5-i,0,-1):
        print(random.choice(['S','E','K','Q']),end = " ")
    for j in range(3-i,0,-1):
        print('X',end = " ")
    print()
print()
#function is used to create a 3 levels of game
def three_levels(que_bank_lev1,que_bank_lev2,que_bank_lev3):
    #define local variables
    correct1=0
    incorrect1=0
    correct2=0
    incorrect2=0
    correct3=0
    incorrect3=0   
    print("\nLevel 1\n")
    #random question selection
    for i in range(5):
        print()
        q1=random.choice(que_bank_lev1)
        ans1=input(q1)#ask que
        #checking answer of que
        if ans1.lower()== ans_bank_lev1[q1]:
            correct1=correct1+1
        else:
            incorrect1=incorrect1+1
    #condition for checking finishing of level
    if correct1<3:
        print('\nIncorrect answer')
        print('Sorry you lose the game!!!')        
    else:
        print('\nYou have cleared this level!!!\n')         
        print("\nLevel 2\n")
        #random question selection
        for i in range(5):
            q1=random.choice(que_bank_lev2)
            ans2=input(q1) #ask que
            print()
            #checking answer of que
            if ans2== ans_bank_lev2[q1]:
                correct2=correct2+1
            else:
                incorrect2=incorrect2+1
        #condition for checking finishing of level
        if correct2<3:
            print('\nIncorrect answer')
            print('Sorry you lose the game!!!')
            
        else:
            print('\nYou have cleared this level!!!\n') 
            
            print("\nLevel 3\n")

            #random question selection
            for i in range(5):
                q1=random.choice(que_bank_lev3)
                ans3=input(q1) #ask que
                print()

                #checking answer of que
                if ans3.lower()== ans_bank_lev3[q1]:
                    correct3=correct3+1
                else:
                    incorrect3=incorrect3+1

            #condition for checking finishing of level
            if correct3<3:
                print('\nIncorrect answer')
                print('Sorry you lose the game!!!')

            else:
                print('\nCongrats!! You have cleared this level!!!\n')
            
    return correct1,incorrect1,correct2,incorrect2,correct3,incorrect3

#main program
player=input('\nEnter your name: ') #ask player name

#questions for different level
que_bank_lev1=['What is the opposite of serious? ',
               'What is the opposite of victory? ',
               'What is the opposite of sick? ',
               'What is the opposite of fall? ',
               'What is the opposite of begin? ',
               'What is the opposite of move? ',
               'What is the opposite of clever? ',
               'What is the opposite of bright? ',
               'What is the opposite of melt? ',
               'What is the opposite of Amateur? ',
               'What is the opposite of happy?']

que_bank_lev2=['What is the palindrome of malayalam? ',
               'What is the palindrome of tenet? ',
               'Are Civic and India words palindrome? Y/N ',
               'Are Madam and Malayalam words palindrome? Y/N ',
               'Is noon a palindrome? Y/N ',
               'Is gig a palindrome? Y/N ',
               'Are madam and noon palindrome? Y/N ',
               'What is the palindrome of nun? ',
               'Arrange the letters r,e and d in palindrome word ',
               'Arrange the letters d and e in palindrome word ']


que_bank_lev3=['Create a word from r,t ant o? ',
               'Create a word from a,u,n and l? ',
               'Create a word from b and i? ',
               'Create a word from a, e and t? ',
               'Create a word from d, r and e? ',
               'Create a word from u,l,n,f,i and y? ',
               'Create a word from t,u,s and o? ',
               'Create a word from q,e and u? ',
               'Create a word from r, y and w? ',
               'Create a word from s,o,l,c, u and a? ']

#answers of questions of different levels
ans_bank_lev1={'What is the opposite of serious? ':'funny',
               'What is the opposite of victory? ':'defeat',
               'What is the opposite of sick? ':'healthy',
               'What is the opposite of fall? ':'balance',
               'What is the opposite of begin? ':'finish',
               'What is the opposite of move? ':'stop',
               'What is the opposite of clever? ':'stupid',
               'What is the opposite of bright? ':'dark',
               'What is the opposite of melt? ':'freeze',
               'What is the opposite of Amateur? ':'professional',
               'What is the opposite of happy? ': 'sad'}

ans_bank_lev2={'What is the palindrome of malayalam? ':'malayalam',
               'What is the palindrome of tenet? ':'tenet',
               'Are Civic and India words palindrome? Y/N ':'N',
               'Are Madam and Malayalam words palindrome? Y/N ':'N',
               'Is noon word palindrome? Y/N ':'Y',
               'Is gig word palindrome? Y/N ':'Y',
               'Are madam and noon words palindrome? Y/N ':'Y',
               'What is the palindrome of nun? ':'nun',
               'Arrange the letters r,e and d in palindrome word ':'redder',
               'Arrange the letters d and e in palindrome word ':'deed'}


ans_bank_lev3={'Create a word from r,t ant o? ':'root',
               'Create a word from a,u,n and l? ' :'annual',
               'Create a word from b and i? ':'bibi',
               'Create a word from a, e and t? ':'ate',
               'Create a word from d, r and e? ':'red',
               'Create a word from u,l,n,f,i and y? ' :'nullify',
               'Create a word from f,u, and s? ':'fuss',
               'Create a word from q,e and u? ':'queue',
               'Create a word from r, y and w? ':'wry',
               'Create a word from s,o,l,c, u and a? ':'callous'}

c1,inc1,c2,in2,c3,inc3=three_levels(que_bank_lev1,que_bank_lev2,que_bank_lev3) #call function

#ask question for viewing analysis of game
analysis=input('\nLets see game analysis? Y/N ')

if analysis=='Y':

    levels=['Level 1','Level 2','Level 3']
    
    #calculating the score of levels
    l1_score= c1*10
    l2_score= c2*10
    l3_score= c3*10
    level_score=[l1_score,l2_score,l3_score]

    #plot bar chart      
    plt.bar(levels,level_score,color='blue',edgecolor='black')
    plt.title('\t\tLevel Wise Scores',fontsize=16) #add title
    plt.xlabel('Levels')#set x-axis label
    plt.ylabel('Scores')#set y-axis label
    plt.show()

    print('\nDescriptive Stats Score:')
    #find mean value
    print('\nMean: ',statistics.mean(level_score))

    #find median value
    print('\nMediand: ',statistics.median(level_score))

    #Mode calculation

    #create NumPy array of values with only one mode
    x = np.array(level_score)

    #find unique values in array along with their counts
    vals, counts = np.unique(x, return_counts=True)

    #find mode
    mode_value = np.argwhere(counts == np.max(counts))

    print('\nMode: ',vals[mode_value].flatten().tolist())

    #find variance
    print('\nVariance: ',np.var(level_score))

    #find standard deviation
    print('\nStandard Deviation: ',statistics.stdev(level_score))

print('\nThanks for Playing!!!')   
            


        

















