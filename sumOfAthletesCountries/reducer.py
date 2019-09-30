s = open("mapperOutput.txt","r")
r = open("reducerOutput.txt", "w")

thisDict = {}
for line in s:
    data = line.strip().split('\t')
    name = data[0]
    year = data[1]
    country = data[2]
    
    if country in thisDict.keys():
        thisDict[country] = thisDict[country] + 1
    else:
        thisDict[country] = 1 
       

#print(thisDict.items())

for keyItem,value in thisDict.items():
    r.write(keyItem +'\t'+ str(value) + "\n" )
    print(keyItem +'\t'+ str(value) +"\n" )

s.close()
r.close()