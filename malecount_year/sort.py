mapperoutput = open("mapperoutput.txt", "r")
reducerinput = open("reducerinput.txt", "w")

lines = mapperoutput.readlines()
lines.sort()

for line in lines:
  reducerinput.write(line)

mapperoutput.close()
reducerinput.close()