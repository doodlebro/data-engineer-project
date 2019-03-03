import csv
import ast


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

def extractProdComps(movieID, rawPC):


def extractGenres(movieID, rawGenres):


def extractMain(movieID, rawMeta):


def mane():
	# Load CSV as list
	dataList = loadCSV(movieMDFilename)
	
	# Hold onto header
	header = dataList[0]
	
	# Iterate through metadata
	workingList = dataList[1:]
	for line in workingList:
		movieID = line[5]
		
		# Lists of dicts, represented as a string
		genres = ast.literal_eval(line[3])
		prodComps = ast.literal_eval(line[12])
		
	
	# Write out files
	
	
	print 'done!'