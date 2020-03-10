dict1 = {'Bob': 44, 'George': 35, 'Sarah': 57}
dict2 = {'Ann': 84, 'Betty': 66, 'Mary': 24}

#put dict2 into dict1
dict1.update(dict2)
finalList = []

#make a value, key tuple for each item in dict1, put these in a list
for key, value in dict1.items():
    itemTuple = (value, key)
    finalList.append(itemTuple)

#sort the list and print each item
for i in sorted(finalList):
    print(i)
