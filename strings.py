#string program
#import all libraries
import re
from collections import Counter
import string
import pandas as pd
import matplotlib.pyplot as plt
import itertools

#find frequency and all letters of enter string
def find_freq(string):
    remove = re.sub(r'[^\w\s]', '', string)#remove all special characters from string
    str_list=remove.split()#split string
    #find the frequency of letter of each word of string
    result=[]#list of letter with frequency
    for word in str_list:
        result.append(dict(Counter(word.lower())))
    result_tup=[]#list of letter with frequency in tuple form
    #create tuple from dictionary of list
    for letters in result:
	#print(letters.items())
        result_tup.append(list(letters.items()))
    return result,result_tup
    
print("---------------------------- Software Development ----------------------------------")
print("This is Strings Program presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("---------------------------- AIH Higher Education ----------------------------------")
print()
user_str=input('Enter one arbirtary string: ') #ask input from user
res1,res2=find_freq(user_str)
print('\nString letters with its frequency : ')
print(res2)


#find string has all letters or not
final_str = re.sub(r'[^\w\s]', '', user_str)
alphabet = set(string.ascii_lowercase)#take all letters of alphabet

#check alphabet of string
if set(final_str.lower()) >= alphabet :
    print('\n" '+final_str+ ' " string has all the letters of the alphabet.')
else:
    print('\n" '+final_str+ ' " string has not all the letters of the alphabet.')
    
    
# find descriptive statistics and graph of string data
          
#create a list of string data
str_data = res1	
#print(str_data)

#create dataframe for string data
df = pd.DataFrame(str_data)
#print(df)

#fill nan value with zero
df1=df.fillna(0)
#print(df1)

#find statistical analysis of string
print('\nStatistical analysis: ')
print(df1.describe())

#draw chart for string data
df1.plot.bar()
plt.title('String Data with Frequency Chart') #title of chart
plt.show()

#Sorting letters in different order and removing duplicates

#take each dictionary and add to list
all_letters=[]
for data in str_data:
    #print(data.items())
    all_letters.append(list(data.items()))

#take each item of dictionary and add into new list
final_letter_list=[]
for letters in all_letters:
    for letter in letters:
        final_letter_list.append(letter)

#sorting final list in ascending order
final_letter_list.sort()
print('\nList after sorting: ',final_letter_list)

#remove duplicates
print('\nList after removing duplicates: ',set(final_letter_list))

#sorting final list in descending order
final_letter_list.sort(reverse=True)
print('\nList after sorting: ',final_letter_list)

#remove duplicates
print('\nList after removing duplicates: ',set(final_letter_list))

#find all anagrams of a given string
perms = [''.join(perm) for perm in itertools.permutations(user_str)]

print('\nAll anagrams of '+user_str+' :')
print(perms)
