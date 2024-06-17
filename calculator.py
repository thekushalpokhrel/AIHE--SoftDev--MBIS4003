#Calculator Program
#import libraries
import random
import pandas as pd
import matplotlib.pyplot as plt

#define global variables
loop_again1='yes' #variable used to continue first loop
numbers=[]
correct_choice=['Super Work!','Nicely Done!','Keep Up', 'Well Done'] #correct result responses
incorrect_choice=['Please Try Again.','Try Once More','Keep Trying', 'Sorry Mate'] #incorrect result responses

student_names=[] #student name list
que_num_list=[] #question number list
ans_list=[] #answer list

Total_add_que=[] #add question count list for all students
Total_sub_que=[] #sub question count list for all students
Total_mul_que=[] #mul question count list for all students
Total_div_que=[] #div question count list for all students
Total_mix_que=[] #mix question count list for all students

Total_correct_add_all=[] #add correct question count list for all students
Total_incorrect_add_all=[] #add incorrect question count list for all students

Total_correct_sub_all=[] #sub correct question count list for all students
Total_incorrect_sub_all=[] #sub incorrect question count list for all students

Total_correct_mul_all=[] #mul correct question count list for all students
Total_incorrect_mul_all=[] #mul incorrect question count list for all students

Total_correct_div_all=[] #div correct question count list for all students
Total_incorrect_div_all=[] #div incorrect question count list for all students

Total_correct_mix_all=[] #mix correct question count list for all students
Total_incorrect_mix_all=[] #mix incorrect question count list for all students

#random number generator function
rand_numbers=[]#variable used to collect random numbers
def take_rand_numbers(n):
    rand_numbers=[]
    #loop used to generate random numbers from 1,8
    for i in range(n):
        num=random.randint(1,9)
        rand_numbers.append(num)
    return tuple(rand_numbers)#convert random numbers list into tuple

#mix question generator
def mix_que_generator(n1,n2,n3,n4,n5):
    symbol=['+','-','*','/'] #all options
    s1=random.choice(symbol) # random option selection
    s2=random.choice(symbol) # random option selection
    s3=random.choice(symbol) # random option selection
    s4=random.choice(symbol) # random option selection
    que1="\nWhat is the result of "+str(n1)+s1+str(n2)+s2+str(n3)+s3+str(n4)+s4+str(n5)+'? '

    r1=0 #result variable
    #condition of different option selection for each position of question
    if s1=='+':
        r1=n1+n2
    elif s1=='-':
        r1=n1-n2
    elif s1=='*':
        r1=n1*n2
    else:
        r1=n1/n2

    if s2=='+':
        r1=r1+n3
    elif s2=='-':
        r1=r1-n3
    elif s2=='*':
        r1=r1*n3
    else:
        r1=r1/n3

    if s3=='+':
        r1=r1+n4
    elif s3=='-':
        r1=r1-n4
    elif s3=='*':
        r1=r1*n4
    else:
        r1=r1/n4

    if s4=='+':
        r1=r1+n5
    elif s4=='-':
        r1=r1-n5
    elif s4=='*':
        r1=r1*n5
    else:
        r1=r1/n5

    result = r1   #result of mix equation
    return result, que1
    
#question generator
def que_generator(n,option):
    if n == 2:
        n1,n2=take_rand_numbers(n) # call function to get random numbers
        que1="\nWhat is the "+option+" of "+str(n1)+" and "+str(n2)+"? "
        if option == 'sum':
            result = n1 + n2 # result calculation of given question
            try:
                ans=int(input(que1)) #ask question
            except:
                print("Answer should be integer")
        elif option == 'substraction':
            result = n1 - n2 # result calculation of given question
            try:
                ans=int(input(que1)) #ask question
            except:
                print("Answer should be integer")
        elif option == 'multiplication':
            result = n1 * n2 # result calculation of given question
            try:
                ans=int(input(que1)) #ask question
            except:
                print("Answer should be integer")
        elif option == 'division':
            que1="\nWhat is the "+option+" of "+str(n1)+" by "+str(n2)+"? "
            result = n1 / n2 # result calculation of given question
            try:
                ans=input(que1) #ask question
            except:
                print("Answer should be in decimal form")
    else:
        n1,n2,n3,n4,n5=take_rand_numbers(5) # call function to get random numbers
        if option == 'mix':
            result,que1=mix_que_generator(n1,n2,n3,n4,n5)
            try:
                ans=input(que1) #ask question
            except:
                print("Answer should be in decimal form")

    return result,ans,que1
        

