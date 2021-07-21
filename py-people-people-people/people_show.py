from os import name
import pandas as pd
import random
from matplotlib import pyplot as plt


ppd = pd.read_csv('/Users/Anna/people_you_must_know.csv')
print('---------- People you must know dataset ----------------')
print(ppd.shape)
print(ppd.columns)
print(ppd.info())
print(ppd.head())

print('---------- Random creation for you ----------------')
creations = ppd['creations']
c = list(creations)
print(c[random.randint(0 , len(c) - 1)], end='\n')

kaggle_painters = pd.read_csv('/Users/Anna/Documents/GitHub/py/py-people-people-people/open_datasets/paintings.csv')
print(kaggle_painters.shape)
print(kaggle_painters.columns)

first_row = kaggle_painters.iloc[0,0:48] 
#print(first_row)
print(type(first_row))
print(first_row.sum()/len(first_row))

#for row in kaggle_painters.iterrows():
#    print('-- Row ')
#    print(row)


# Code for loop that adds a column
for i, row in kaggle_painters.iterrows():
    kaggle_painters.loc[i ,'score'] = round(row[0:48].mean(), 2)   

print(kaggle_painters.columns)

cols_to_drop = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11',
       'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21',
       'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31',
       'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41',
       'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48']

kaggle_painters = kaggle_painters.drop(columns=cols_to_drop)

print(kaggle_painters.columns)
print(kaggle_painters.head())
plt.hist(kaggle_painters['score'])

plt.show()
