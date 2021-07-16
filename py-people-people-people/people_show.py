from os import name
import pandas as pd
import random

ppd = pd.read_csv('/Users/Anna/people_you_must_know.csv')
print('---------- People you must know dataset ----------------')
print(ppd.shape)
print(ppd.columns)
print(ppd.info())
print(ppd.head())

print('---------- Random creation for you ----------------')
creations = ppd['creations']
c = list(creations)
print(c[random.randint(0 , len(c))], end='\n')
