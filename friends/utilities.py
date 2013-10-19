"""
utilities.py contains utility functions used throughout the 'friends' app.
"""

def print_execution_time(operation_name, start_time, end_time):
	"""
	Outputs the execution time (in seconds) of an operation to the console.
	"""
	print(operation_name + ' took ' + str('%.1f' % (end_time - start_time)) + ' seconds.')

def chunks(full_list, chunk_size):
	"""
	Given a list, returns successive sublists of specified size.
	"""
	chunks = []
	for index in xrange(0, len(full_list), chunk_size):
		chunks += [full_list[index:index+chunk_size]]
	return chunks