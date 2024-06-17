#survey program
#import libraries
import statistics
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

#predefined responses set by lecturer
responsez=[1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5] #User response list

print("---------------------------- Software Development ----------------------------------")
print("This is Survey Program presented:")
print()
print("By Kushal, Sudip and Suman")
print()
print("To Cesar Sanin")
print("---------------------------- AIH Higher Education ----------------------------------")
print()
print("Welcome to the Survey Program")

#also can take 20 custom responses from user
for i in range(20):
    msg='Please rate quality of product'+str(i+1)+' from 1 to 5: '
    user_rate=int(input(msg))
    responsez.append(user_rate)

print(responsez)

responsezinword=[]  #list of response words
#add responses word against response rate
for res in responsez:
    if res==1:
        responsezinword.append('awful')
    elif res==2:
        responsezinword.append('okay')
    elif res==3:
        responsezinword.append('good')
    elif res==4:
        responsezinword.append('better')
    elif res==5:
        responsezinword.append('excellent')

#print(responses_in_word)

#find frequency of response
frequency=dict(Counter(responsez))
print('\nFrequency of each rating: ',frequency)
        
print('\nResponse Statistics:')
#find min and max value
print('\nMin value: ',min(responsez))
print('\nMax value:',max(responsez))

#find range of response
mini=min(responsez)
maxi=max(responsez)
print('\nRange is {0} to {1}'.format(mini,maxi))

#find mean value
print('\nMean: ',statistics.mean(responsez))

#find median value
print('\nMediand: ',statistics.median(responsez))

#Mode calculation

#create NumPy array of values with only one mode
x = np.array(responsez)

#find unique values in array with the counts
vals, counts = np.unique(x, return_counts=True)

#find mode
mode_value = np.argwhere(counts == np.max(counts))

print('\nMode: ',vals[mode_value].flatten().tolist())

#find variance
print('\nVariance: ',np.var(responsez))

#find st.dev
print('\nStandard Deviation: ',statistics.stdev(responsez))

#calculate response frequencies %
percentresponsez=[]
for i in range(5):
    percentresponse=(frequency[i+1]/20)*100
    percentresponsez.append(int(percentresponse))

#plot pie chart with percentage
chart_label=['1(Awful)','2(Ok)','3(Good)','4(Better)','5(Excellent)']
plt.pie(percentresponsez,labels=chart_label,autopct='%1.1f%%')
plt.title("Response and their frequencies percent of total responses")#add title
plt.axis('equal')
plt.show()

#plot bar chart      
plt.bar(responsezinword,responsez,color='orange',edgecolor='black')
plt.title('User Chart on Product',fontsize=16)#add title
plt.xlabel('Rating in words')#set x-axis
plt.ylabel('Rating')#set y-axis
plt.show()

#will have two sets of plots, predefined response and user input response