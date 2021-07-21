'''Assignments of chapter1 course Introduction to Python'''
# https://campus.datacamp.com/courses/joining-data-with-pandas/merging-tables-with-different-join-types?ex=7

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
	print("### Chapter 2 - Python Lists Comprehension")
	print()
	# Create a list of strings: fellowship
	fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
	# Create list comprehension: new_fellowship
	new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]
	# Print the new list
	print(new_fellowship)

	# https://campus.datacamp.com/courses/python-data-science-toolbox-part-2/list-comprehensions-and-generators?ex=9
	
	# Create a list of strings: fellowship
	fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
	# Create dict comprehension: new_fellowship
	new_fellowship = { val:len(val) for val in fellowship }
	# Print the new dictionary
	print(new_fellowship)
	
	#
	#
	#
	#
	# List of strings
	fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
	# List comprehension
	fellow1 = [member for member in fellowship if len(member) >= 7]
	# Generator expression
	fellow2 = (member for member in fellowship if len(member) >= 7)
	#
	#
	#
	# # Create generator object: result
	result = (num for num in range(31))

	# Print the first 5 values
	print(next(result))
	print(next(result))
	print(next(result))
	print(next(result))
	print(next(result))
	print('----')
	# Print the rest of the values
	for value in result:
    	print(value)

