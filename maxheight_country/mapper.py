f = open("athlete_events.txt","r")  
# open and read contents of this file
o = open("PoojithaMapperOutput.txt","w")
 # open and write into this file
for line in f:  
    data = line.strip().split("	") 
    # We are seperating the coloumns using the spaces
    if len(data) == 15:
        ID, Name, Sex, Age, Height, Weight, Team, NOC, Games, Year, Season, City, Sport, Event, Medal = data
        o.write("{0}\t{1}\n".format(City, Height))
        # Seperate city and height from rest of the data and write it to the given file
       # print("{0}\t{1}\n".format(City, Height))
f.close()
o.close()
# Closing both the read only and write files.














