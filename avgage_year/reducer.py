reducerInput = open("reducerInput.txt","r")
# Open the mapper output as input to reducer funciton
reducerOutput = open("DivyaReducerOutput.txt", "w")
# Write the final output to this file
AverageDictionary = {}
for line in reducerInput:
    data = line.strip().split('\t')
    # Seperate columns using space as reference
    year = data[1]
    # We are finding if age is given as NA or Female or Male and assigning them with 0
    if str(data[0]) == "NA" or str(data[0]) == "F" or str(data[0]) == "M":
        age = 0
    else:
        try:
            age = int(data[0])
        except:
            age = 0
    # we are adding the age to the array of year if there is already existing year, if not add a new one
    if year in AverageDictionary.keys():
        AverageDictionary[year] = AverageDictionary[year] + [age]
    else:
        AverageDictionary[year] = [age]

# We are finding the average value of the age for each year
for keyItem,value in AverageDictionary.items():
    ageSum = sum(value)
    averageAge = ageSum/len(value) 
    reducerOutput.write(keyItem +'\t'+ str(averageAge) + "\n" )
    # 
    print(keyItem +'\t'+ str(averageAge) +"\n" )
reducerInput.close()
reducerOutput.close()
# Closing both the read only and write files