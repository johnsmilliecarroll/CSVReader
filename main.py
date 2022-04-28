import csv
import sys

#  set up CSV
filename = str(sys.argv[1])
print("Reading " + filename)
myfile = open(filename)  # load first arg
mycsv = csv.DictReader(myfile)  # read file

#  look for the Columns we need in the file
createNewFiles = False
requiredCols = ["Institution", "Team", "City", "State", "Country", "Advisor", "Problem", "Ranking"]
myDict = {}  # dictionary to use to get the value our csv uses for our required column values
for col in mycsv:
    for i in range(0, len(col)):  # check if the csv file columns have names that include our required names
        for j in range(0, len(requiredCols)):
            if requiredCols[j].lower() in list(col)[i].lower():
                myDict[requiredCols[j]] = list(col)[i]
                break
    break  # only want header values

if len(requiredCols) == len(myDict): #we have all our columns
    createNewFiles = True
if not createNewFiles: # we dont have all our columns
    print("The columns of the input file are too ambiguous to be used. Please use a file that "
          "includes aptly named columns for Institution, Team Number, City, State/Province, Country, Advisor, "
          "Problem, and Ranking.")
else:
    splitName = filename.split('.')  # get file name without .csv
    instfilename = splitName[0] + 'institutions.csv'  # create names for our files
    teamfilename = splitName[0] + 'teams.csv'

    # open files in create or write mode, so if the file already exists it will overwrite
    # newline='' is apparently needed in Windows to suppress an extra blank line being appended after every row
    instfile = open(instfilename, 'w', newline='')
    teamfile = open(teamfilename, 'w', newline='')

    instwriter = csv.writer(instfile)  # writers
    teamwriter = csv.writer(teamfile)

    instwriter.writerow(["ID", "Name", "City", "State/Province", "Country"])  # headers
    teamwriter.writerow(["ID", "Advisor", "Problem", "Ranking", "InstitutionID"])

    instID = 0  # id value to increment
    institutions = {}  # dictionary to keep track of institutions

    for col in mycsv:
        instrow = []
        teamrow = []
        instval = col[myDict['Institution']]  # institution name
        if instval not in institutions:  # only append if it's a new unique name
            institutions[instval] = instID  # create dictionary entry
        instrow.append(instID)  # add the values
        instrow.append(instval)
        instrow.append(col[myDict['City']])
        instrow.append(col[myDict['State']])
        instrow.append(col[myDict['Country']])
        instwriter.writerow(instrow)
        instID += 1  # increment id number
        teamrow.append(col[myDict['Team']])
        teamrow.append(col[myDict['Advisor']])
        teamrow.append(col[myDict['Problem']])
        teamrow.append(col[myDict['Ranking']])
        teamrow.append(institutions[instval])
        teamwriter.writerow(teamrow)

    # close files

    myfile.close()
    instfile.close()
    teamfile.close()

    print("Successfully created files " + instfilename + " and " + teamfilename)
