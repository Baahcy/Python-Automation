# Let's have some fun
import os, sys

finput = input("Enter the file name: ")
if finput:
	try:
		with open(os.path.join(sys.path[0],finput),'r') as f:
				print(f.read())
		count = 0
		with open ( os.path.join ( sys.path[0] , finput ) , 'r' ) as f :
			for line in f :
				count += 1
		print ( 'Total number of lines is :' , count )

	except:
		print ('File cannot be read:'), finput
		exit()





elif finput == 'na na boo boo or easter eggs':
	print('NA NA BOO BOO TO YOU, you\'ve been punked ! LOL')

