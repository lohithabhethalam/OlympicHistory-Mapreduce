x = open("PoojithaMapperOutput.txt","r")
# Open the mapper output as input to reducer funciton
y = open("PoojithaReducerOutput.txt", "w")
# Write the final output to this file
thisDict = {}
for line in x:
    data = line.strip().split('\t')
    # Seperate columns using space as reference
    city = data[0]
    # We are finding if height is given as NA and assigning them with 0
    if(str(data[1]) == "NA"):
        height = 0
    else:
        height = int(data[1])
    # we adding height to the array of cities if there is already exsisting city if not add a new one
    if city in thisDict.keys():
        thisDict[city] = thisDict[city] + [height]
    else:
        thisDict[city] = [height]
#print(thisDict.items())
# We are finding the maximum value of the height for each city
for keyItem,value in thisDict.items():
    maximum = max(value)
    y.write(keyItem +'\t'+ str(maximum) + "\n" )
    # 
    print(keyItem +'\t'+ str(maximum) +"\n" )
x.close()
y.close()
# Closing both the read only and write files