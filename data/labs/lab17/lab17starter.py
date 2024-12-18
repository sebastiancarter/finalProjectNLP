import matplotlib.pyplot as plt
import csv

#Input: A dict d, and a list specifying the desired order of the keys
#Output: A list with the values ordered in the same way as the passed-in keys
def dictToOrderedList(d, orderedKeys):
    ret = []
    for key in orderedKeys:
        ret.append(d[key])
    return ret


states = ["Utah", "Washington", "Hawaii", "New York"]
#Dicts, mapping from state to percentage
incidence2000 = {}
mortality2000 = {}
incidence2011 = {}
mortality2011 = {}


f = open("cancer.csv", "r") # NO FILESTREAM CLOSE???? BAD STYLE -100000 points
reader = csv.DictReader(f)
for row in reader:
    if row['state'] not in states:
        continue #Skip states that don't match the ones we're looking for
    
    if int(row['year']) == 2000:
        if row['event type'] == 'Incidence':
            incidence2000[row["state"]] = 100*(int(row["count"]) / int(row["study population"]))
        else:
            mortality2000[row["state"]] = 100*(int(row["count"]) / int(row["study population"]))

    if int(row['year']) == 2011:
        if row['event type'] == 'Incidence':
            incidence2011[row["state"]] = 100*(int(row["count"]) / int(row["study population"]))
        else:
            mortality2011[row["state"]] = 100*(int(row["count"]) / int(row["study population"]))


#Convert the dicts to ordered lists, for easier use with matplotlib
incidence2000List = dictToOrderedList(incidence2000, states)
mortality2000List = dictToOrderedList(mortality2000, states)
incidence2011List = dictToOrderedList(incidence2011, states)
mortality2011List = dictToOrderedList(mortality2011, states)



firstWidthList = list()
secondWidthList = list()
for x in range(len(states)):
    firstWidthList.append(x-0.2)
    secondWidthList.append(x+0.2)


(fig, axes) = plt.subplots(1, 2)
axes[0].set_title("mortality and incidences in 2000")
axes[0].bar(firstWidthList, incidence2000List, width=0.4, label="incidences")
axes[0].bar(secondWidthList, mortality2000List, width=0.4, label="mortality")
axes[0].set_xticks(range(len(states)), states, rotation=50, ha='right')
axes[0].set_xlabel("states")
axes[0].set_ylabel("percentage of cases per population")
axes[0].legend()

axes[1].set_title("mortality and incidences in 2011")
axes[1].bar(firstWidthList, incidence2011List, width=0.4, label="incidences")
axes[1].bar(secondWidthList, mortality2011List, width=0.4, label="mortality")
axes[1].set_xticks(range(len(states)), states, rotation=50, ha='right')
axes[1].set_xlabel("states")
axes[1].set_ylabel("percentage of cases per population")
axes[1].legend()

fig.subplots_adjust(wspace=1.0, hspace=2.0)
plt.tight_layout()
plt.show()
