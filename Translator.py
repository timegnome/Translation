# ********************************************************
# Marcel Maxwell
# Translator
# This file will be the backend of the translation program
# and will house the necessary calls and objects for the
# translator. The file will consist of at least 2 classes
# for the translator to operate. It will take in the 
# desired text selected by the user and then input it into
# the translator. The input will be linked to the output
# word-word and sentence-sentence. This will allow for the
# program to adapt the the users changes and corrections.

# Takes in a text file in a type of language. 
# Checks the type of language matches with designated language and then begins the translation.
# Stores text temporarily in program.
# Use the tuples to increment the popularity of either trans or phrase
# Use the dictionary to store {translatedText: (original, popularity)}
# Use the dictionary to store {Index: translatedWord}
# Use the dictionary to store {Index: translatedPhrase}
# Use the tuples to store {Word, [index1, index2, index3.....]} (Word :[index1, index2, index3...])
class Translator:
	def _int_(self):
		self.transDatabase = {}
		self.directDatabase = {}
		self.phraseDatabase = {}
		self.grammarphrases = {}
		self.puncuation = {'"', ',', '(', ')', '\'', '.', '?', '!', '#', '$', '%', '('}
	
	'''
	def getTranslations(self, fileDataBase):
		return transDatabase
	def getDirect(self, fileDataBase):
		return directDatabase
	def getPhrase(self, ):
		return phraseDatabase
		
	def readdata(textfile):
		for text in textfile:
			assigntext(text)
		
	def assigntext(self, text):
		if(!(database.exists(text))):
			self.database.add(text)
		
	def translatetext(text, database)
		if(database.exists(text)):
	
# codec list
# big 5, big5hkscs, cp037, cp932, cp949, gb2312, gbk, gb18030, hz, utf_16, utf_7, utf_16be, utf_8, utf_16le, iso2022_jp_2 

# Parse the data on the Excel or .csv file and import it into the database class.
# If there is a current directory in use import data from either a binary temp file or full import the whole database with pertinent information
	def readdatabase(currentproject)
		if()
		file.open()
	def grammarcheck()
		if()
		if()
		if()
	
	def translationcheck()

	def exportdatabase()

	def importdatabase()

	def changetranslation()

	def changelink()
'''