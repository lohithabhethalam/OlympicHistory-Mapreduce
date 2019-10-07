# read the contents of mapperOutput.txt for input
s = open("mapperOutput.txt","r")
# write output into reducerOutput.txt
r = open("reducerOutput.txt", "w")
# create a dictionary with empty key-value pairs
thisKey = ""
oldKey = ""
value = 0
# read each line in input file
sortedData = s.readlines() 
sortedData.sort()
r.write("Country" +'\t'+ "Sum of Countries" + "\n" )
for line in sortedData:
    data = line.strip().split('\t')
    name = data[2]
    year = data[1]
    country = data[0]
    # if country doesnot match with thiskey then goes into conditional loops
    if thisKey != country:
        #if thiskey exists print and write output to file
        if thisKey:
            # print the output contents into reducerOutput.txt
            print(thisKey +'\t'+ str(value) +"\n" )
            r.write(thisKey +'\t'+ str(value) +"\n" )
            value = 0
        
    # if this key equals country then add country to thiskey and increment the value
    thisKey = country
    value += 1
        
       
# close mapperOutput.txt and reducerOutput.txt
s.close()
r.close()
