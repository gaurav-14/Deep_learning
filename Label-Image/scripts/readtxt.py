import sys
import os
import stat

list = []
directory = '../Labels/003'


for file in os.listdir(directory):
	print file	
	with open(os.path.join(directory,file),'r') as f:

			for line in f:
				a = line.split()
		  		list.append(a)
		  	
			if len(list[0]) ==1:
				list.pop(0)

			print len(list)
				#swapping between x and y
			for i in range(len(list)):
				list[i][0],list[i][1] = list[i][1],list[i][0]
				list[i][2],list[i][3] = list[i][3],list[i][2]
	f.close()

	with open(os.path.join(directory,file),'w') as fr:	
		for i in list:
			fr.write(' '.join(i) + '\n')
		list = [] #initialize list	
	fr.close()
		


