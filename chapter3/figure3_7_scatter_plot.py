from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends,minutes)

#name each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy = (friend_count, minute_count),     #set specific point with label
        xytext = (5, -5),                       #but lightely out of center
        textcoords = 'offset points')

#add title
plt.title('Daily Minutes vx. Number of Friends')

#add legend to the 'x' axis
plt.xlabel('Number of Friends')
plt.ylabel('Daily Minutes Spent on Site')

plt.show()