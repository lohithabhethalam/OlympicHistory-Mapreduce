# open data file athlete_events.txt to open datasource
mapperinput = open("../data/athlete_events.txt","r")
# write results in output.txt
mapperoutput = open("mapperoutput.txt", "w")
# open everyline in athlete_events.txt
for line in mapperinput:
  # separate each column in dataset using space between each column in athlete_events.txt
  data = line.strip().split('	')
  # if number of columns in dataset is 15 then separate year and sex columns in datasource and write them in output.txt
  if (len(data) == 15):
    ID, Name, Sex, Age, Height, Weight, Team, NOC, Games, Year, Season, City, Sport, Event, Medal = data
    mapperoutput.write(Year + "\t" + Sex+ "\n")
# close athelete_events.txt and mapperoutput.txt
mapperinput.close()
mapperoutput.close()
