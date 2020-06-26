# main_script for PyPoll

import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
csv_path=os.path.join('Resources','election_data.csv')

def percentage(part,whole):
    return round(100 * float(part)/float(whole),2)

total_vote=[]
candidates=["Khan","Li","Correy","O'Tooley"]
candidates_total=[]
total_Khan=0.0
total_Li=0.0
total_Correy=0.0
total_OTooley=0.0
with open(csv_path) as csvfile:

    csv_reader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvfile)

    for row in csv_reader:
        total_vote.append(row[1])

        if row[2]==candidates[0]:
            total_Khan=total_Khan+1
            
        elif row[2]==candidates[1]:
            total_Li=total_Li+1
            
        elif row[2]==candidates[2]:
            total_Correy=total_Correy+1
            
        elif row[2]==candidates[3]:
            total_OTooley=total_OTooley+1
            
candidates_total.append(total_Khan)
candidates_total.append(total_Li)
candidates_total.append(total_Correy)
candidates_total.append(total_OTooley)

# greatest_vote=max(total_Khan,total_Li,total_OTooley,total_Correy)
greatest_vol=max(candidates_total)
max_index=candidates_total.index(greatest_vol)
winner=candidates[max_index]

print("ELECTION RESULTS")
print("------------------")
print(f"The total Votes is   {len(total_vote)}")
print("------------------")
print(f"Total Khan % is {percentage(total_Khan,len(total_vote))} {total_Khan}\n"
    f"Total Li is {percentage(total_Li,len(total_vote))}  {total_Li}\n"
    f"Total Correy is {percentage(total_Correy,len(total_vote))} {total_Correy}\n"
    f"Total OTooley is {percentage(total_OTooley,len(total_vote))} {total_OTooley}")
print("------------------")
print("The Winner is .....     " + winner)
