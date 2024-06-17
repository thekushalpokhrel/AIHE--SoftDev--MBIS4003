#analysis function for three level game
def stat_analysis(c1,c2,c3):
    #ask question for viewing analysis of game
    analysis=input('\nDo you want to see your game analysis? (Yes/No) ')
    if analysis=='Yes':

        levels=['Level 1','Level 2','Level 3']
        
        #calculating the score of levels
        l1_score= c1*10
        l2_score= c2*10
        l3_score= c3*10
        level_score=[l1_score,l2_score,l3_score]

        #plot bar chart      
        plt.bar(levels,level_score,color='blue',edgecolor='black')
        plt.title('Levelwise Scores',fontsize=16)#add title
        plt.xlabel('Levels')#set x-axis label
        plt.ylabel('Scores')#set y-axis label
        plt.show()

        print('\nDescriptive Statistics of Scores:')
        #find mean value
        print('\nMean: ',statistics.mean(level_score))

        #find median value
        print('\nMediand: ',statistics.median(level_score))

        #Mode calculation

        #create numPy array of values with only one mode
        arr_val = np.array(level_score)

        #find unique values in array along with their counts
        vals, uni_val_counts = np.unique(arr_val, return_counts=True)

        #find mode
        mode_value = np.argwhere(counts == np.max(uni_val_counts))

        print('\nMode: ',vals[mode_value].flatten().tolist())

        #find variance
        print('\nVariance: ',np.var(level_score))

        #find standard deviation
        print('\nStandard Deviation: ',statistics.stdev(level_score))
        print('\nGood Bye.See you later!!!')
        
    elif analysis=='No':
        print('\nGood Bye.See you later!!!')
        
    else:
        print('Invalid value enter')
        stat_analysis(c1,c2,c3)

