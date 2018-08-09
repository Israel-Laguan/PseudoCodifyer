#!/usr/bin/python
# -*- coding: utf-8 -*-

from sintaxis import check_if, check_while, check_function, check_assign

STRUCTURES = {
	"english" : ["IF","WHILE","FUNCTION","ASSIGN"],
	"espanish":["SI","MIENTRAS","FUNCION","ASIGNAR"]
}

def create_tree(matrix_original):
	matrix = matrix_original
	rows = len(matrix)
	for row in range(0,rows):
		if matrix[row][1] == "IF":
			matrix[row] = check_if(matrix[row])
		elif matrix[row][1] == "WHILE":
			matrix[row] = check_while(matrix[row])
		elif matrix[row][1] == "FUNCTION":
			matrix[row] = check_function(matrix[row])
		elif matrix[row][1] == "ASSING":
			matrix[row] = check_assign(matrix[row])
	return 





if __name__ == "__main__":
	import sys
	import time
	start_time = time.time()
	elapsed_time = (time.time() - start_time)
	argument = sys.argv[0]
