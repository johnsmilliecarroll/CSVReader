A program that takes an input csv for a math competition and creates csv tables for Institutions and Teams. 
## How to use:

In the same folder as main.py, place the csv file you'd like to read. Next, run main.py via command line with the name of the file as the first argument.

So if the file you would like to parse is named 2015.csv, this is what you should run.

    % python main.py 2015.csv

It will create two output files, appending institutions and teams the name of the input file. In this case it will be 2015institutions.csv and 2015teams.csv. Running the program again with the same args will overwrite these files.

The institution file contains information on institutions included in the input file. The teams file has information relating to the teams.

Institutions: "Institution ID", "Institution Name", "City", "State/Province", and "Country".

Teams: "Team Number", "Advisor", "Problem", "Ranking", and "Institution ID"

### Limitations
This program requires some amount of standardization between files can can be used as inputs. This program will look through the input csv file and attempt to match the column names with the columns that are required to create the new files. If the column name doesn't include a specific keyword the program will not work. These are the keywords that the program will check for: "Institution", "Team", "City", "State", "Country", "Advisor", "Problem", "Ranking".

Also, the program has no way of checking for typos in any of the names of the Institutions. If an institution is spelled differently it will be inserted to the file as a new institution.