'''Notes about Dictionary - Python Data Structure 
Dictionary - is mutable
            key - have to be immutable 
'''

### Create a dictionary
my_dict = {
   "key1":"value1",
   "key2":"value2",
}
europe = {
    'spain':'madrid',
    'france':'paris',
    'germany':'perlin',
    'norway':'oslo',
    'australia' : 'sidney' 
}

### Access dictionary
    # keys in dict
print(europe.keys())
    # value that belongs to key
print(europe['norway'])

### Dictionary manipulation
    # Add key - value pair
europe['italy'] = 'rome'
    # Update value of key
europe['germany'] = 'berlin'
    # checks if element in dict 
print('italy' in europe)    #True
    # Remove key - value pair
del(europe['australia'])
    # Print dict
print(europe)

