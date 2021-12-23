import csv
a=[]

print("The given training dataset \n")

with open('enjoysport.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes = len(a[0])-1

print("the initial value of hypothesis:\n")
S = ['0']*num_attributes
G = ['?']*num_attributes
print("Most specific hypothesis is: S0: ['0','0','0','0','0','0']\n")
print("Most General hypothesis is: G0: ['?','?','?','?','?','?']\n")

for j in range(0,len(a)):
    S[j]=a[0][j] 

print("\nversion control\n")
temp = []

for i in range(0, len(a)):
    print("\n--------------------------------------------------------\n")
    if(a[i][num_attributes]=='Yes'):
        for j in range(0,num_attributes):
            if(a[i][j]!=S[j]):
                S[j]='?'
        for j in range(0, num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j]!=S[j] and temp[k][j]!='?':
                    del temp[k]
        print("for training example:{0} initial hypothesis is: s{0}".format(i+1), S)
        
        if len(temp)==0:
            print("for training example:{0} initial hypothesis is: s{0}".format(i+1), G)
        else:
            print("for training example:{0} initial hypothesis is: s{0}".format(i+1), temp)
    if(a[i][num_attributes]=='No'):
        for j in range(0,num_attributes):
            if S[j]!=a[i][j] and S[j]!='?':
                G[j]=S[j]
                temp.append(G)
                G=['?']*num_attributes
        print("for training example:{0} initial hypothesis is: s{0}".format(i+1), S)
        print("for training example:{0} initial hypothesis is: s{0}".format(i+1), temp)
                