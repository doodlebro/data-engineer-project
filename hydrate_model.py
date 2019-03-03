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
	companies = []
	for companyDict in rawPC:
		pcID = companyDict.get('id')
		pcName = companyDict.get('name')
		companies.append([pcID, movieID, pcName])
	
	return companies


def extractGenres(movieID, rawGenres):
	genres = []
	for genreDict in rawPC:
		genreID = genreDict.get('id')
		genreName = genreDict.get('name')
		genres.append([genreID, movieID, genreName])
	
	return genres


def extractMain(movieID, rawMeta):
	originalTitle = rawMeta[8]
	releaseDate = rawMeta[14]
	budget = rawMeta[2]
	revenue = rawMeta[15]
	popularity = rawMeta[10]
	
	movie = [movieID, originalTitle, releaseDate, budget, revenue, popularity]
	
	return movie
	
	
def mane():
	# Load CSV as list
	dataList = loadCSV(movieMDFilename)
	
	# Hold onto header
	header = dataList[0]
	
	# Prepare output lists
	movies = [movieHeader]
	genres = [genreHeader]
	pcs = [pcHeader]
	
	# Iterate through metadata
	workingList = dataList[1:]
	for line in workingList:
		movieID = line[5]
		
		# Lists of dicts, represented as a string
		genres = ast.literal_eval(line[3])
		prodComps = ast.literal_eval(line[12])
		
		# Modular extraction & append to respective output lists
		movieLine = extractMain(movieID, line)
		movies.append(movieLine)
		
		genreLines = extractGenres(movieID, genres)
		genres.extend(genreLines)
		
		pcLines = extractProdComps(movieID, prodComps)
		pcs.extend(pcLines)
		
	
	# Write out files
	
	
	print 'done!'