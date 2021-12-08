
from ast import Index
import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame

def read_open_data(file_loaction):
    print('---------- An Open DataSet from Kaggle  ----------------')
    open_dataset = pd.read_csv(file_loaction)
    print(open_dataset.shape)
    print(open_dataset.columns)
    print(open_dataset.info())
    print(open_dataset.head())
    return open_dataset

def improve_open_data(dataset):
    # Add a column with the mean score
    for i, row in dataset.iterrows():
        dataset.loc[i ,'score'] = round(row[0:48].mean(), 2)   
    # Drop the 48 columns of personal votes
    print(dataset.columns)

    cols_to_drop = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11',
           'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21',
           'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31',
           'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41',
           'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48']

    thin_kaggle_painters = dataset.drop(columns=cols_to_drop)

    return thin_kaggle_painters


### Main
local_file_loaction = '/Users/Anna/Documents/GitHub/py/py-people-people-people/open_datasets/paintings.csv'

kaggle_painters = DataFrame()
kaggle_painters_row_data = read_open_data(local_file_loaction)
kaggle_painters = improve_open_data(kaggle_painters_row_data)

print('i wonder if it might work')
print(kaggle_painters.head(20))
kaggle_painters = kaggle_painters.sort_values(reversed = )
painters_colors = [i for i in range(39)]
paintings_score = kaggle_painters['score'] * 100

fig, ax = plt.subplots()
plt.scatter(x = kaggle_painters['artist'], y = kaggle_painters['score'], c = painters_colors, s = paintings_score)
ax.set_xticklabels(kaggle_painters['artist'], rotation=60)
plt.xlabel('painters')

plt.show()

gr = kaggle_painters.groupby('art movement')
movements = [movement[0] for movement in gr]
print(type(movements))
print(movements)
print('The length of movements')
print(len(movements))

#type(gr.value_counts['art movement'])

#data = {'a': np.arange(39),
#        'c': np.random.randint(0, 20, 39),
#        'd': np.random.randn(39)}
#data['b'] = data['a'] + 10 * np.random.randn(39)
#data['d'] = np.abs(data['d']) * 100



#print(kaggle_painters.columns)
#print(kaggle_painters.head())
#plt.hist(kaggle_painters['score'])


#print('x')
#print(type(data['a']))
#print(len(data['a']))
#print(data['a'])
#print('y - Score')
#print(type(kaggle_painters['score']))
#print(len(kaggle_painters['score']))
#print(kaggle_painters['score'])

#print(type(kaggle_painters['score']))
#plt.scatter(x = data['a'], y = kaggle_painters['score'], c = painters_colors)
