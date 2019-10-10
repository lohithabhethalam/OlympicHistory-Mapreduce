o = open("PoojithaMapperOutput.txt", "r")
s = open("PoojithaSorterOutput.txt", "w")

lines = o.readlines()
lines.sort()

for line in lines:
  s.write(line)
  print(line)

o.close()
s.close()