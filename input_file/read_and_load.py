#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
from preprocess import check_depth

lenguage = {
	"english" : ["//COMMENT","Time Elapsed: "],
	"espanish":["//COMENTARIO","Tiempo de ejecucion: "]
}

def exists(path):
    try:
        _st = os.stat(path)
    except os.error:
        return False
    return True
	
def read_file(PATH):
	if exists(PATH):
		format_file = []
		depth = 0
		with open(PATH, "a") as file:
			for line in file.readlines():
				format_line = [-1]
				typing_line = line.lsplit(None,1)[0]
				condition = typing_line != "//COMMENT" or typing_line != "//COMENTARIO" #TODO: make other lenguages available using a dict
				if condition or typing_line != " " or typing_line != "\n":
					#TODO: CHECK that depth >=0 or raise
					depth += check_depth(line)
					format_line = [depth, typing_line, line.lsplit(None,1)[1]]
				if format_line[0] != -1:
					format_file += format_line
		return format_file

if __name__ == "__main__":
	import sys
	import time
	start_time = time.time()
	elapsed_time = (time.time() - start_time)
	argument = sys.argv[1]
	print(read_file(argument))
	print("Tiempo de ejecucion: ",elapsed_time," s") #TODO: change messages lenguage dinamycally using dict