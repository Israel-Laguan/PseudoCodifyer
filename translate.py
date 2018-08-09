#!/usr/bin/python
# -*- coding: utf-8 -*-
#Made by Israel Laguan

from input_file.read_and_load import read_file
#from process_file.create_graph import *
#from output import *

if __name__ == "__main__":
	import sys
	import time
	start_time = time.time()
	elapsed_time = (time.time() - start_time)
	argument = sys.argv[1]
	#lenguage = sys.argv[2]  #set to python by now

	format_file = read_file(argument)
	#graph_tree = make_tree(format_file)
	#solved_tree = solve_tree(graph_tree)
	#output_file = make_py(solved_tree)

