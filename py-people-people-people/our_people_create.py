'''Creats list of people
        and saves it to csv file 'people_you_must_know.csv'
'''
import pandas as pd

p = [
        {
            'name' : 'Haruki Murakami',
            'titles' : 'writer',
            'creations' : 'The Wind-Up Bird Chronicle',
            'creations_year' : '2002'  #need a check
        },
        {
            'name' : 'Haruki Murakami',
            'titles' : 'writer',
            'creations' : 'Man in the Taxi',
            'creations_year' : '2017' #need a check
        },
        {
            'name' : 'David Lynch',
            'titles' : 'filmmaker',
            'creations' : 'Lost Highway',
            'creations_year' : '1997' #need a check
        },
        {
            'name' : 'Michelle Gurevich',
            'titles' : 'singer',
            'creations' : 'Party Girl',
            'creations_year' : '2010' #need a check
        },
        {
            'name' : 'Salvador Dali',
            'titles' : 'artist',
            'creations' : 'A Couple with Their Heads Full of Clouds',
            'creations_year' : '1936' #need a check    
        },
        {
            'name' : 'Salvador Dali',
            'titles' : 'artist',
            'creations' : 'Apparition of Face and Fruit Dish on a Beach',
            'creations_year' : '1938' #need a check
        },
        {
            'name' : 'Salvador Dali',
            'titles' : 'artist',
            'creations' : 'The Disintegration of the Persistence of Memory',
            'creations_year' : '1954' #need a check
        }
    ]

# DataFrame from list pf dicts
p_df = pd.DataFrame(p)
p_df.to_csv('/Users/Anna/people_you_must_know.csv')
print('Saved to csv.. ')
