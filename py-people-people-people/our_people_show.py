
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

def read_our_data():
    people_our_data = pd.read_csv('/Users/Anna/people_you_must_know.csv')
    print('---------- People you must know dataset ----------------')
    print(people_our_data.shape)
    print(people_our_data.columns)
    print(people_our_data.info())
    print(people_our_data.head())
    return people_our_data

def our_random_recomindatiom(df):
    print('---------- Random creation for you ----------------')
    random_index = 0
 #   creations = ppd['creations']
 #   c = list(creations)
 #   print(c[random.randint(0 , len(c) - 1)], end='\n')
 # mm
    return df.iloc[random_index]


#read_our_data()
