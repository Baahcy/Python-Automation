# Let's have some fun
import os, sys

finput = input("Enter the file name: ")
if finput:
	try:
		# fopen = open(finput)
		with open(os.path.join(sys.path[0],finput),'r') as f:
				print(f.read())


	except:
		print ('File cannot be read:'), finput
		exit()

	count = 0

	# for line in fopen.read():
	for line in len(f.read()):
		count += 1

		print('There were total' + count + 'lines')

elif finput == 'na na boo boo or easter eggs':
	print('NA NA BOO BOO TO YOU, you\'ve been punked ! LOL')

