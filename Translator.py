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
# Use the string to link translation node and the translated text
# I.e. {translation node : 'word', translation node : 'other'} 
# Use the tuples to store {Word, [index1, index2, index3.....]} (Word :[index1, index2, index3...])
import csv
class translNode():
	def  __init__(self, *args, **kwargs):
		self.translated = args[0]
		self.original = args[1]
		self.count = 1
		self.possible = [] # List of possible translations from the original
# May replace with Natural Language Toolkit NLKT
class grammarcheck():
	def  __init__(self, *args, **kwargs)
		self.puncuation = {'"', ',', '(', ')', '\'', '.', '?', '!', '#', '$', '%'}
		self.grammarphrases = {}
		self.temp =1
class Translator():
	def  __init__(self, *args, **kwargs):
		self.transDatabase = {}
		self.directDatabase = {}
		self.phraseDatabase = {}
		self.userDatabase = {}
		
	def addTranslation (self, trans, orig):
		if orig in self.transDatabase:
			self.transDatabase[orig].count += 1
		else:
			self.transDatabase[orig] = translNode(trans, orig)
			self.transDatabase[orig].possible = self.getPossible(orig)
			
	def removeTranslation(self, orig):
		if orig in transDatabase 
			if self.transDatabase[orig].count > 1:
				self.transDatabase[orig].count -=1
			else:
				del self.transDatabase[orig]
				
	def getPossible(self, orig)
		return self.directDatabase[orig]
		
	def importDefault(self, directory):
		with open('eggs.csv', newline='') as csvfile:
			transReader = csv.reader(csvfile, delimiter=',')
				for row in tranReader:
					self.directDatabase[row[0]] = row[1:]
		
	def importExisting(self, directory):
		with open('eggs.csv', newline='') as csvfile:
			transReader = csv.reader(csvfile, delimiter=',')
				for row in tranReader:
					self.transDatabase[row[0]] = row[1:]
		with open('eggs.csv', newline='') as csvfile:
			transReader = csv.reader(csvfile, delimiter=',')
				for row in tranReader:
					self.phraseDatabase[row[0]] = row[1:]
		with open('eggs.csv', newline='') as csvfile:
			transReader = csv.reader(csvfile, delimiter=',')
				for row in tranReader:
					self.userDatabase[row[0]] = row[1:]
		self.importDefault()
		
	def exportDatabase(self, filename):
		with open('eggs.csv', 'w', newline='') as csvfile:
			transReader = csv.writer(csvfile, delimiter=',')
				for row in transDatabase:
					spamwriter.writerow(self.transDatabase[row[0]])
		with open('eggs.csv', 'w', newline='') as csvfile:
			transReader = csv.writer(csvfile, delimiter=',')
				for row in phraseDatabase:
					spamwriter.writerow(self.phraseDatabase[row[0]])
		with open('eggs.csv', 'w', newline='') as csvfile:
			transReader = csv.writer(csvfile, delimiter=',')
				for row in userDatabase:
					spamwriter.writerow(self.userDatabase[row[0]])
		
	def getUsersTranslation(self):
		return self.userDatabase
		
	def getTranslations(self):
		return self.transDatabase
		
	def getDirect(self):
		return self.directDatabase
		
	def getPhrase(self):
		return self.phraseDatabase
	
	def assigntext(self, text):
		if(!(database.exists(text))):
			self.database.add(text)
		
	def translatetext(self, text)
		for word in text:
			if(text in self.transDatabase):
				return self.transDatabase[text]
			elif text in self.directDatabase:
				self.transDatabase[text] = self.directDatabase[text]
				return self.transDatabase[text]
			else:
				# Prompt user for a translation recommendation
				self.transDatabase[text] = translNode(userInput, text)
				return self.transDatabase[text]
# codec list
# big 5, big5hkscs, cp037, cp932, cp949, gb2312, gbk, gb18030, hz, utf_16, utf_7, utf_16be, utf_8, utf_16le, iso2022_jp_2 

# Parse the data on the Excel or .csv file and import it into the database class using dict's.
# If there is a current directory in use import data from either a binary temp file or full import the whole database with pertinent information
