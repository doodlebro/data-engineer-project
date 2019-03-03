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
	
	
def parseObject(movieID, obj, objType):
	try:
		retVal = ast.literal_eval(obj) if obj is not None else None
		
		return retVal if retVal is not None else []
	except SyntaxError as e:
		print 'Error encountered parsing {0} for movie ID: {1}'.format(objType, movieID)
		return []
		

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
		try:
			movieID = int(line[5])
		except ValueError as e:
			print 'Invalid movieID for line: {0}'.format(idx)
			continue
		
		try:
			rawGenres = line[3]
			workingGenres = parseObject(movieID, rawGenres, 'genre')
			genreLines = extractGenres(movieID, workingGenres)
			genres.extend(genreLines)
		except IndexError as e:
			print 'Missing genre for movie ID: {0}'.format(movieID) 
		try:
			rawPCs = line[12]
			prodComps = parseObject(movieID, line[12], 'prod comp')
			pcLines = extractProdComps(movieID, prodComps)
			pcs.extend(pcLines)
		except IndexError as e:
			print 'Missing prod comp for movie ID: {0}'.format(movieID)
		
		# Modular extraction & append to respective output lists
		movieLine = extractMain(movieID, line)
		movies.append(movieLine)
		
		
		
		
		
	return (movies, genres, pcs)
		
	
	# Write out files
	
	
	print 'done!'