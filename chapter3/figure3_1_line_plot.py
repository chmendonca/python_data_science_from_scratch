from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#to create a graph of lines. 'years' on 'x' axis. 'gdp' on 'y' axis.
#plt.plot(years,gdp, color='yellow', marker='o', linestyle='dotted')
plt.plot(years,gdp, color='red', marker='*', linestyle='dashed')
#plt.plot(years,gdp, color='orange', marker='^', linestyle='solid')

#add title
plt.title('Nominal GDP')

#add legend to the 'y' axis
plt.ylabel('Billions of $')
plt.show()