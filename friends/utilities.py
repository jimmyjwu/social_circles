"""
utilities.py contains utility functions used throughout the 'friends' app.
"""

def chunks(full_list, chunk_size):
	"""
	Given a list, returns successive sublists of specified size.
	"""
	chunks = []
	for index in xrange(0, len(full_list), chunk_size):
		chunks += [full_list[index:index+chunk_size]]
	return chunks

def print_execution_time(operation_name, start_time, end_time):
	"""
	Outputs the execution time (in seconds) of an operation to the console.
	"""
	print(operation_name + ' took ' + str('%.1f' % (end_time - start_time)) + ' seconds.')

def print_object_type(variable_name, variable):
	"""
	Outputs the object type (class) of a variable.
	"""
	print variable_name + ' is a ' + str(type(variable))

def test_and_print_edge_uniqueness(graph):
	"""
	Given a graph, outputs the number of duplicate edges (u,v) and (u,v), if any.
	"""
	edges = graph.edges()
	edge_set = set(edges)
	number_of_duplicate_edges = 0
	for u, v in edges:
		if (v, u) in edge_set:
			number_of_duplicate_edges += 1
	print(str(number_of_duplicate_edges) + ' DUPLICATE EDGES DETECTED.' if number_of_duplicate_edges > 0 else 'NO DUPLICATE EDGES DETECTED.')



