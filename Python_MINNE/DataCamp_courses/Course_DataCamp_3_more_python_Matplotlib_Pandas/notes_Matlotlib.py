'''Notes about matplotlib of chapter1 course Introduction to Python'''

from matplotlib import pyplot as plt
import random

def show_plot_for_my_data(x_data, y_data, plot_func):
	print()
	print()
	print("### My Data:")
	print(x_data)
	print(y_data)
	print('Plotting with ' + plot_func.__name__ +' !')
	plot_func(x_data, y_data)
	plt.show()

##################### main ######################
if __name__ == "__main__":
	
	x = [i+1 for i in range(12)]
	y1 = [(i+1)*3 for i in range(12)]
	y2 = [random.randint(0,100) for _ in range(12)]
	y3 = [random.randint(0,100) for _ in range(12)]
	y4 = list(map(lambda x: x**2, range(12)))
	
#	show_plot_for_my_data(x, y1, plt.plot)
#	show_plot_for_my_data(x, y2, plt.plot)
#	show_plot_for_my_data(x, y3, plt.plot)
#	show_plot_for_my_data(x, y3, plt.scatter)
#	show_plot_for_my_data(x, y4, plt.plot)
#	show_plot_for_my_data(x, y4, plt.scatter)
	
#	x5 = [i+1 for i in range(120)]
	y5 = [random.randint(0,100) for _ in range(120)]
	plt.hist(y5, bins = 20)
	plt.show()