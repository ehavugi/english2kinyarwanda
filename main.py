from code.number2words import *
from code.EnglishTagging import *
from code.translator import translate
from code import *
from sys import *
from math import *
from re import *

if __name__=="__main__":
	try:	
		#print("trying")
		if len(argv)<2:
			print ("add inputs -- function inputs")
			function=input("Enter function : ")
			inputs_1=input("Enter input to the function : ")
			a=eval(function+"("+inputs_1+")")
			print(a)
		elif len(argv)==2:
			print(argv[1])

			if " " not in argv[1] and not '"' in argv[1]: ### this capters numbers(that need to be string,etc)
				a=argv[1].replace('(','("').replace(')','")')
				print(a,1)
			elif ' ' not in argv[1] and not "'" in argv[1]:
				a=argv[1].replace("(","('").replace(")","')")
				print(a,2)
			else:
				a=argv[1].replace('(','("').replace(')','")')
				print(a,3)

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






#print(econj("get"))
# print([x**3 for x in range(10)])
# print([ibihumbi(i) for i in range(10)])
# print(translate("See you next time  and good morning"))
