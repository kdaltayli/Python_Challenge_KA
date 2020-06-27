# main_script for PyPoll

import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
csv_path=os.path.join('Resources','election_data.csv')

def percentage(number,whole):
    return round(100 * float(number)/float(whole),2)

total_vote=0.0

# created candidate dictionary
candidates_dict={}

with open(csv_path) as csvfile:

    csv_reader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvfile)
    
    for row in csv_reader:
        total_vote=total_vote+1

        if row[2] not in  candidates_dict:

            candidates_dict[row[2]]=1
            
        else: 
            candidates_dict[row[2]]=candidates_dict[row[2]]+1

print(f"ELECTION RESULTS\n"
    f"-----------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"-----------------------------")



for candidate in candidates_dict.keys():

    percentage_candidate=percentage(candidates_dict[candidate],total_vote)

    print(f"{candidate} {percentage_candidate}% ({candidates_dict[candidate]})")

max_value=max(candidates_dict.values())
max_keys=[k for k, candidate in candidates_dict.items() if candidate==max_value]

print(f"-----------------------------\n"
    f"The Winner is {max_keys} ({max_value}) ")


output_path=os.path.join("Analysis_PyPoll","myfile_Analysis.txt")
with open(output_path,'w') as text:
    text.write(f"ELECTION RESULTS\n"
    f"-----------------------------\n"
    f"Total Votes: {total_vote}\n"
    f"-----------------------------")
    text.write("--------------------\n")
    text.write(f" {candidates_dict} \n"
            f"The Winner is {max_keys} ({max_value}) ")