reducerInput = open("reducerInput.txt","r")
# Open the mapper output as input to reducer funciton
reducerOutput = open("DivyaReducerOutput.txt", "w")
# Write the final output to this file
excelData = reducerInput.readlines()
excelData.sort()

thisKey = ""
ageValue = 0
ageCount = 0
ageAverage = 0.0
for line in excelData:
    data = line.strip().split('\t')
    # Seperate columns using space as reference
    year = data[0]
    summerYear = year+" Summer"
    winterYear = year+" Winter"
    #print(year)
    if year == summerYear:
        year = year.replace("Summer","")
    elif year == winterYear:
        year = year.replace("Winter","")
    # We are finding if age is given as NA or Female or Male and assigning them with 0
    
    if str(data[1]) == "NA" or str(data[1]) == "F" or str(data[1]) == "M":
        age = 0
    else:
        try:
            age = int(data[1])
        except:
            age = 0
    # we are adding the age to the array of year if there is already existing year, if not add a new one
    
    if thisKey != year:
        if thisKey:
            ageAverage = float(ageValue/ageCount)
            print(thisKey +'\t'+ str(ageAverage) +"\n" )
            ageCount = 0
            ageValue = 0
       
    ageValue += age
    thisKey = year
    ageCount += 1

        

# We are finding the average value of the age for each year
#for keyItem,value in AverageDictionary.items():
    #ageSum = sum(value)
   # averageAge = ageSum/len(value) 
   # reducerOutput.write(keyItem +'\t'+ str(averageAge) + "\n" )
    # 
    #print(keyItem +'\t'+ str(averageAge) +"\n" )
reducerInput.close()
reducerOutput.close()
# Closing both the read only and write files