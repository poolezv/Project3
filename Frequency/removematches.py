def removeMatches(myString, removeString):
	newStr = ""
	for ch in myString:
		if ch not in removeString:
			newStr = newStr + ch
	return newStr

