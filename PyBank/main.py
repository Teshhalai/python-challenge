import os
import csv

csvpath = os.path.join(
    '..', 'PyBank', 'PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    revenue = []
    date = []
    rev_change = []

    first_row = next(csvreader)
    for row in csvreader:
        revenue.append(int(row[1]))
        date.append(row[0])

    for i in range(1, len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = '{:,.2f}'.format(sum(rev_change)/len(rev_change))

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = (date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", len(date))
print("Total Revenue : $", sum(revenue))
print("Avereage Revenue Change: $", (avg_rev_change))
print("Greatest Increase in Profits:",
      max_rev_change_date, "($", max_rev_change, ")")
print("Greatest Decrease in Profits:",
      (min_rev_change_date), "($", min_rev_change, ")")
