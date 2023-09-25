# module 3 
# total number of months included in the dataset 
# the net total amount of profit/losses over the entire period 
# greatest increase in profits (date & amount) over the entire period 
# greatest decrease in profits (date & amount) over the entire period

# import the csv file 
import csv
from pathlib import Path 

#stating the csv file's path 
csv_path = Path("budget_data.csv")

# declare the variables 
general_profit_loss = 0
prev_month_profit_loss = 0 
# calculate the number of months 
change_in_profit_loss = []
months = []


# read the CSV file 
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    #skip the header! 
    next(csvreader)
    for row in csvreader: 
        # extract data from the current row 
        date, profit_loss = row[0], int(row[1])
        months.append(date)
        # calc the change in profit & loss in prev month
        if prev_month_profit_loss != 0:
            change = profit_loss - prev_month_profit_loss
            change_in_profit_loss.append(change)

        #calc the profit & loss 
        general_profit_loss += profit_loss

        #store the current month's profit/loss for the next comparsion 
        prev_month_profit_loss = profit_loss


#calc the total number of months 
total_months = len(months)





# find the greatest increase & greates decrease for profits/losses
great_increase = max(change_in_profit_loss)
great_decrease = min(change_in_profit_loss)
#find the months of greates profit/ loss 
greatest_increase_month = months[change_in_profit_loss.index(great_increase)]
greatest_decrease_month = months[change_in_profit_loss.index(great_decrease)]

#finding the average
avg_change = round(sum(change_in_profit_loss) / len(change_in_profit_loss),2)


# print the results like the image 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months} ")
print(f"Total: ${general_profit_loss}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${great_increase}")
print(f"Greatest Increase in Losses: {greatest_decrease_month} ${great_decrease}")

# the outputs 
with open("budget_analysis.txt", "w") as textfile: 
    textfile.write("Finacial Analysis\n")
    textfile.write("--------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${general_profit_loss}\n")
    textfile.write(f"Average Change: ${avg_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} ${great_increase}\n")
    textfile.write(f"Greatest Increase in Losses: {greatest_decrease_month} ${great_decrease}\n")
