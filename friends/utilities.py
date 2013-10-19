"""
utilities.py contains utility functions used throughout the 'friends' app.
"""

def print_execution_time(operation, start_time, end_time):
	"""
	Outputs the execution time (in seconds) of an operation to the console.
	"""
	print(operation + ' took ' + str('%.1f' % (end_time - start_time)) + ' seconds.')

def chunks(full_list, chunk_size):
    """
    Generator function; yields successive sublists of specified size from a list.
    """
    for index in xrange(0, len(full_list), chunk_size):
        yield full_list[index:index+chunk_size]