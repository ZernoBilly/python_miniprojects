from datetime import date
import csv

dt = date.today()
filename = "expence_tracker/expenses.csv"
expenses = []
stopped = False

with open(filename, "a", newline="") as file:
    csvwriter = csv.writer(file)

    while not stopped:
        expense = int(input("What is the todays expences (type 0 to stop)"))

        if expense == 0:
            stopped = True
        else:
            csvwriter.writerow([str(dt), str(expense)])
            expenses.append(expense)

file.close()
print(expenses)