# calculator function used to generate calculation results
def user_calci(user):
    print('')
    print("=========================== Welcome to the Calculator Game ==============================")
    print()

    #local variables for total number of questions
    i=0 #total add questions
    j=0 #total sub questions
    k=0 #total mul questions
    l=0 #total div questions
    m=0 #total mix questions

    #local variables for counting total correct and incorrect questions
    Total_correct_add=0 #total add correct questions
    Total_incorrect_add=0 #total add incorrect questions

    Total_correct_sub=0 #total sub correct questions
    Total_incorrect_sub=0 #total sub incorrect questions

    Total_correct_mul=0 #total mul correct questions
    Total_incorrect_mul=0 #total mul incorrect questions

    Total_correct_div=0 #total div correct questions
    Total_incorrect_div=0 #total div incorrect questions
 
    Total_correct_mix=0 #total mix correct questions
    Total_incorrect_mix=0 #total mix incorrect questions

    while loop_again1=='yes':
        #menu options
        print('Choose any options from below:')
        print('\n1 Addition problems\n2 Subtraction problems\n3 Multiplication problems\n4 Division problems\n5 Random mixture of all these\n6 Exit')

        #menu option selection
        choice=int(input('Enter your option : '))

        #condition for selection of add option
        if choice == 1:
            i=i+1 #count total add questions
            result,ans,que1=que_generator(2,'sum')
            repeat_que=que1
            repeat_result=result
            loop_again2='yes' #repeat loop variable for wrong question
            while loop_again2=='yes':
                if ans == result:
                    Total_correct_add=Total_correct_add+1 #count correct add questions
                    que_num_list.append('add_correct'+ str(i))
                    ans_list.append('add_correct'+str(i))
                    #correct answer response selection
                    n=random.randint(1,3)
                    print(correct_choice[n-1])
                    break
  
                else:
                    Total_incorrect_add=Total_incorrect_add+1 #count incorrect add questions
                    que_num_list.append('add_incorrect'+str(i))
                    ans_list.append('add_incorrect'+str(i))
                    #incorrect answer response selection
                    n=random.randint(1,3)
                    print(incorrect_choice[n-1])
                    #repeat wrong question
                    ans=int(input(repeat_que))
                    result = repeat_result
                    loop_again2= 'yes'

        #condition for selection of sub option
        elif choice == 2:
            j=j+1 #count total sub questions
            result,ans,que1=que_generator(2,'substraction')
            repeat_que=que1
            repeat_result=result
            loop_again2='yes' #repeat loop variable for wrong question
            while loop_again2=='yes':
                if ans == result:
                    Total_correct_sub=Total_correct_sub+1 #count correct sub questions
                    que_num_list.append('sub_correct'+ str(j))
                    ans_list.append('sub_correct'+str(j))
                    #correct answer response selection
                    n=random.randint(1,3)
                    print(correct_choice[n-1])
                    break

                else:
                    Total_incorrect_sub=Total_incorrect_sub+1 #count incorrect sub questions
                    que_num_list.append('sub_incorrect'+str(j))
                    ans_list.append('sub_incorrect'+str(j))
                    #incorrect answer response selection
                    n=random.randint(1,3)
                    print(incorrect_choice[n-1])
                    #repeat wrong question
                    ans=int(input(repeat_que))
                    result = repeat_result
                    loop_again2= 'yes'

        #condition for selection of mul option
        elif choice == 3:
            k=k+1 #count total mul questions
            result,ans,que1=que_generator(2,'multiplication')
            repeat_que=que1
            repeat_result=result
            loop_again2='yes' #repeat loop variable for wrong question
            while loop_again2=='yes':
                if ans == result:
                    Total_correct_mul=Total_correct_mul+1 #count correct mul questions
                    que_num_list.append('mul_correct'+ str(k))
                    ans_list.append('mul_correct'+str(k))
                    #correct answer response selection
                    n=random.randint(1,3)
                    print(correct_choice[n-1])
                    break

                else:
                    Total_incorrect_mul=Total_incorrect_mul+1 #count incorrect mul questions
                    que_num_list.append('mul_incorrect'+str(k))
                    ans_list.append('mul_incorrect'+str(k))
                    #incorrect answer response selection
                    n=random.randint(1,3)
                    print(incorrect_choice[n-1])
                    #repeat wrong question
                    ans=int(input(repeat_que))
                    result = repeat_result
                    loop_again2= 'yes'            

        #condition for selection of div option
        elif choice == 4:
            l=l+1 #count total div questions
            result,ans,que1=que_generator(2,'division')
            repeat_que=que1
            repeat_result=result
            ans=float("{:.2f}".format(float(ans)))
            result=float("{:.2f}".format(result))
            loop_again2='yes' #repeat loop variable for wrong question
            while loop_again2=='yes':
                if ans == result:
                    Total_correct_div=Total_correct_div+1 #count correct div questions
                    que_num_list.append('div_correct'+ str(l))
                    ans_list.append('div_correct'+str(l))
                    #correct answer response selection
                    n=random.randint(1,3)
                    print(correct_choice[n-1])
                    break
  
                else:
                    Total_incorrect_div=Total_incorrect_div+1 #count incorrect div questions
                    que_num_list.append('div_incorrect'+str(l))
                    ans_list.append('div_incorrect'+str(l))
                    #incorrect answer response selection
                    n=random.randint(1,3)
                    print(incorrect_choice[n-1])
                    #repeat wrong question
                    ans= input(repeat_que)
                    result = repeat_result
                    ans=float("{:.2f}".format(float(ans)))
                    result=float("{:.2f}".format(result))
                    loop_again2= 'yes'             

        #condition for selection of mix option
        elif choice == 5:
            m=m+1 #count total mix questions
            result,ans,que1=que_generator(5,'mix')
            repeat_que=que1
            repeat_result=result
            ans=float("{:.1f}".format(float(ans)))
            result=float("{:.1f}".format(result))
            loop_again2='yes' #repeat loop variable for wrong question
            while loop_again2=='yes':
                if ans == result:
                    Total_correct_mix=Total_correct_mix+1 #count correct mix questions
                    que_num_list.append('mix_correct'+ str(m))
                    ans_list.append('mix_correct'+str(m))
                    #correct answer response selection
                    n=random.randint(1,3)
                    print(correct_choice[n-1])
                    break

                else:
                    Total_incorrect_mix=Total_incorrect_mix+1 #count incorrect mix questions
                    que_num_list.append('mix_incorrect'+str(m))
                    ans_list.append('mix_incorrect'+str(m))
                    #incorrect answer response selection
                    n=random.randint(1,3)
                    print(incorrect_choice[n-1])
                    #repeat wrong question
                    ans= input(repeat_que)
                    result = repeat_result
                    ans=float("{:.2f}".format(float(ans)))
                    result=float("{:.2f}".format(result))
                    loop_again2= 'yes'          

        #condition for selection of exit option
        elif choice == 6:
            break

        #condition for selection of invalid option
        else:
            print('\nInvalid option selection.')
            
    #add the count of questions for each user
    Total_add_que.append(i)
    Total_sub_que.append(j)
    Total_mul_que.append(k)
    Total_div_que.append(l)
    Total_mix_que.append(m)

    #add the count of correct and incorrect questions for each user
    Total_correct_add_all.append(Total_correct_add)
    Total_incorrect_add_all.append(Total_incorrect_add)

    Total_correct_sub_all.append(Total_correct_sub)
    Total_incorrect_sub_all.append(Total_incorrect_sub)

    Total_correct_mul_all.append(Total_correct_mul)
    Total_incorrect_mul_all.append(Total_incorrect_mul)

    Total_correct_div_all.append(Total_correct_div)
    Total_incorrect_div_all.append(Total_incorrect_div)

    Total_correct_mix_all.append(Total_correct_mix)
    Total_incorrect_mix_all.append(Total_incorrect_mix)

    #ask to display chart for single user
    ask=input('\nDo you want to display chart for this student (Yes/No)? ')
    if ask == 'Yes':
        #Create a Dictionary of series for single user
        d = {'User':pd.Series(student,),'Total_add_que':pd.Series([i,]),'Total_correct_add':pd.Series([Total_correct_add,]),
             'Total_incorrect_add':pd.Series([Total_incorrect_add,]),
             
             'Total_sub_que':pd.Series([j,]),'Total_correct_sub':pd.Series([Total_correct_sub,]),
             'Total_incorrect_sub':pd.Series([Total_incorrect_sub,]),
             
             'Total_mul_que':pd.Series([k,]),'Total_correct_mul':pd.Series([Total_correct_mul,]),
             'Total_incorrect_mul':pd.Series([Total_incorrect_mul,]),
             
             'Total_div_que':pd.Series([l,]),'Total_correct_div':pd.Series([Total_correct_div,]),
             'Total_incorrect_div':pd.Series([Total_incorrect_div,]),
             
             'Total_mix_que':pd.Series([m,]),'Total_correct_mix':pd.Series([Total_correct_mix,]),
             'Total_incorrect_mix':pd.Series([Total_incorrect_mix,])}

        #print(d)

        #create dataframe for single student
        single_student_data = pd.DataFrame(d)
        #print(single_student_data)

        #find statistical analysis for single student
        print("\nStatistical analysis of "+user+" data: ")
        print(single_student_data.describe())

        #draw chart for single student
        single_student_data.plot.bar()
        title_msg= user+"'s Test Analysis Chart"
        plt.title(title_msg) #title of chart
        plt.show()
