#!/usr/bin/python
# -*- coding: utf-8 -*-
fixed = {
		"END":	   -1,
		"FIN":	   -1,
		"IF":		1,
		"SI":		1,
		"WHILE":	1,
		"MIENTRAS":	1,
		"ELSE":		1,
		"CONTRARIO":1,
		"FUNCTION":	1,
		"FUNCION":	1
	}

def check_depth(condition):
	if condition in fixed:
		return fixed[condition]
	else:
		return 0
	#TODO: ADD CLASSES AND OTHER CASES



if __name__ == "__main__":
	import sys
	import time
	start_time = time.time()
	elapsed_time = (time.time() - start_time)
	argument = sys.argv[1]
	print(check_depth(argument))
	print("Tiempo de ejecucion: ",elapsed_time," s")

