import numpy as np

def print_my_np(np_arr):
    print('\n---------------------')
    print(str(np_arr))
    print('type: ' + str(type(np_arr)))
    print('type of data: ' + str(np_arr.dtype))
    print('shape of data: ' + str(np_arr.shape))
    print('---------------------')


#1
a = np.array([1,2,3])
#2
b = np.array(a, dtype=float)
#3
a = np.arange(0,11)
#4
a = np.linspace(0,23,7)
#5
b = np.ones((2,5,1,5,2,1))
b.fill(5)
#6
#c = b.take(axis=0)

k = np.split(b, axis=0)


print('\n')
print(k)
#print_my_np(k)


