# read the contents of athlete_events.txt for input
s = open("../data/athlete_events.txt","r")
# write output into reducerInput.txt
r = open("reducerInput.txt", "w")
# read each line in input file
lines = s.readlines()
lines.sort()
# out of all the columns in datasource select only age, year columns as mapper output
for line in lines:
    data = line.strip().split('\t')
    age = data[3]
    year = data[9]
    # write the selected columns into reducerInput.txt
    r.write(age +'\t'+ year + '\n')
    print(age +'\t'+ year + '\n')
# close athlete_events.txt and reducerInput files
s.close()
r.close()