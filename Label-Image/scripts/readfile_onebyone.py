import sys
import os
import stat

list = []
file = '../Labels/003/frame0028.txt'

with open(file,'r') as f:
	for line in f:
		a = line.split()
		list.append(a)
		  	
	if len(list[0]) ==1:
		list.pop(0)

	#swapping between x and y
	for i in range(len(list)):
		list[i][0],list[i][1] = list[i][1],list[i][0]
		list[i][2],list[i][3] = list[i][3],list[i][2]

f.close()

with open(file,'w') as fr:	
	for i in list:
		fr.write(' '.join(i) + '\n')
	list = []
fr.close()
		


