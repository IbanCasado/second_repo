from sys import argv

script, input_file1 , input_file2   = argv

def open_file(input_file):
	with open(input_file,'r') as f:
		 print f.read()

def open_two_files(input_file1 , input_file2):
	open_file(input_file1)
	open_file(input_file2)
		
open_two_files(input_file1,input_file2) 