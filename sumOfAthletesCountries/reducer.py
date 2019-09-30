# read the contents of mapperOutput.txt for input
s = open("mapperOutput.txt","r")
# write output into reducerOutput.txt
r = open("reducerOutput.txt", "w")
# create a dictionary with empty key-value pairs
thisDict = {}
# read each line in input file
for line in s:
    data = line.strip().split('\t')
    name = data[0]
    year = data[1]
    country = data[2]
    # if country matches the previous country key in dictionary increment the key value with existing country value
    if country in thisDict.keys():
        thisDict[country] = thisDict[country] + 1
    # if country doesnt match the previous country key in dictionary then consider key value as one
    else:
        thisDict[country] = 1 
       

# print the output contents into reducerOutput.txt

for keyItem,value in thisDict.items():
    r.write(keyItem +'\t'+ str(value) + "\n" )
    print(keyItem +'\t'+ str(value) +"\n" )
# close mapperOutput.txt and reducerOutput.txt
s.close()
r.close()