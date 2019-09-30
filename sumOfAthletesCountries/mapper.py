s = open("../data/athlete_events.txt","r")
r = open("mapperOutput.txt", "w")
lines = s.readlines()
lines.sort()
for line in lines:
    data = line.strip().split('\t')
    name = data[1]
    year = data[9]
    country = data[6]
    r.write(name +'\t'+ year + '\t' + country + '\n')
    print(name +'\t'+ year + '\t' + country + '\n')

s.close()
r.close()