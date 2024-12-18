import matplotlib.pyplot as plt
import csv


aveIncomes = list()
years = list()


with open("us-income.csv") as inFile:
    reader = csv.DictReader(inFile)
    for row in reader:
        aveString = row["mean_income"]
        aveString = aveString.replace(",", "")
        yearString = row["year"]
        aveIncomes.append(int(aveString))
        years.append(int(yearString))

plt.plot(years, aveIncomes)
plt.xlabel("year")
plt.ylabel("average income")
plt.title("ave incomes per year in the US")
plt.savefig("USincomes.png")




