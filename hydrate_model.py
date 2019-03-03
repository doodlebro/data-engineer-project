import csv


# Pre-vars
movieMDFilename = 'movies_metadata.csv'

movieHeader = ['movie_id', 'original_title', 'release_date', 'budget', 'revenue', 'popularity']
genreHeader = ['genre_id', 'movie_id', 'name']
pcHeader = ['pc_id', 'movie_id', 'name']

def loadCSV(filename):
	file = open(filename, 'rb')
	reader = csv.reader(file)
	csvList = list(reader)

	return csvList


def mane():
	# Load CSV as list
	
	
	# Hold onto header
	
	
	# Iterate through metadata
	
	
	print 'done!'