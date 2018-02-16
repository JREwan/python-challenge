#-----------------------------------------------------------
#
# Before You Begin
#  1. Create a new GitHub repo called python-challenge. Then, clone it to your computer.
#  2. Inside your local git repository, create a directory for 2 of the 4 Python Challenges. Use folder names corresponding to the 2 challenges that you have chosen to complete: PyBank, PyPoll, PyBoss, or PyParagraph.
#  3. Inside of each folder that you just created, add a new file called main.py. This will be the main script to run for each analysis.
#  4. Push the above changes to GitHub.
#
# Option 1: PyBank
#
# In this challenge, you are tasked with creating a Python script for analyzing 
# the financial records of your company. You will be given two sets of revenue 
# data (budget_data_1.csv and budget_data_2.csv).
#
# Each dataset is composed of two columns: 
#  - Date (NOTE: date format changes!)
#  - Revenue. 
#   (Thankfully, your company has rather lax standards for accounting so the 
#   records are simple.)
#
# Your task is to create a Python script that analyzes the records to calculate 
# each of the following:
#  •	The total number of months included in the dataset
#  •	The total amount of revenue gained over the entire period
#  •	The average change in revenue between months over the entire period
#  •	The greatest increase in revenue (date and amount) over the entire period
#  •	The greatest decrease in revenue (date and amount) over the entire period
#
# Your final script must be able to handle any such similarly structured dataset
# in the future (your boss is going to give you more of these -- so your script
# has to work for the ones to come). In addition, your final script should both 
# print the analysis to the terminal and export a text file with the results.
#
#-----------------------------------------------------------

#-----------------------------------------------------------
# Imports
#-----------------------------------------------------------
import os
import csv

#-----------------------------------------------------------
# Viariables and lists
#-----------------------------------------------------------
File1Revenue = 0
File1RowCount = 0
File1Ave = 0
File2Revenue = 0
File2RowCount = 0
File2Ave = 0
MaxMonthRev = 0
PrevMonthRev = 0
BiggestRevIncrease = 0
BiggestRevDecrease = 0
MaxMonthRev2 = 0
PrevMonthRev2 = 0
BiggestRevIncrease2 = 0
BiggestRevDecrease2 = 0
SumOfMonthChange1 = 0
SumOfMonthChange2 = 0

#-----------------------------------------------------------
# Set the path to my input files
#-----------------------------------------------------------
DataFile1_csv = os.path.join("raw_data", "budget_data_1.csv")
# DataFile2_csv = os.path.join("raw_data", "budget_data_2.csv")

#----------------------------------------------------------
# Process the first file
# - get the sum
# - get the row count
# - determine file average
# - identify max change month and amount
# ---------------------------------------------------------
with open(DataFile1_csv, newline="") as csvfile:
        # CSV Reader
        csvreader = csv.reader(csvfile, delimiter=',')
        
        first_row = next(csvreader)
        for CurrentRow in csvreader:
                File1Revenue = File1Revenue + int(CurrentRow[1])
                File1RowCount = File1RowCount + 1
                Monthchange = int(CurrentRow[1]) - int(PrevMonthRev)
                SumOfMonthChange1 = Monthchange + SumOfMonthChange1
                if Monthchange >= 0:
                        if Monthchange >= BiggestRevIncrease :
                                BiggestRevIncrease = Monthchange
                                MonthBiggestIncrease = CurrentRow[0]
                else:
                        if Monthchange <= BiggestRevDecrease :
                                BiggestRevDecrease = Monthchange
                                MonthBiggestDecrease = CurrentRow[0]
                #print(CurrentRow)
                PrevMonthRev = CurrentRow[1]
                #if int(CurrentRow[1]) >= int(MaxMonthRev):
                #        MaxMonthRev = CurrentRow[1]
                #        MaxRevMonth = CurrentRow[0]

                
File1Ave = SumOfMonthChange1/File1RowCount

#-----------------------------------------------------------------------------------------------------------------
# Process the second file
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------
# Set the path to my input files
#-----------------------------------------------------------
DataFile2_csv = os.path.join("raw_data", "budget_data_2.csv")

#----------------------------------------------------------
# - get the sum
# - get the row count
# - determine file average
# - identify max change month and amount
# ---------------------------------------------------------
with open(DataFile2_csv, newline="") as csvfile:
        # CSV Reader
        csvreader = csv.reader(csvfile, delimiter=',')
        
        first_row = next(csvreader)
        for CurrentRow in csvreader:
                File2Revenue = File2Revenue + int(CurrentRow[1])
                File2RowCount = File2RowCount + 1
                Monthchange2 = int(CurrentRow[1]) - int(PrevMonthRev2)
                SumOfMonthChange2 = Monthchange2 + SumOfMonthChange2
                if Monthchange2 >= 0:
                        if Monthchange2 >= BiggestRevIncrease2 :
                                BiggestRevIncrease2 = Monthchange2
                                MonthBiggestIncrease2 = CurrentRow[0]
                else:
                        if Monthchange2 <= BiggestRevDecrease2 :
                                BiggestRevDecrease2 = Monthchange2
                                MonthBiggestDecrease2 = CurrentRow[0]
                PrevMonthRev2 = CurrentRow[1]
                
                
File2Ave = SumOfMonthChange2/File2RowCount

#-----------------------------------------------------------------------------------------------------------------
# Print the results & write to a text file
#-----------------------------------------------------------------------------------------------------------------
# Specify the file to write to
output_path = os.path.join('results', 'results.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=' ')
    # print, then write to file
    RowToWrite = " "
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 1 ----------"
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 1 total revenue is:  " + str(File1Revenue)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 1 row count is:  " + str(File1RowCount)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 1 average monthly revenue change is:  " + str(File1Ave) + " per month"
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "Max increase in revenue month / amount:  " + str(MonthBiggestIncrease) + " / " + str(BiggestRevIncrease)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "Biggest decrease in revenue month / amount:  " + str(MonthBiggestDecrease) + " / " + str(BiggestRevDecrease)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "End File 1 ------"
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = " "
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 2 ----------"
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 2 total revenue is:  " + str(File2Revenue)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 2 row count is:  " + str(File2RowCount)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "File 2 average monthly revenue change is:  " + str(File2Ave) + " per month"
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "Max increase in revenue month / amount:  " + str(MonthBiggestIncrease2) + " / " + str(BiggestRevIncrease2)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    RowToWrite = "Biggest decrease in revenue month / amount:  " + str(MonthBiggestDecrease2) + " / " + str(BiggestRevDecrease2)
    print(RowToWrite)
    csvwriter.writerow([RowToWrite])
    #txtfile.write(RowToWrite +"\n")
    RowToWrite = "End File 2 ------"
    print(RowToWrite)
    #csvwriter.writerow([RowToWrite])
    txtfile.write(RowToWrite+"\n")
