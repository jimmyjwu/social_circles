"""
utilities.py contains utility functions used throughout the 'friends' app.
"""

def print_execution_time(operation, start_time, end_time):
	"""
	Outputs the execution time (in seconds) of an operation to the console.
	"""
	print(operation + ' took ' + str('%.1f' % (end_time - start_time)) + ' seconds.')