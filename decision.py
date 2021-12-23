import numpy as np
import pandas as pd
import pprint
eps = np.finfo(float).eps
print(eps)
from numpy import log2 as log
outlook = 'overcast,overcast,overcast,overcast,rainy,rainy,rainy,rainy,rainy,sunny,sunny,sunny,sunny,sunny'.split(',')
temp = 'hot,cool,mild,hot,mild,cool,cool,mild,mild,hot,hot,mild,cool,mild'.split(',')
humidity = 'high,normal,high,normal,high,normal,normal,normal,high,high,high,high,normal,normal'.split(',')
windy = 'FALSE,TRUE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,TRUE'.split(',')
play = 'yes,yes,yes,yes,yes,yes,no,yes,no,no,no,no,yes,yes'.split(',')
dataset ={'outlook':outlook,'temp':temp,'humidity':humidity,'windy':windy,'play':play}
df = pd.DataFrame(dataset,columns=['outlook','temp','humidity','windy','play'])
print(df)


def totalentropy(df):
    Class=df.keys()[-1]
    values=df[Class].unique()
    entropy=0
    for value in values:
        fraction=len(df[Class][df[Class]==value])/len(df[Class])
        entropy+=-fraction*log(fraction)
    return entropy
print(totalentropy(df))
    

def information(df,att):
    Class=df.keys()[-1]
    values=df[Class].unique()
    targetvalues=df[att].unique()
    information=0
    for tval in targetvalues:
        entropy1=0
        
        for value in values:
            num=len(df[att][df[att]==tval][df[Class]==value])
            den=len(df[att][df[att]==tval])
            fraction=num/(den+eps)
            entropy1+=-fraction*log(fraction+eps)
        information+=(den/len(df[att]))*entropy1
    
    return abs(information)

def find_winner(df):
    IG=[]
    S=totalentropy(df)
    for att in df.keys()[:-1]:
        IG.append(S-information(df,att))
    return df.keys()[:-1][np.argmax(IG)]

def subtable(df,node,val):
    return df[df[node]==val]

def destree(df):
    
    tree={}
    
    winner=find_winner(df)
    tree[winner]={}
    
    #if len(df[winner].unique())==1:
        
        
        
    for val in df[winner].unique():
        sub=subtable(df, winner, val)
        if len(sub[sub.keys()[-1]].unique())==1:
            tree[winner][val]=sub[sub.keys()[-1]].unique()[0]
        else:
            tree[winner][val]=destree(sub)
    
    return tree
    
    
    
    
    
    
tree=destree(df)
pprint.pprint (tree)