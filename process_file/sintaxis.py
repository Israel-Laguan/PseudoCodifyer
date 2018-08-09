#!/usr/bin/python
# -*- coding: utf-8 -*-

def check_function(row_array):
	row = row_array
	#TODO: CHECK IF IS WRITTEN WITH OTHER FORMAT
	try:
		function_name = row.lsplit("(",1)[0]
		function_arguments = row[2].lsplit("(",1)[1].rsplit(")",1)[0]
		functions_variables = function_arguments.split(",")
	except:
		print("Function not well writen: ",row[2])
	aux_list = ["def {}(".format(function_name)]
	for variable in functions_variables:
		if variable.find("(") != -1: #variable is a function
			row[0] +=1
			in_name = variable.lsplit("(",1)[0]
			in_arguments = variable.lsplit("(",1)[1].rsplit(")",1)[0]
			#TODO: Check if function call other functions
			aux_list += in_name
			aux_list += "("
			aux_list += in_arguments
			aux_list += ":"
		else:
			if aux_list.find("(") != -1:#is first argument
				aux_list += variable
			else:
				aux_list += ","
				aux_list += variable
		row += " ".join(aux_list)
	return row

def check_if(row_array):
	row = row_array
	#TODO: CHECK IF IS WRITTEN WITH OTHER FORMAT
	try:
		#CHECK if are multiple conditions
		#Check if 
	except:
	return row

def check_while(row_array):
	row = row_array
	return row

def check_assign(row_array):
	row = row_array
	return row

if __name__ == "__main__":
	import sys
	import time
	start_time = time.time()
	elapsed_time = (time.time() - start_time)
	argument = sys.argv[0]
