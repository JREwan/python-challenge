# Option 3: PyBoss

# In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

# Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:
# 	Emp ID,Name,DOB,SSN,State
# 	214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# Then convert and export the data to use the following format instead:
#
# 	Emp ID,First Name,Last Name,DOB,SSN,State
# 	214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 	
# In summary, the required conversions are as follows:
#
# The Name column should be split into separate First Name and Last Name columns.
# The DOB data should be re-written into DD/MM/YYYY format.
# The SSN data should be re-written such that the first five numbers are hidden from view.
# The State data should be re-written as simple two-letter abbreviations.
# Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.
#
#
#-----------------------------------------------------------

#-----------------------------------------------------------
# Imports
#-----------------------------------------------------------
import os
import csv
from datetime import datetime
from dateutil.parser import parse

#-----------------------------------------------------------
# Viariables and lists
#-----------------------------------------------------------
EmpId = 0 
EmpName = " "
EmpFirstName = " "
EmpLastName = " "
oldDOB = " "
DOB = " "
SSN = " "
SSN1 = " "
SSN2 = " "
SSN3 = " "
State = " "
StateAbbr = " "
#-----------------------------------------------------------
# Python disctionary for state abbreviations
#-----------------------------------------------------------
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}

#-----------------------------------------------------------
# Set the path to my input files
#-----------------------------------------------------------
emp_file_1 = os.path.join("raw_data", "employee_data1.csv")
#-----------------------------------------------------------
# Specify the file to write to
#-----------------------------------------------------------
output_path = os.path.join('Results', 'MergedFileJRE.csv')
#-----------------------------------------------------------
# open the output file in write mode
#-----------------------------------------------------------
with open(output_path, 'w', newline='') as OutputFile:
        # initialize
        csvwriter = csv.writer(OutputFile, delimiter=',')
        # Write the first row (column headers)
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
#----------------------------------------------------------
# Process the first file
# 
# Import the employee_data1.csv file, which currently holds employee records like the below:
# 	Emp ID,Name,DOB,SSN,State
# 	214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#
# The required conversions are as follows:
#       Emp ID, First Name, Last Name, DOB (DD/MM/YYYY), SSN (XXX-XX-1234), State (IL)
# ---------------------------------------------------------
with open(emp_file_1, newline="") as csvfile:
        # CSV Reader
        csvreader = csv.reader(csvfile, delimiter=',')
        first_row = next(csvreader)
        for CurrentRow in csvreader:
                EmpId = CurrentRow[0]
                EmpName = CurrentRow[1]
                EmpFirstName, EmpLastName = EmpName.split(" ")
                oldDOB = datetime.strptime(CurrentRow[2], '%Y-%m-%d')
                DOB = oldDOB.strftime('%d/%m/%Y')
                SSN1, SSN2, SSN3 = CurrentRow[3].split("-")
                SSN = "XXX-XX-" + str(SSN3)
                State = CurrentRow[4]
                StateAbbr = us_state_abbrev[State]
                #print(EmpId, EmpName)
                with open(output_path, 'a', newline='') as OutputFile:
                        csvwriter = csv.writer(OutputFile, delimiter=',')
                        # Write the row
                        csvwriter.writerow([EmpId, EmpFirstName, EmpLastName, DOB, SSN, StateAbbr])

#-----------------------------------------------------------------------------------------------------------------
# Process the second file
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------
# Set the path to my input files
#-----------------------------------------------------------
emp_file_2 = os.path.join("raw_data", "employee_data2.csv")

#----------------------------------------------------------
# Process the second file
# The required conversions are as follows:
#       Emp ID, First Name, Last Name, DOB (DD/MM/YYYY), SSN (XXX-XX-1234), State (IL)
# ---------------------------------------------------------
with open(emp_file_2, newline="") as csvfile:
        # CSV Reader
        csvreader = csv.reader(csvfile, delimiter=',')
        first_row = next(csvreader)
        for CurrentRow in csvreader:
                EmpId = CurrentRow[0]
                EmpName = CurrentRow[1]
                EmpFirstName, EmpLastName = EmpName.split(" ")
                oldDOB = datetime.strptime(CurrentRow[2], '%Y-%m-%d')
                DOB = oldDOB.strftime('%d/%m/%Y')
                SSN1, SSN2, SSN3 = CurrentRow[3].split("-")
                SSN = "XXX-XX-" + str(SSN3)
                State = CurrentRow[4]
                StateAbbr = us_state_abbrev[State]
                #print(EmpId, EmpName)
                with open(output_path, 'a', newline='') as OutputFile:
                        csvwriter = csv.writer(OutputFile, delimiter=',')
                        # Write the row
                        csvwriter.writerow([EmpId, EmpFirstName, EmpLastName, DOB, SSN, StateAbbr])

