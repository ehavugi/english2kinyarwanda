
from code.number2words import *
from code.EnglishTagging import *
from code.translator import translate
from sys import *
from math import *
#print(econj("do"))
# print([x**2 for x in range(10)])
# print([ibihumbi(i) for i in range(10)])
#print(translate(45))
#print(translate(" See you next time  and good morning"))

if __name__=="__main__":
	try:	
		#print("trying")
		if len(argv)==2:
			if " " not in argv[1]: ### this capters numbers(that need to be string,etc)
				a=argv[1].replace("(","('").replace(")","')")
			a=argv[1]
			#print("argv ==2",a)

			a=(eval(a))

			if len(a)>1 and not isinstance(a,str):
				for i in a:
					print (i)
			else:
				if a!="none":
			 		print(a)
		else:
			functionx=str(argv[1])+"("+str(argv[2])+")"
			print(functionx)
			print(eval(functionx))
	except:
		print("except",argv)
		pass
		#print (argv [3])