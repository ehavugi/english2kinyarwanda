
from code.number2words import *
from code.EnglishTagging import *
#from code.ubuke_ubwinshi import *
from sys import *
from math import *
#print(econj("do"))
# print([x**2 for x in range(10)])
# print([ibihumbi(i) for i in range(10)])

if __name__=="__main__":
	try:	
		#print("trying")
		if len(argv)==2:
			a=(eval(argv[1]))
			if len(a)>1 and not isinstance(a,str):
				for i in a:
					print (i)
			else:
				if a!="none":
			 		print(a)
		else:
			functionx=str(argv[1])+"("+str(argv[2])+")"
			#print(functionx)
			print(eval(functionx))
	except:
		print("except",argv)
		pass
		#print (argv [3])