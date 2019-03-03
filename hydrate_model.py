import csv
import ast
import os


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
	
	
def parseObject(movieID, obj, objType):
	try:
		retVal = ast.literal_eval(obj) if obj is not None else None
		
		return retVal if retVal is not None else []
	except SyntaxError as e:
		print 'Error encountered parsing {0} for movie ID: {1}'.format(objType, movieID)
		return []
	
		
def mineMovieID(rawLine, lineIDX, expIDX):
	try:
		movieID = int(rawLine[expIDX])
	except ValueError as e:
		print 'Invalid movieID for line: {0}'.format(lineIDX)
		movieID = -1
	
	return movieID
	

def mineListObj(rawLine, objType, expIDX, movieID):
	try:
		rawObj = rawLine[expIDX]
		workingObj = parseObject(movieID, rawObj, objType)
	except IndexError as e:
		print 'Missing {0} for movie ID: {1}'.format(objType, movieID)
		workingObj = None
		
	return workingObj
		

def extractProdComps(movieID, rawPC):
	if type(rawPC) is not list:
		print 'Error encountered extracting prod comps for movie ID: {0}'.format(movieID)
		return []

	companies = []
	for companyDict in rawPC:
		pcID = companyDict.get('id')
		pcName = companyDict.get('name')
		companies.append([pcID, movieID, pcName])
	
	return companies


def extractGenres(movieID, rawGenres):
	if type(rawGenres) is not list:
		print 'Error encountered extracting genres for movie ID: {0}'.format(movieID)
		return []

	genres = []
	for genreDict in rawGenres:
		genreID = genreDict.get('id')
		genreName = genreDict.get('name')
		genres.append([genreID, movieID, genreName])
	
	return genres


def extractMain(movieID, rawMeta):
	originalTitle = rawMeta[8] if len(rawMeta) > 8 else None
	releaseDate = rawMeta[14] if len(rawMeta) > 14 else None
	budget = rawMeta[2] if len(rawMeta) > 2 else None
	revenue = rawMeta[15] if len(rawMeta) > 15 else None
	popularity = rawMeta[10] if len(rawMeta) > 10 else None
	
	movie = [movieID, originalTitle, releaseDate, budget, revenue, popularity]
	
	return movie
	
	
def writeOut(finalList, outFile):
	with open(outFile, 'wb') as f:
		fileWriter = csv.writer(f)
		fileWriter.writerows(finalList)
	
	
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
	for idx, line in enumerate(workingList):
		movieID = mineMovieID(line, idx, 5)
		if movieID == -1: # If movie ID is missing, move to next line.
			continue
		
		# Mine & Extract Genres
		workingGenres = mineListObj(line, 'genre', 3, movieID)
		genreLines = extractGenres(movieID, workingGenres) if workingGenres is not None else []
		genres.extend(genreLines)

		workingPCs = mineListObj(line, 'prod comp', 12, movieID)
		pcLines = extractProdComps(movieID, workingPCs) if workingPCs is not None else []
		pcs.extend(pcLines)
		
		# Modular extraction & append to respective output lists
		movieLine = extractMain(movieID, line)
		movies.append(movieLine)
		
	# Write out files
	writeOut(movies, 'movies.csv')
	writeOut(genres, 'genres.csv')
	writeOut(pcs, 'prod_comps.csv')
	
	print 'done!'