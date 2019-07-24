from sys import argv
from s8.txt import open_file, open_two_files



script, input_file1 , input_file2, outfile, outfile2, outfile3   = argv

b= open_two_files(input_file1 , input_file2)


a = open_two_files(input_file1,input_file2)

#File1 value
with open(outfile ,'w+') as f: 	
	f.write( a[0])

#File2 value
with open(outfile2 ,'w+') as f: 	
	f.write( a[1])


#Both files values
with open(outfile3 ,'w+') as f: 	
	f.write( a[0]+a[1])