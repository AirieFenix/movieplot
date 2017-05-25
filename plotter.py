#plotter

import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

genres = [{'genre_name': 'Thriller', 'number': 41}, {'genre_name': 'Science Fiction', 'number': 60}, {'genre_name': 'Drama', 'number': 63}, {'genre_name': 'Documentary', 'number': 26}, {'genre_name': 'Comedy', 'number': 37}, {'genre_name': 'Fantasy', 'number': 23}, {'genre_name': 'Action', 'number': 55}, {'genre_name': 'Mystery', 'number': 22}, {'genre_name': 'Music', 'number': 6}, {'genre_name': 'Horror', 'number': 11}, {'genre_name': 'Romance', 'number': 12}, {'genre_name': 'Crime', 'number': 22}, {'genre_name': 'War', 'number': 5}, {'genre_name': 'Adventure', 'number': 53}, {'genre_name': 'History', 'number': 6}, {'genre_name': 'Animation', 'number': 10}, {'genre_name': 'Family', 'number': 9}, {'genre_name': 'Western', 'number': 1}]

times = {'avg_runtime': 113.04022988505747, 'total_runtime': 19669, 'min_runtime': 38, 'min_runtime_name': 'Space Junk 3D', 'max_runtime': 201, 'max_runtime_name': 'The Lord of the Rings: The Return of the King'}

scores = {'max_score': 8.1, 'max_score_name': 'Modern Times', 'min_score': 4.3, 'min_score_name': 'Bio-Dome'}

def draw_genres():

	sum = 0
	labels = []
	sizes = []
	newlist = sorted(genres, key=itemgetter('number'),reverse=True)

	for g in range(0,9):
		labels.append(newlist[g]['genre_name'])
		sizes.append(newlist[g]['number'])

	#for a in range(7,len(newlist)):
	#	sum += newlist[a]['number']

	#labels.append('Others')
	#sizes.append(sum)

	fig, ax = plt.subplots()
	ax.pie(sizes,labels=labels,autopct='%1.1f%%')
	ax.axis('equal')
	fig.suptitle('Movies by genre')
	plt.show()

if __name__ == '__main__':
	draw_genres()