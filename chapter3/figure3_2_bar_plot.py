from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

#plot bars with x coordinates at left [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title('My favorite movies')
plt.ylabel('Number of Academy Awards')

#insert the name of the movies into the bars, at their center
plt.xticks(range(len(movies)), movies)

plt.show()