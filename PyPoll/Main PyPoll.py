import os
import csv
import sys

stockham = "Charles Casper Stockham"


print("")
print("Election Results: \n ")
print("-------------------------------------- \n ")

file_path = os.path.join("..", "PythonHomework", "Resources PyPoll", "election_data.csv")

#counts number of votes
def count_csv_column(file_path, column_index):
    try:
        #opens file
        with open(file_path, 'r') as csv_file:
            #reads file
            reader = csv.reader(csv_file)
            #skips header
            header = next(reader)
            #counts each row
            row_count = 0
            for row in reader:
                row_count += 1
        return row_count
    #Handles Exceptions
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

row_count = count_csv_column(file_path, 0)
print(f"Total Votes: {row_count}")

print("")
print("-------------------------------------- \n ")

candidate = ""
def Count_Votes_for_Candidate(file_path, name, column_index):
    try:
        count = 0
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) > column_index and row[column_index] == name:
                    count += 1
        return count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

stockham = "Charles Casper Stockham"
stockam_vote_count = Count_Votes_for_Candidate(file_path, stockham, 2)
stockam_vote_count_percentage = round(100*stockam_vote_count/row_count, 3)
print(f"Charles Casper Stockham: %{stockam_vote_count_percentage}  ({stockam_vote_count})")


def Count_Votes_for_Candidate(file_path, name, column_index):
    try:
        count = 0
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) > column_index and row[column_index] == name:
                    count += 1
        return count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

print("")
degette = "Diana DeGette"
degette_vote_count = Count_Votes_for_Candidate(file_path, degette, 2)
degette_vote_count_percentage = round(100*degette_vote_count/row_count, 3)
print(f"Diana DeGette: %{degette_vote_count_percentage}  ({degette_vote_count})\n")

doane = "Raymon Anthony Doane"
doane_vote_count = Count_Votes_for_Candidate(file_path, doane, 2)
doane_vote_count_percentage = round(100*doane_vote_count/row_count, 3)
print(f"Raymon Anthony Doane: %{doane_vote_count_percentage}  ({doane_vote_count})")

print("\n -------------------------------------- \n ")

if doane_vote_count > degette_vote_count and doane_vote_count > stockam_vote_count: 
    winner = doane
    print(f"Winner: {doane}")
elif degette_vote_count > doane_vote_count and degette_vote_count > stockam_vote_count: 
    winner = degette
    print(f"Winner: {degette}")
else: 
    winner = stockham
    print(f"Winner: {stockham}")
print("\n --------------------------------------\n")


txt_file_path = os.path.join("..", "PythonHomework", "analysis", "PyPoll_analysis.txt")
# Open a file in write mode
output_file = open(txt_file_path, 'w')
# Redirect standard output to the file
sys.stdout = output_file

print(f"Total Votes: {row_count}\nCharles Casper Stockham: {stockam_vote_count_percentage}({stockam_vote_count})\nRaymon Anthony Doane: {doane_vote_count_percentage}({doane_vote_count})\nDiana DeGette: {degette_vote_count_percentage}({degette_vote_count})\nWinner: {winner}")

# Close the file
output_file.close()

# Restore standard output
sys.stdout = sys.__stdout__
