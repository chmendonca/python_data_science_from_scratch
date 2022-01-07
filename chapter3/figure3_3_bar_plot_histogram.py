from matplotlib import pyplot as plt

from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 40, 85, 82, 100, 67, 73, 77, 0]

#group the grades by 10 per 10 and set 100 within the 90's
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], #Move the bars 5 to the right
    histogram.values(),                    #Set the right height
    10,                                    #Set the width of 10 to each bar (it accepts float number)
    edgecolor = (0,0,0))                   #Set dark columns edges

plt.axis([-5,105,0,5])                     #'x' axis from -5 to 105 and 'y' axis from 0 to 5

plt.xticks([10 * i for i in range(11)])    #'x' ticks from 0 to  100 by 10

plt.title('Distribution of Exam 1 Grades')
plt.ylabel('Number of Students')
plt.xlabel('Decile')

plt.show()
