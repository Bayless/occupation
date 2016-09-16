#Write a Python script to read in the file and build an appropriate dictionary from it. Make sure the percentages are stored as numbers.
#Create a function that returns a randomly selected occupation where the results are weighted by the percentage given. For example, there should be a 6.1% chance that "Education, training and library" is returned.
#File under occupation, with your local submodule name in this format: Aast-Airst_Bast-Birst
import random

occupations = open('occupations.csv','r')
occupations = occupations.read()
occupations = occupations.split('\n')
occupations = occupations[1:len(occupations)-1] #removes the job class and the total
Occups = []
percentages = []
for x in range (0,len(occupations)-1):
    lastCom = occupations[x].rfind(",")
    y = occupations[x][:lastCom]#spliting a row into occupation adn percetage seperately
    if y.count(',')>0:#if there is more than one comma
        y = y[1:len(y)-1]#get rid of the ""
    #print y
    q = occupations[x][lastCom+1:]
    #print q
    Occups.append(y) #occupations is all the stuff before the last comma
    percentages.append(float(q)) #percent is after the last comma
prof_dict = {}
for i in range(len(occupations)-1):#making it a dict
    #print Occups[i]
    prof_dict[Occups[i]] = percentages[i]

#for j in prof_dict:
    #print j, prof_dict[j]

cumSum = {}#makin a dict  with cummulative percentages
yo = 0
for g in prof_dict:
    print g
    print prof_dict[g]
    cumSum[g] = prof_dict[g] + yo
    yo += prof_dict[g]
#print cumSum['Life, Physical and Social Science']
cumLo = {}#makin a dict shifted one down from cumSum (1st place is 0)
yay = 0
for h in prof_dict:
    cumLo[h] = yay
    yay = cumSum[h]
#print cumLo['Production']
   
def randMan():
    randNum = random.random() * 100
    
    for i in cumSum:
        if (cumSum[i] >= randNum) and (cumLo[i] < randNum):
            return i
    print i

    
#.index('')
#dict['key']=val
#convert all percentages to nums
#prof_dict['occupation']->percentage
