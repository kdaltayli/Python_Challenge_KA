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
candidate_list=[]
percentage_list=[]
candidate_vote=[]
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


# candidates_dict.keys[candidates_dict.values.index("max_value")]
for candidate in candidates_dict.keys():

    percentage_candidate=percentage(candidates_dict[candidate],total_vote)
    candidate_list.append(candidate)
    percentage_list.append(percentage_candidate)
    candidate_vote.append(candidates_dict[candidate])
    print(f"{candidate} {percentage_candidate}% ({candidates_dict[candidate]})")

result_file=zip(candidate_list,percentage_list,candidate_vote)

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
    for row in zip(result_file):
        
        a,b,c=row[0]
        print(a)
        final_result=(f" {a}{b}% ({c}) \n ")
        text.write(f" {final_result}")
    text.write("--------------------\n")
    text.write(f"The Winner is {max_keys} ({max_value}) ")