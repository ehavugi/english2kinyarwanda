## A number of components for an English to Kinyarwanda translator(Focus - rules +English tagging)

# current supported features:

1. Detecting kinyarwanda_ness of txt by using ratio consonant combinations that confirm to kinyarwanda consonant constraints(ibihekane)
2. Autogenerating numbers wording in order of 10^15(Kinyarwanda), and English(10^6)
	+ test kinyarwanda number2word at <http://g.havugimana.com//count/1010000>, change the numeric value and see the output
3. Autoconjugating (present, past, and future) in kinyarwanda ---template()
4. Plural formation(kinyarwanda) --still in development(it can be used as noun class detector with some tweak)

## Currently, I am doing 

1. English tense and verb detector (on simple sentences)
2. webscrawling +webscraping tool
3. studying IBM models(for SMT)

# for testing features (use,edit)

testing_features.py

+ edit testing_features by uncommenting and commenting
+ print(function_number(input))
	+ print(thousands(100)) ===> one hundred 
+ Error?
	+ make sure you have imported all neccessary code
		+ from code.number2words import *, inport everything in number2words(including bugs if any)
	+install any missing lib
		+BS4
		+NLTK(if used)

+ No need to install for testing some features:
	+ <http://g.havugimana.com/count/224>
		+ works for numbers and return wording for a number(this case 224)
	+ <http://g.havugimana.com/ubwinshi/icyuki>
		+ return the plural form of word icyuki
			+ currently in development
			+ You can look at the code and suggest tweaks
+ word list 
	+ <http:///www.havugimana.com/rw_word_list.txt> 



