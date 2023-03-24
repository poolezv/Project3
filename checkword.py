import re

def checkWord(unused, pattern):
	resList = []
	with open('wordlist.txt', 'r') as wordFile:
		rePat = '['+unused+']'
		regex = re.sub('[a-z]', rePat, pattern) + '$'
		regex = regex.lower()
		print('matching', regex)
		for line in wordFile:
			if re.match(regex, line[:-1]):
				resList.append(line[:-1])
	return resList

def findLetters(unused, pattern):
	resList = []
	with open('wordlist.txt', 'r') as wordFile:
		ctLetters = re.findall('[a-z]', pattern)
		print(ctLetters)
		rePat = '(['+unused+'])'
		regex = re.sub('[a-z]', rePat, pattern) + '$'
		regex = regex.lower()
		for line in wordFile:
			myMatch = re.match(regex, line[:-1])
			if myMatch:
				matchingLetters = myMatch.groups()
				matchList = []
				for l in matchingLetters:
					matchList.append(l.upper())
				resList.append(line[:-1])
				resList.append(list(zip(ctLetters, matchList)))
	return resList
