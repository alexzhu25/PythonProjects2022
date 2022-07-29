# wordcount.py
# counts the number of times that each word appears in a text file

# source text file
fo = open(.\"wordcountdoc.txt") 
# TODO: can add query for custom document selection


#\\=====List implementation of program=====\\
print("=====List version=====")

# create list
tempList = []

# traverse doc and add each word to list
lines = fo.readlines()

for line in lines:
  words = line.split()
  for word in words:
    w = word.strip().lower() # when considering words, ignore caps
    tempList.append(w)

# count each word appearance in list and print results
for n in tempList:
  print(n + ", " + str(tempList.count(n)))


#\\=====Dictionary implementation of program=====\\
print("\n=====Dictionary version=====")

# create dictionary
tempDict = {}

# traverse doc and add each word to dictionary
for line in lines:
  words = line.split()
  for word in words:
    w = word.strip().lower() # when considering words, ignore caps
    # if new word, add new dictionary entry for word and assign initial count of 1
    if w not in tempDict:
      tempDict[w] = 1
    # if word already in dictionary (ie. repeat), increase word count by 1
    else:
      tempDict[w] = tempDict[w] + 1

# print dictionary results
for x, y in tempDict.items():
  print(x+":", y)


fo.close()