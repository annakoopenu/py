import pandas as pd
import random

p1 = {
    'name' : 'Haruki Murakami',
    'titles' : 'writer',
    'creations' : 'The Wind-Up Bird Chronicle',
    'creations_year' : '01-01-2000'  #need a check
}
p11 = {
    'name' : 'Haruki Murakami',
    'titles' : 'writer',
    'creations' : 'Man in the Taxi',
    'creations_year' : '01-01-2000' #need a check
}
p2 = {
    'name' : 'David Lynch',
    'titles' : 'filmmaker',
    'creations' : 'Lost Highway',
    'creations_year' : '01-01-1997' #need a check
}
p3 = {
    'name' : 'Michelle Gurevich',
    'titles' : 'singer',
    'creations' : 'Party Girl',
    'creations_year' : '01-01-2010' #need a check
}
p4 = {
    'name' : 'Salvador Dali',
    'titles' : 'artist',
    'creations' : 'A Couple with Their Heads Full of Clouds',
    'creations_year' : '01-01-1936' #need a check    
}
p44 = {
    'name' : 'Salvador Dali',
    'titles' : 'artist',
    'creations' : 'Apparition of Face and Fruit Dish on a Beach',
    'creations_year' : '01-01-1938' #need a check
}
p444 = {
    'name' : 'Salvador Dali',
    'titles' : 'artist',
    'creations' : 'The Disintegration of the Persistence of Memory',
    'creations_year' : '01-01-1954' #need a check
}
# Please add p5
p5 = {
    'name' : 'Antoni Gaudí',
    'titles' : 'architect',
    'creations' : ' Casa Batlló ',
    'creations_year' : '01-01-1906' #need a check
}
# DataFrame from list pf dicts
ppd = pd.DataFrame([p1, p11, p2, p3, p4, p44, p444])
ppd = ppd.append(p5, ignore_index = True)
print()
print('---------- People you must know dataset ----------------')
#print(ppd.shape)
print(ppd.head())

creations = ppd['creations']
c = list(creations)
print(c)

print('---------- Random creation for you ----------------')
print(c[random.randint(0 , len(c))])
#lambda 
print()

ppd.to_csv('people_you_must_know.csv')
print('Saved to csv.. i hope.. ')
