'''Assignments of chapter1 course Introduction to Python'''

def how_to_Assign_Variables():
	# Create a variable savings
	savings = 100
	# Print out savings
	print(savings)

def how_to_make_Type_Conversion():
	# Definition of savings and result
	savings = 100
	result = 100 * 1.10 ** 7

	# Fix the printout
	print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

	# Definition of pi_string
	pi_string = "3.1415926"

	# Convert pi_string into float: pi_float
	pi_float = float(pi_string)	

##################### main ######################
if __name__ == "__main__":
	print()
	print()
	print("### Chapter 1 - Python Basics")
	print()
	print("#Chapter 1 ex1 - how to Assign Variables")
	how_to_Assign_Variables()
	print()
	print("#Chapter 1 ex4 - how to make Type Conversation")
	how_to_make_Type_Conversion()

	print()
	print()
	print("### Chapter 2 - Python Lists")
	print()
	