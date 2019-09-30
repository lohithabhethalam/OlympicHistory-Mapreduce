# read the contents of athlete_events.txt for input
s = open("../data/athlete_events.txt","r")
# write output into mapperoutput.txt
r = open("mapperOutput.txt", "w")
# read each line in input file
lines = s.readlines()
lines.sort()
# out of all the columns in datasource select only name, year and country columns as mapper output
for line in lines:
    data = line.strip().split('\t')
    name = data[1]
    year = data[9]
    country = data[6]
    # write the selected columns into mapperOutput.txt
    r.write(name +'\t'+ year + '\t' + country + '\n')
    print(name +'\t'+ year + '\t' + country + '\n')
# close athlete_events.txt and mapperoutput files
s.close()
r.close()