# python, parsing file for generating python code of flow chart 

from six import string_types
# input file
inpfile = 'inp.txt'
outfile = 'pycode.py'


fileinp  = open(inpfile,'r')
fileout  = open(outfile,'w')

sttr =''
indent = 0 

for line in fileinp:

	line = line.replace("\n", "")
	wlist = line.split(' ')
	command = wlist[0]

	if command == 'START':
		sttr = '#pycode.py\n'
		indent = 0

	elif command == 'INP':
		charlist = wlist[1]
		charlist = charlist.split(',')

		for var in charlist:
			sttr += '\t'*indent + var + ' = input("enter variable ' + var + '")\n'

	elif command == 'OUT':
		charlist = wlist[1]
		'''
		print line + '\n'
		if "\"" in line:
			print [i for i, letter in enumerate(line) if letter == "\""]

		
			if isinstance(var, string_types):
				sttr += '\t'*indent +'print ' + var + '"\n'
			else:

		'''
		charlist = charlist.split(',')
		for var in charlist:
			var = var.replace('$',' ')
			print var
			sttr += '\t'*indent +'print ' + var + '\n'

	elif command == 'IF':
		charlist = wlist[1]
		sttr += '\t'*indent + 'if ' + charlist + ':\n'
		indent += 1

	elif command == 'ELSE':
		sttr += '\t'*(indent-1) + 'else:\n'

	elif command == 'OPR':
		sttr += '\t'*(indent-1) + wlist[1] + '\n'

	elif command == 'FI':
		indent-=1	

	elif command =='STOP':
		sttr +='# file ends here\n'

if __name__ == '__main__':
    fileout.write(sttr)
    #print sttr


