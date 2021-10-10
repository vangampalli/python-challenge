import os
import csv

budget_data = os.path.join("..", "python-challenge", "PyBank", "Resources", "budget_data.csv")

month = []
money = 0
money_list = []
money_list_ints = []
differences = []

with open(budget_data, "r") as csv_file:
    csv.reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

    

    for row in csv.reader: 
        month.append(row[0])
        money_list.append(row[1])
        money += int(row[1])

    money_list_ints = list(map(int, money_list))

    #for i in range(0, len(money_list)):
    #   money_list_ints[i] = int(money_list[i])
    
    for x in range(len(money_list_ints)-1):
       differences.append((money_list_ints[x+1]) - (money_list_ints[x]))
    
increase = max(differences)
decrease = min(differences)

increase_month = differences.index(increase)+1
decrease_month = differences.index(decrease)+1
increase_month_str = month[increase_month]
decrease_month_str = month[decrease_month]

print("Financial Analysis")
#print(f"Header {csv_header}")
print(f"Total Months: {len(month)}")
print(f"Total Value: ${(money)}")
print(f"Greatest Increase in Profits: {(increase_month_str)} ${(increase)}")
print(f"Greatest Decrease in Profits: {(decrease_month_str)} ${(decrease)}")

#print(money_list)
#print(money_list_ints)
#print(differences)

#PyBank_output = os.path.join(("..", "Desktop",  "python-challenge", "PyBank", "Analysis", "Financial_Analysis.txt")

with open("/Users/Vanga/Desktop/python-challenge/PyBank/Analysis/financial_analysis.txt", "w") as data:
    data.write(f"Financial Analysis")
    data.write("\n") 
    data.write("-------------------------")
    data.write("\n") 
    data.write(f"Total Months: {len(month)}")
    data.write("\n") 
    data.write(f"Total Value: ${(money)}") 
    data.write("\n") 
    data.write(f"Greatest Increase in Profits: {(increase_month_str)} ${(increase)}")  
    data.write("\n")
    data.write(f"Greatest Decrease in Profits: {(decrease_month_str)} ${(decrease)}")   