print()
print("-------------------------------- Software Development ----------------------------------")
print("This is Calculator Game presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("-------------------------------- AIH Higher Education ----------------------------------")
print()
number_of_student=int(input('\nEnter the number of students who plays: ')) #ask number of students

#loop used to find the questions for each student
for i in range(number_of_student):
    student=input('\nEnter the student name: ') #enter student name
    print('\nWelcome ',student)

    #add student name to create chart of all students
    student_names.append(student)
    user_calci(student)#call calculator function for calculation

#ask user to create a chart of all students
ask=input('\nDo you want to display the chart for all the students (Yes/No)? ')
if ask == 'Yes':
    #Create a Dictionary of series for all students
    d = {'User':pd.Series(student_names),'Total_add_que':pd.Series(Total_add_que),'Total_correct_add':pd.Series(Total_correct_add_all),
         'Total_incorrect_add':pd.Series(Total_incorrect_add_all),
         
         'Total_sub_que':pd.Series(Total_sub_que),'Total_correct_sub':pd.Series(Total_correct_sub_all),
         'Total_incorrect_sub':pd.Series(Total_incorrect_sub_all),
         
         'Total_mul_que':pd.Series(Total_mul_que),'Total_correct_mul':pd.Series(Total_correct_mul_all),
         'Total_incorrect_mul':pd.Series(Total_incorrect_mul_all),
         
         'Total_div_que':pd.Series(Total_div_que),'Total_correct_div':pd.Series(Total_correct_div_all),
         'Total_incorrect_div':pd.Series(Total_incorrect_div_all),
         
         'Total_mix_que':pd.Series(Total_mix_que),'Total_correct_mix':pd.Series(Total_correct_mix_all),
         'Total_incorrect_mix':pd.Series(Total_incorrect_mix_all)}

    #print(d)

    #create dataframe for all students
    all_student_data = pd.DataFrame(d)
    #print(all_student_data)

    #find statistical analysis of all students
    print("\nStatistical analysis of all the student's data: ")
    print(all_student_data.describe())

    #draw chart for all students
    all_student_data.plot.bar()
    plt.title("All Student's Analysis Chart") #title of chart
    plt.show()

else:
    print('\nThanks for using this calculator!!!') #exit message

