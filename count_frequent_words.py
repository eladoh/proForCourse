import sys

with open ("words.txt", "r") as file: # open the file as readable
	file = file.read() # reads the file content

file = "".join(x for x in file if x.isalpha() or x == " ") # turns the file into string and filters non alphabet characters

file = file.split(" ") # puts all words in the list

fileList = list(filter(lambda x: x != "" and len(x) > 1,file)) # filters "" and single letters 
fileDict = {x: fileList.count(x) for x in fileList} # sets how many times x appered and creates a dicts

sortedListByKey = list(sorted(fileDict, key= lambda x: fileDict[x], reverse=True)) # create a list sorted by the occurance of the words in the sheet

try:
	n = int(sys.argv[1])	
	for i in range(n): # printing only the amoumt the user asked for 
		print(f"the word: {sortedListByKey[i]} appered {fileDict[sortedListByKey[i]]} times")
except ValueError as e:
	print("please enter an integer! ")
