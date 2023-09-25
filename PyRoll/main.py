# mypoll instructions 
# calc the total number of votes cast
# a complete list of candidates who received votes 
# percentage of votes each candidate won 
# the winner of the election based on popular vote 

# import the csv file 
import csv
from pathlib import Path 
import collections 
from collections import Counter 
# import Counter to make it easier on counting elements

csv_path = Path("election_data.csv")


#declare the variables set 
total_voters = []
vote_count_per_candid = []
# list_of_candidates = []

#set your path by grabbing the Path 
#csv_path = Path("Users/vanessav/Downloads/Starter_Code-9/PyPoll/Resources/election_data.csv")

with open(csv_path) as csvfile: 
    # CSV reader needs a variable to hold the content & delimiter 
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    # read the row header 
    csv_header = next(csvreader)

    # after the header, read each row
    for row in csvreader: 
        total_voters.append(row[2])
    
    # Sort the list of list 
    list_of_candidates = sorted(total_voters)

    #use Counter library to find common elements & count them 
    cleaned_list_of_candid = Counter(list_of_candidates)

    # Need to convert Counter object to list, 
    vote_count_per_candid.append(cleaned_list_of_candid.most_common())

    # calc the candidate vote percetnage, 3rd decimal - look at the solution image provided 
    # percentage = ( votes per candidate / number of votes ) * 100 
    for item in vote_count_per_candid: 
        first_place_percetage = format(item[0][1]*100/(sum(cleaned_list_of_candid.values())), '.3f')
        # .3f return to teh 3rd decimal place 
        second_place_percentage = format(item[1][1]*100/(sum(cleaned_list_of_candid.values())), '.3f')
        third_place_percentage = format(item[2][1]*100/(sum(cleaned_list_of_candid.values())), '.3f')


# count the number of total votes * assign it 
total_voter_count = len(total_voters)


# print the results like the image 
print("Election Results")
print("----------------------------")
print(f"Total Votes:  {total_voter_count}")
print("----------------------------")
print(f"{vote_count_per_candid[0][0][0]}: {first_place_percetage}% ({vote_count_per_candid[0][0][1]}\n")
print(f"{vote_count_per_candid[0][1][0]}: {second_place_percentage}% ({vote_count_per_candid[0][1][1]}\n")
print(f"{vote_count_per_candid[0][2][0]}: {third_place_percentage}% ({vote_count_per_candid[0][2][1]}\n)")
print("----------------------------")
print(f"Winner: {vote_count_per_candid[0][0][0]}")
print("------------------------------")

with open("election_data.txt", "w") as output_files: 

    output_files.write("Election Results\n")
    output_files.write("--------------------\n")
    output_files.write(f"Total Votes: :{total_voter_count}\n")
    output_files.write("---------------------\n")
    output_files.write(f"{vote_count_per_candid[0][0][0]}: {first_place_percetage}% ({vote_count_per_candid[0][0][1]}\n)")
    output_files.write(f"{vote_count_per_candid[0][1][0]}: {second_place_percentage}% ({vote_count_per_candid[0][1][1]}\n)")
    output_files.write(f"{vote_count_per_candid[0][2][0]}: {third_place_percentage}% ({vote_count_per_candid[0][2][1]}\n)")
    output_files.write("--------------------\n")
    output_files.write(f"Winner: {vote_count_per_candid[0][0][0]}\n")
    output_files.write("-------------------\n")


