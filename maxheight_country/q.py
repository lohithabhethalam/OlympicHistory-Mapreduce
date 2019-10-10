s = open("PoojithaSorterOutput.txt","r")
r = open("PoojithaReducerOutput.txt", "w")

thisKey = ""
thisValue = 0

for line in s:
  data = line.strip().split('\t')
  city, height = data
  if str(height) == 'NA':
    height = 0
    
  if city != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')
      print(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = city 
    thisValue = 0
  
  # apply the aggregation function
  max = 0
  if thisValue > max:
    max = thisValue

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')
print(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()