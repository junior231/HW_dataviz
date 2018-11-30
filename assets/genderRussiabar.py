import csv
import matplotlib.pyplot as plt 
import numpy as np


categories = []
russia =[]

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "RUS":
			russia.append([int(row[0]), row[5], row[6], row[7]])
		
men_rus = []
women_rus = []

for gender in russia:
		if gender[1] == "Men":
			men_rus.append(gender)

		if gender[1] == "Women":
			women_rus.append(gender)



m = len(men_rus)
f = len(women_rus)


print('Number of men in RUSSIA' , len(men_rus))
print('Number of women in RUSSIA', len(women_rus))



print('processed', line_count, 'rows of data')

x = np.arange(2)
medals = [m,f]

fig, ax = plt.subplots()
plt.bar(x, medals)
plt.xticks(x, ('RUSSIA Men', 'RUSSIA Women'))
plt.title("Number of men and women from RUSSIA in the Olympics")

plt.show()


