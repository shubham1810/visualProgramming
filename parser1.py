# python, parsing file for generating python code of flow chart 

# input file
inpfile = 'inp.txt'
outfile = 'pycode.py'


fileinp  = open(inpfile,'r')
fileout  = open(outfile,'w')

flagstart = 0
sttr =''

for line in fileinp:

	line = line.replace("\n", "")
	wlist = line.split(' ')
	command = wlist[0]

	if command == 'START':
		flagstart = 1
		sttr = '#pycode.py\n'

	elif command == 'INP' and flagstart == 1:
		charlist = wlist[1]
		charlist = charlist.split(',')

		for var in charlist:
			sttr += var + ' = raw_input("enter variable ' + var + '")\n'

	elif command == 'OUT' and flagstart == 1:
		charlist = wlist[1]
		charlist = charlist.split(',')

		for var in charlist:
			sttr += 'print ' + var + '\n'

	elif command =='STOP' and flagstart == 1:
		flagstart = 0;
		sttr +='# file ends here\n'

if __name__ == '__main__':
    fileout.write(sttr)
    #print sttr


