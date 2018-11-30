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
			russia.append([int(row[0]), row[5], row[6], row[7]]) 
		line_count += 1

men = []
women = []

for medal in russia:
	if medal[1] == "Men":
		men.append(medal)

	if medal[1] == "Women":
		women.append(medal)

print('Number of men in RUSSIA', len(men))
print('Number of women in RUSSIA', len(women))
print('procesed', line_count, 'rows of data')

totalMedals = len(men) + len(women)

#percentage of all medals
men_percentage = int(len(men) / totalMedals * 100)
women_percentage = int(len(women) / totalMedals * 100)



labels = "Men", "Women"
sizes = [men_percentage, women_percentage]
colors = ['yellowgreen', 'blue',]
explode = (0.01, 0.01,)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Gender of Russia in the Olympics")
plt.xlabel("Men vs Women")
plt.show()