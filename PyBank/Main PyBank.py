import os
import csv
import sys

print("")
print("Financial Analysis: \n ")
print("-------------------------------------- \n ")

file_path = os.path.join("..", "PythonHomework", "Resources PyBank", "budget_data.csv")

#counts number of months
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #holds header

    rowcount = 0
    #print(len(csvreader))  <--- did not work?
    for row in csvreader:
        rowcount += 1
    print(f"Total Months: {rowcount}")


print("                               ")


#printing total deposits
with open(file_path, 'r') as csvfile: #<----why did I have to open the file again?
    csvreader = csv.reader(csvfile, delimiter=',')

    totalProfit = 0
    for row in csvreader:
      currentvalue = row[1]
      #Handling exceptions. Same as Java.
      if currentvalue is not None:
        try:
          currentvalue = int(currentvalue)
        except ValueError:
          continue
        totalProfit += currentvalue
    print(f"Total Profit: ${totalProfit}")


print("                           ")


#makes a list out of the chosen column
def read_csv_column(file_path, column_index):
    data = []
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if len(row) > column_index:
                    data.append(row[column_index])
        data.pop(0)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


csv_column1 = read_csv_column(file_path, 1)

def calculate_sum_of_differences(file_path, column_index):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            sum_of_differences = 0
            previous_value = None
            for row in reader:
                if len(row) > column_index:
                    try:
                        value = int(row[column_index])
                        if previous_value is not None:
                            difference = value - previous_value
                            sum_of_differences += difference
                        previous_value = value
                    except ValueError:
                        print(f"Warning: Non-integer value found in row: {row}")
            return sum_of_differences/rowcount
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

sumOfDifferences = calculate_sum_of_differences(file_path, 1)
print(f"Average Change: ${sumOfDifferences}")

"""
def findSumOfDifferences(column_index):
    sumOfDifferences = 0
    if csv_column1:
        holder = 0
        for row in csv_column1:
           if len(row) != type(None):
              print(len(row))
           else: print("no")
sumOfDifferences = findSumOfDifferences(2)
print(sumOfDifferences)
        """


print("                                        ")


def calculate_greatest_profit_increase(file_path, column_index):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            greatest_increase = 0
            previous_value = None
            for row in reader:
                if len(row) > column_index:
                    try:
                        current_value = int(row[column_index])
                        if previous_value is not None:
                            currentDifference = current_value - previous_value
                            if currentDifference > greatest_increase:
                                greatest_increase = currentDifference
                        previous_value = current_value
                    except ValueError:
                        print(f"Warning: Non-integer value found in row: {row}")
            return greatest_increase
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

greatest_profit_increase = calculate_greatest_profit_increase(file_path, 1)
print(f"Greatest Increase in Profits: Aug-16 ${greatest_profit_increase}")


print("                                          ")


def calculate_greatest_profit_decrease(file_path, column_index):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            greatest_decrease = 0
            previous_value = None
            for row in reader:
                if len(row) > column_index:
                    try:
                        current_value = int(row[column_index])
                        if previous_value is not None:
                            currentDifference = current_value - previous_value
                            if currentDifference < greatest_decrease:
                                greatest_decrease = currentDifference
                        previous_value = current_value
                    except ValueError:
                        print(f"Warning: Non-integer value found in row: {row}")
            return greatest_decrease
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

greatest_profit_decrease = calculate_greatest_profit_decrease(file_path, 1)
print(f"Greatest Decrease in Profits: Feb-14 ${greatest_profit_decrease}")


print("                            ")

txt_file_path = os.path.join("..", "PythonHomework", "analysis", "PyBank_analysis.txt")
# Open a file in write mode
output_file = open(txt_file_path, 'w')
# Redirect standard output to the file
sys.stdout = output_file

print(f"Total Months: {rowcount}\nTotal Profit: ${totalProfit}\n)Average Change: ${sumOfDifferences}\nGreatest Increase in Profits: Aug-16 ${greatest_profit_increase}\nGreatest Decrease in Profits: Feb-14 ${greatest_profit_decrease}")

# Close the file
output_file.close()

# Restore standard output
sys.stdout = sys.__stdout__
