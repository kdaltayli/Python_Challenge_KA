# main_script
import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csv_path=os.path.join('Resources','budget_data.csv')
#prev_revenue=row[1]

revenue_change_list=[]
total_amount=0.0
length_of_month=[]
profit=[]
total_revenue=0.0
months=[]

with open(csv_path) as csvfile:
        csv_reader=csv.reader(csvfile, delimiter=',')
       
        csv_header=next(csv_reader)
        first_row = next(csv_reader)
        length_of_month.append(first_row[0])

        total_revenue=float(first_row[1])

        prev_revenue = int(first_row[1])
        for row in csv_reader:

            months.append(row[0])
            length_of_month.append(row[0])

            profit.append(row[1])
            
            total_revenue=int(total_revenue)+int(row[1])
           
            revenue_change=int(row[1])-prev_revenue

            prev_revenue=int(row[1])
            
            # revenue_change_list=revenue_change_list + [revenue_change]
            revenue_change_list.append(revenue_change)
        
        Greatest_increase=max(revenue_change_list)
        Greatest_decrease=min(revenue_change_list)
            
        max_index = revenue_change_list.index(Greatest_increase)
        greatest_increase_date=months[max_index]

        min_index=revenue_change_list.index(Greatest_decrease)
        greatest_decrease_date=months[min_index]
        
         
revenue_average=round(sum(revenue_change_list) / len(revenue_change_list),2)
print("FINANCIAL ANALYSIS")

print("------------------------")

print(f"Total Months is  {len(length_of_month)} \n"
f"The Total Revenue is :  {total_revenue} \n"
f"Revenue Average is {revenue_average}\n"
f"Greatest Increase in Profits {greatest_increase_date} {Greatest_increase}\n"
f"Greatest Decrease in Profits {greatest_decrease_date}  {Greatest_decrease}")







