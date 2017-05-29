#pymovie plotter

import json
import sys
import requests
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

filename = 'movies.txt'
API_KEY = '2a60ad26c7e7ba01e87ffd2eed786a6f'
discover_url = 'https://api.themoviedb.org/3/movie/'
search_url = 'https://api.themoviedb.org/3/search/movie'

def search_movie(s_query):

	extra_params = {'api_key':API_KEY,'query':s_query}	

	r = requests.get(search_url,extra_params)
	data = r.json()

	return data

def get_movie_data(id):

	extra_params = {'api_key':API_KEY}

	r = requests.get(discover_url+str(id),extra_params)
	movie_data = r.json()

	return movie_data

def get_movie_id(data,word):

	for result in data['results']:
		if result['original_title'].lower() == word.lower() or result['title'].lower() == word.lower():
			return result['id']

	return None

def complete_list(movies):

	errors = list()

	for movie in movies:
		data = search_movie(movie['title'])
		
		id = get_movie_id(data,movie['title'])
		#print(id)
		try:
			x = get_movie_data(id)
			print(x['original_title'])
			movie['genres'] = x['genres']
			movie['popularity'] = x['popularity']
			movie['runtime'] = x['runtime']
			movie['date'] = x['release_date']
			movie['votes'] = x['vote_average']
			movie['budget'] = x['budget']
			print(movie)
		except KeyError:
			print('ERROR',movie['title'])
			errors.append(movie['title'])

	print(errors)	
	print('Errores:',str(len(errors)),'out of',str(len(movies)))
	return movies

def get_list():

	movie=dict()
	movies=list()
	file_obj = open(filename,'r')

	aux_list = file_obj.read().split(', ')
	file_obj.close()

	aux_list = aux_list[:-1]

	for x in aux_list:
		movie['title'] = x.split(' (')[0]
		movie['genres'] = list()
		movie['popularity'] = 0.0
		movie['votes'] = 0.0
		movie['runtime'] = 0
		movie['date'] = ''
		movie['budget'] = 0
		movies.append(movie.copy())

	return movies

def dump_json(movies):
	
	with open('movie_data','w') as fout:
		json.dump(movies,fout)

if __name__ == '__main__':

	movies = get_list()
	movies = complete_list(movies)
	genres = count_genres(movies)

	dump_json(movies)