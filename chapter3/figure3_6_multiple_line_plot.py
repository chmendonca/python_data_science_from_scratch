from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#it is allowed to make many calls to plt.plot to show multiple series in the same graph
#supported values for line types are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(xs, variance, 'g-', label='variance')        #solid green line 
plt.plot(xs, bias_squared, 'y-.', label='bias^2')     #dashdot yellow line
plt.plot(xs, total_error, 'b:', label='total error')  #dotted blue line

#since it were set some legends, it is possible to create a grouped legend (loc=9 means 'top center')
plt.legend(loc=9)

#add title
plt.title('The Bias-Variance Tradeoff')

#add legend to the 'x' axis
plt.xlabel('model complexity')
plt.xticks([])

plt.show()