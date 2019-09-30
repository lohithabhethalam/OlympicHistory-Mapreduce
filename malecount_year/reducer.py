# open and read contents of s.txt for input
reducerinput = open("mapperoutput.txt","r")
# write output contents in result.txt
reduceroutput = open("reduceroutput.txt", "w")
# sort the contents of reducerinput
lines = reducerinput.readlines()
lines.sort()
# set variable malecount value to 0
maleCount = 0
# create new dictionary with empty key, value pairs
thisDictionary = {}
# read each line in input file
for line in lines:
    # separate columns in data 
    data = line.strip().split('\t')
    year = data[0]
    gender = data[1]
    # if gender is male and if year key in the dictionary is equal to the previous year key increment year key with 1
    if year in thisDictionary.keys():
         if str(gender) == 'M':
            thisDictionary[year] = thisDictionary[year] + 1
    # else if gender is male and if year key in the dictionary is not equal to the previous year key initialize year key in dictionary to 1 
    else:
         if str(gender) == 'M':
             thisDictionary[year] = 1
   
        
# write the output contents in results.txt

for keyItem,value in thisDictionary.items():

    reduceroutput.write("Year: "+keyItem+"\t"+"count of male people: "+str(value) +"\n")
# close mapperoutput.txt and reduceroutput.txt
reducerinput.close()
reduceroutput.close()
