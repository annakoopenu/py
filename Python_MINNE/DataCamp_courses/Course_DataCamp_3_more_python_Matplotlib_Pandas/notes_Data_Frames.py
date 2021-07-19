'''Notes about Data Frames 
'''
import pandas as pd

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary with three key:value pairs
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

def print_example_at_once(toprint, title):
    print()
    print()
    print (title)
    print()
    print(toprint)
    input()

# Build a DataFrame from dict
cars = pd.DataFrame(my_dict)
print_example_at_once('Ooo', '-------- First created a DataFrame: -------')

print_example_at_once(cars, '-- Here the cars DataFrame example: ')

# Label rows
cars.index = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
print_example_at_once(cars, '-- Labeling rows: ')

print_example_at_once(cars['country'], 'Taking out one column as Pandas Series')
print_example_at_once(cars[['country']], 'Taking out one column as Pandas Frame')
print_example_at_once(cars[['country', 'drives_right']], 'Taking out DataFrame with x and y columns')
print_example_at_once(cars[0:3], 'Select first 3 observations')
print_example_at_once(cars[3:6], 'Select fourth, fifth and sixth observation')

# loc - data selection based on column name
print_example_at_once(cars.loc['JPN'], 'Select column by index')
print_example_at_once(cars.loc[['AUS','EG']], 'more index')
print_example_at_once(cars.loc[:, ['country']], 'column')


# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row) 

