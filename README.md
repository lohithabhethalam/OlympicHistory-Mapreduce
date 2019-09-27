# Olympic History
We are working on this project for Bigdata course. Our project number is 05. 
## List of developers
- Gangadhar Adusumalli
- Lohitha Bhethalam
- Poojitha Singam
- Divyaharshini Bheemireddy
## Links
- https://github.com/lohithabhethalam/project
- https://github.com/lohithabhethalam/project/issues
## Introduction
This project is used to implement map reduce functionality on our bigdata source Olympic history.The reason why we chose olympic history as our datasource is because they are many columns which gave us multiple options to map reduce.
## Datasource
Our datasource provides 120 years historic information of Olympic games.Datasource provides 120 years of data.The datasource is structured in excel sheet. 
## Link to datasource
- https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results
## The challange
What makes it a big data problem? 
- Volume: There is 5MB of data in this dataset and 271,000 records. 120 years of Olympic data is available in this source.
- Variety: This dataset is structured and it is in excel format.
- Velocity: Data will be generated based on when the Olympic games were organized.  
- Veracity: Data is very clear. They are no unnecessary columns and the data was collected from www.sports-reference.com and it seems to be trustworthy.
- Value: Using this data source we can evaluate 120 years of Olympic history data including their gender, their year of participation, season, year and all the other information.
## Big Data Questions
- For each year, I'll calculate the count of male people who participated in Olympic games. (Lohitha Bhethalam)
- For each country,I'll find the maximum height of participants. (Poojitha Singam) 
- For each year, Find the average age of players participated in Olympic games. (Divyaharshini Bheemireddy)
- For each country,I will find the sum of all the players particpated in Olympic games. (Gangadhar Adusumalli)

## Big data solutions
one solution per developer.
- Lohitha Bhethalam
  * Mapper input
  One line of data that mapper will read:
  1	A Dijiang	M	24	180	80	China	CHN	1992 Summer	1992	Summer	Barcelona	Basketball	Basketball Men's Basketball	NA
  * Mapper output/reducer input
  example of an intermediate key, value pair output by your mapper:
  1992 M
  1992 F
  1993 M
  1993 M
  1993 F
  * Reducer output
  year = 1992 count of male people = 48
  * Language being used
  The language that I am using for map reducing is "Python".
  * What kind of chart will you use to display your results? 
I will use pie chart to display my results.
