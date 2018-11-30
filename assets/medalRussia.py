import csv
import matplotlib.pyplot as plt

categories = []
russia = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "RUS":
			russia.append([int(row[0]), row[5], row[6], row[7]])    #Year Gender Event Medal
		line_count += 1

gold = []
silver = []
bronze = []

for medal in russia:
	if medal[3] == "Gold":
		gold.append(medal)

	if medal[3] == "Silver":
		silver.append(medal)

	if medal[3] == "Bronze":
		bronze.append(medal)


print('Number of gold medal in RUSSIA', len(gold))
print('Number of silver medal in RUSSIA', len(silver))
print('Munber of bronze medal in RUSSIA', len(bronze))
print('procesed', line_count, 'rows of data')

totalMedals = len(gold) + len(silver) + len(bronze)

#percentage of all medals
gold_percentage = int(len(gold) / totalMedals * 100)
silver_percentage = int(len(silver) / totalMedals * 100)
bronze_percentage = int(len(bronze) / totalMedals * 100)



labels = "gold", "silver","bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ['red', 'yellow', 'black']
explode = (0.05, 0.05, 0.05)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Types of RUSSIA Medals in the Olympics")
plt.xlabel("Gold vs Silver vs Bronze")
plt.show()