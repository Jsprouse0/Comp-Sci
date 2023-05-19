'''
Author: Jacob Sprouse
Assignment title: Program 12
Assignment Description: Movie Times
Due Date: 05/12/2023
Date Created: 05/12/2023
Date Last Modified: 05/12/2023
'''

from collections import namedtuple

# namedtuple keeps track of movies with same name
Movies = namedtuple('Movie', 'times, title, rating')
movie_data = dict()

# Input
file_name = input().strip()
file = open(file_name)

# Process/reads each line in file to strip and split each line
for line in file:
    time, title, rating = line.strip().split(',')
    if title not in movie_data:
        movie_data[title] = Movies([], title, rating)
    movie_data[title].times.append(time)
file.close()

# Output/prints the movie title up to 44 characters, also prints times/rating in sections
for movie in movie_data:
    print(f'{movie[0:44]:44} | {movie_data[movie].rating:>5} | ', end='')
    for show_time in movie_data[movie].times:
        print(f' {show_time}', end='')
    print()
