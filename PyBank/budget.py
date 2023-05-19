# To import and get the needed information from the cvs file
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = 'budget_data.csv'
#budget_data_csv = os.path.join('.','budget_data.csv')
#defining the corresponding values as either intergers, lists or strings
total_months = 0
total_profit = 0
profit_changes = []
months = []
average_change = 0
previous_profit = 0
Greatest_increase = 0
Greatest_decrease = 0
Greatest_increase_date = ""
Greatest_decrease_date = ""


#To read the CSV file
with open(budget_data_csv, 'r') as csvfile:

    #Splitting the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        month = row[0]
        profit = int(row[1])
        #looping through the total number of months 
        total_months += 1
        total_profit += profit
        if total_months > 1:
            change = profit - previous_profit
            profit_changes.append(change)
            months.append(month)
            previous_profit = profit
    average_change = sum(profit_changes) / len(profit_changes)
    Greatest_increase = max(profit_changes)
    Greatest_decrease = min(profit_changes)
    Greatest_increase_date =months[profit_changes.index(Greatest_increase)]
    Greatest_decrease_date =months[profit_changes.index(Greatest_decrease)]


#Returning the results into the terminal
print("Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit)}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: ${str(Greatest_increase_date)}, {Greatest_increase}")
print(f"Greatest Decrease in Profits: ${str(Greatest_decrease_date)}, {Greatest_decrease}")

#printing my results in a textfile
#budget_data_csv = os.path.join('.', 'Resources', 'PyBank_Results.txt')
budget_data_csv = 'PyBank_Results.txt'
with open(budget_data_csv, "w") as text_file:
    print("Financial Analysis", file=text_file)
    print(f"----------------------------", file=text_file)
    print(f"Total Months: {str(total_months)}", file=text_file)
    print(f"Total: ${str(total_profit)}", file=text_file)
    print(f"Average Change: ${average_change:.2f}", file=text_file)
    print(f"Greatest Increase in Profits: ${str(Greatest_increase_date)}, {Greatest_increase}", file=text_file)
    print(f"Greatest Decrease in Profits: ${str(Greatest_decrease_date)}, {Greatest_decrease}", file=text_file)



    

