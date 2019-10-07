reducerinput = open("mapperoutput.txt","r")
reduceroutput = open("reduceroutput.txt", "w")

thisKey = ""
thisValue = 0.0
count = 0
for line in reducerinput:
  data = line.strip().split('\t')
  year, gender = data
  #payment, cost = data

  if year != thisKey:
    if thisKey:
      # output the last key value pair result
      reduceroutput.write(thisKey + '\t'  +str(thisValue) +'\n')

    # start over when changing keys
    thisKey = year 
    thisValue = 0.0
  
  # apply the aggregation function
  
  if str(gender) = 'M':
    thisValue += float(count)
    count += 1

# output the final entry when done
reduceroutput.write(thisKey + '\t'+ str(thisValue) + '\n')

reducerinput.close()
reduceroutput.close()
