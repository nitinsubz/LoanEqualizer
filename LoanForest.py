import csv
count=0

first=True
rows=[]
names=[]

with open('/Users/rohittanikella/Desktop/socialjustice/accept.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        row=row[0:17]
        del row[1]
        del row[1]
        del row[3]
        del row[10]
        
        if(first):
            names=row
            first=False
            
        if('' not in row and 'loan_amnt' not in row):
            rows.append(row)

labels=[]
purposes=['credit_card', 'car', 'small_business', 'other', 'wedding', 'debt_consolidation', 
          'home_improvement', 'major_purchase', 'medical', 'moving', 'vacation', 
          'house', 'renewable_energy', 'educational']
processedData=[]

print(len(rows))
for i in range(0,len(rows)):
    temp=[]
    doAdd=True
    
    temp.append(int(rows[i][0]))
    x=rows[i][1].index("m")
    temp.append(int(rows[i][1][0:x]))
    #Converts "xx months" to xx as an integer
    temp.append(float(rows[i][2][0:len(rows[i][2])-1]))
    x=0
    if "y" in rows[i][3]:
        x=rows[i][3].index("y")
    try:
        temp.append(int(rows[i][3][0:x]))
    except:
        if "+" in rows[i][3]:
            temp.append(10)
        else:
            temp.append(1)
    
    if rows[i][4]=='RENT':
        temp.append(0)
    elif rows[i][4]!='OWN':
        temp.append(1)
    elif rows[i][4]!='MORTAGE':
        temp.append(2)
    elif rows[i][4]!='OTHER':
        temp.append(3)
    else:
        doAdd=False
    
    #0 is rent
    #1 is own
    #2 is mortage
    #3 is other
    
    temp.append(float(rows[i][5]))
    
    if "Fully Paid" in rows[i][6] and doAdd:
        labels.append("Fully Paid")
    elif "Charged Off" in rows[i][6]:
        labels.append("Charged Off")
    else:
        doAdd=False
    
    if rows[i][7]=='n':
        temp.append(0)
    else:
        temp.append(1)
    #0 is no payment plan and 1 is a payment plan
    
    temp.append(purposes.index(rows[i][8]))
    
    temp.append(float(rows[i][9]))
    temp.append(float(rows[i][10]))
    temp.append(float(rows[i][11]))
        
    temp.append(float(rows[i][12][0:len(rows[i][12])-1]))
    
    #print(rows[i])
    if doAdd:
        processedData.append(temp)
    
#index 6 is the real status of the actual loan and is the independent variable

#print(len(processedData))
#print(processedData[10])
for item in labels:
    if not (item=="Fully Paid" or item=="Charged Off"):
        print("bad")
        print(item)

for item in processedData:
    for i in item:
        if type(i).__name__=='str':
            print("Error")

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=15)
clf = clf.fit(processedData[0:int(.8*len(processedData))], labels[0:int(.8*len(labels))])
print(clf)

from sklearn.metrics import accuracy_score
preds=clf.predict(processedData)
print(accuracy_score(preds,labels))

import pickle
path = 'loanTree.pkl'
# Open the file to save as pkl file
pkl_file = open(path, 'wb')
pickle.dump(clf, pkl_file)
# Close the pickle instances
pkl_file.close()
