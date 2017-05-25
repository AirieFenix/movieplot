import json
import sys

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
		if movie['budget'] < min and movie['budget'] != 0:
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

if __name__ == '__main__':
	
	movie_data = read_data(sys.argv[1])
	#print(movie_data)
	print(count_genres(movie_data))
	print(calc_budget(movie_data))
	print(calc_stats(movie_data))
	print(calc_times(movie_data))