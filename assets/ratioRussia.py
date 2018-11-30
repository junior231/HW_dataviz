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
		elif row[4] == "USA":
			russia.append([int(row[0]), row[5], row[6], row[7]])
		
silver_2014 = []
silver_2002 = []

for silver in russia:
		if silver[0] == 2014 and silver[3] == "Silver":
			silver_2014.append(silver)

		if silver[0] == 2002 and silver[3] == "Silver":
			silver_2002.append(silver)


m = len(silver_2014)
f = len(silver_2002)


print('Number of Silver in 2014' , len(silver_2014))
print('Number of Silver in 2002', len(silver_2002))



print('processed', line_count, 'rows of data')

x = np.arange(2)
medals = [m,f]

fig, ax = plt.subplots()
plt.bar(x, medals)
plt.xticks(x, ('SILVER 2014', 'SILVER 2002'))
plt.title("Number of Silver from RUSSIA in the 2014 and 2002 Olympics")

plt.show()


