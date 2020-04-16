import sys

def findAll(source, search):
	retList = []
	last_found = -1 
	while True:
		last_found = source.find(search, last_found + 1)
		if last_found == -1:  
			break  
		retList.append(last_found)

	return retList

def getParams(source):
	retList = []
	startIndex = findAll(source, "{{")
	endIndex = findAll(source, "}}")

	for start, end in zip(startIndex, endIndex):
		print(f'set: start={start} end={end}')

		start = start + 2 if start != -1 else start
		if start != -1 and endIndex != -1:
			exVal = source[start:end]
			print(f'param found: {exVal}')
			retList.append(exVal)

	return retList
