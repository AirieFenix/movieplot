import json
import sys
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import datetime as dt

def read_data(filename):
	with open(filename) as fout:
		d = json.load(fout)

	return d

def count_genres(movies):

	genres=list()
	names=list()
	list_genres=list()

	for movie in movies:
		for gen in movie['genres']:
			genres.append(gen['name'])

	for x in genres:
		if x not in names:
			names.append(x)

	for i in range(len(names)):
		aux=dict()
		aux['genre_name'] = names[i]
		aux['number'] = genres.count(aux['genre_name'])
		list_genres.append(aux.copy())

	return list_genres

def calc_times(movies):

	times = dict()
	sum = 0
	max = 0
	min = 500
	max_runtime_movie = ''
	min_runtime_movie = ''

	for movie in movies:
		sum += movie['runtime']
		if movie['runtime'] > max:
			max = movie['runtime']
			max_runtime_movie = movie['title']
		if movie['runtime'] < min:
			min = movie['runtime']
			min_runtime_movie = movie['title']

	times['avg_runtime'] = sum/len(movies)
	times['total_runtime'] = sum
	times['min_runtime'] = min
	times['min_runtime_name']=min_runtime_movie
	times['max_runtime'] = max
	times['max_runtime_name'] = max_runtime_movie

	return times

def calc_budget(movies):

	min = 999999999
	max = 0
	min_budget_name = ''
	max_budget_name = ''
	max_name = ''
	min_name = ''


	for movie in movies:
		if movie['budget'] < min and movie['budget'] > 1000:
			min = movie['budget']
			min_name = movie['title']
		if movie['budget'] > max:
			max = movie['budget']
			max_name = movie['title']

	budget_dict = {'min_budget':min,'min_budget_movie':min_name,'max_budget':max,'max_budget_movie':max_name}

	return budget_dict

def calc_stats(movies):

	scores = dict()
	max_score = 0.0
	max_score_name = ''
	min_score = 10.0
	min_score_name = ''

	for movie in movies:
		if movie['votes'] > max_score:
			max_score = movie['votes']
			max_score_name = movie['title']
		if movie['votes'] < min_score and movie['votes'] > 0.0:
			min_score = movie['votes']
			min_score_name = movie['title']

	scores['max_score'] = max_score
	scores['max_score_name'] = max_score_name
	scores['min_score'] = min_score
	scores['min_score_name'] = min_score_name
	
	return scores

def calc_antique(movies):

	today = dt.date.today()
	release_delta = list()

	for movie in movies:
		x=0
		aux = movie['date'].split('-')[0]
		release_delta.append(aux)

	release_delta.sort()
	return release_delta

def draw_antique(release_delta):

	k = [int(n) for n in release_delta]
	bins = [i for i in range(1930,2030,3)]
	print(bins)

	plt.hist(k,bins,histtype='bar',rwidth=0.99)

	#plt.bar(k,k2,label='Bars1')
	plt.show()

def draw_ratings_hist(movies):

	k = list()

	for movie in movies:
		if movie['votes'] != 0.0:
			k.append(movie['votes'])
	bins = [i for i in range(11)]

	plt.hist(k,bins,histtype='bar',rwidth=0.99)

	#plt.bar(k,k2,label='Bars1')
	plt.show()

def draw_times(movies):

	k = [movie['runtime'] for movie in movies]
	bins = [i for i in range(30,210,5)]

	plt.hist(k,bins,histtype='bar',rwidth=1)
	plt.show()

def draw_genres(genres,limit=0):

	sum = 0
	labels = []
	sizes = []
	newlist = sorted(genres, key=itemgetter('number'),reverse=True)

	for g in range(limit):
		print(str(g))
		labels.append(newlist[g]['genre_name'])
		sizes.append(newlist[g]['number'])

	if limit == 0:	
		for a in range(7,len(newlist)):
			sum += newlist[a]['number']
		labels.append('Others')
		sizes.append(sum)

	else:
		for a in range(limit,len(newlist)):
			sum += newlist[a]['number']
		labels.append('Others')
		sizes.append(sum)

	fig, ax = plt.subplots()
	ax.pie(sizes,labels=labels,autopct='%1.1f%%')
	ax.axis('equal')
	fig.suptitle('Movies by genre')
	plt.show()

def draw_ratings(movies):

	ordered_list = sorted(movies, key=itemgetter('votes'),reverse=True)
	ratings = [movie['votes'] for movie in movies]
	labels = [movie['title'] for movie in movies]
	xx = [x for x in range(1,len(movies)+1)]

	fig, ax = plt.subplots()
	ax.bar(xx,ratings)
	ax.set_xticks(xx)
	ax.set_xticklabels([movie['title'] for movie in movies])
	plt.show()

if __name__ == '__main__':

	movie_data = read_data(sys.argv[1]) #data file

	date = movie_data[0]['date']

	print(type(date))
	release_delta = calc_antique(movie_data)

	#draw_ratings(movie_data)
	#draw_times(movie_data)
	#draw_ratings_hist(movie_data)

	#print(release_delta)
	draw_antique(release_delta)

	#for x in release_delta:
	#	print(x)

	#genres = count_genres(movie_data)
	#print(movie_data)
	#print(count_genres(movie_data))
	#print(calc_budget(movie_data))
	#print(calc_stats(movie_data))
	#print(calc_times(movie_data))
	#draw_genres(genres,6)