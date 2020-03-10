originalList = [1, 2, 2]
finalList = []

#outer loop iterates through list
for i in range(len(originalList)):
    j = i
    #inner loop creates a subset and adds it to the final list if not already there
    while j < len(originalList):
        currentSlice = originalList[i:j + 1]
        if currentSlice not in finalList:
            finalList.append(currentSlice)
        j += 1
print(finalList)



