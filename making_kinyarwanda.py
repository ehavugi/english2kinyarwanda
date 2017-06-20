"""
	get English tagged list and devise a kinyarwanda version using kinyarwanda sentence formation rules, word formation rules
	and compound sentence formation both in Kinyarwanda and English..

"""

### a person to learn from :: how did he do with kiswahili? can I get his progress by today and inform him any of my progress "http://keshav.is/building/swahili-translator/"
noun_examples=["umwana","abana","umurima","imirima","iriba","amariba","icyebo","ibyebo","inka","inzuzi","urukwavu","inkwavu",]
noun_class=["mu","ba","mu","mi","ri","ma","ki", "bi","n","n","ru","ka","tu","bu","ku","ha"]
subject_marker=["a","ba","u","i",""]
object_marker=["mu","ba",""] ### I can ask a person who know them




def tense_marker(tense):
	if tense=="present":
		return ["ra","a"] ## nakubisse umwana ## ndahinga, urahinga, arahinga, turahinga,barahinga
	if tense=="past":
		return ["ara", "e"]  ## narahinze, warahinze, barahinze,twarahinze,barahinze
	if tense=="future":
		return "inzagihe marker"  #nzahinga
	if tense=="x":
		return "x"
	else:
		return 
#print("example on each noun_class",len(noun_examples))
#print("noun class : ", len(noun_class))
#print("subject makers: ", len(subject_marker))
#print("object marker : ", len(object_marker))
 


def kinya_constr(list):
	"""
		construct kinyarwanda wording from list of english tagged lists:
		tags: verb, tense, subject=="with kinyarwanda classifier equi", object="with kinyarwanda classfier tag"

	"""
	return 
	