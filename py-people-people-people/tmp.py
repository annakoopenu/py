'''Checking the style of .py
'''
import pycodestyle

y = range(0, 5)
print(y)
print(type(y))


print('--------------------------------')
print('Just enother loop comprehension')
z = [i for i in range(5)]
print(z)

zz = [[i for i in range(5)] for j in range(5)]
print(zz)
print('--------------------------------')


style_checker = pycodestyle.StyleGuide()

x = [7, 8, 9]
y = [-3.3, -2, 3.2] + x[0:2]
print(x[0:2])
print()
print('Here something:')
print(y)
print(len(y))
print('\n it was something:')

style_check = style_checker.check_files(['/Users/Anna/Documents/Github/py/py-people-people-people/tmp.py'])

# in shell
#pycodestyle
#pip install pycodestyle
#pycodestyle dict_to_array.py



