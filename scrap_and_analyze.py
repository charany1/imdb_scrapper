import requests
from bs4 import BeautifulSoup


def getPages(url="https://www.imdb.com/search/title?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,&page=1"):
	resposne = requests.get(url)
	return resposne.text

def parseHtml(htmlString):
	soup = BeautifulSoup(htmlString,'html.parser')

	movie_soups = soup.find_all(class_='lister-item')

	movie_info_list = list()

	for soup in movie_soups:
		movie_info_list.append(prepareDict(getTitle(soup),getYear(soup),getDuration(soup),getGenreList(soup),getRating(soup),getDirector(soup),getStars(soup)))


	printMovieRating(movie_info_list)


	#for movie in movie_info_list:
	#	print(movies)
	#crew_soup = soup.find_all(class_='lister-item')[0].find_all('div', recursive=False)[-1].find_all('p')[-2].find_all('a')
	#for index in range(1,len(crew_soup)):
	#	print (crew_soup[index].get_text())


def printMovieRating(movie_info_list):
	for movie in movie_info_list:
		print (movie['title']+"  "+"*"*int(movie["rating"][0]))


def printMovieByDecade(movie_info_list):
	decade_dict = dict()
	for movie in movie_info_list:
		



def prepareDict(title,year,duration,genres,rating,director,stars):
	return {"title":title,"year":year,"duration":duration,"genres":genres,"rating":rating,"director":director,"stars":stars}


def getTitle(lister_item):
	return lister_item.find(class_='lister-item-content').a.get_text()

def getYear(lister_item):
	return lister_item.find(class_='lister-item-year').get_text()[1:5]

def getDuration(lister_item):
	return lister_item.find(class_='runtime').get_text()[0:4]

def getGenreList(lister_item):
	return lister_item.find(class_='genre').get_text().split(", ")

def getRating(lister_item):
	return lister_item.find(class_='ratings-bar').strong.get_text()

def getDirector(lister_item):
	return lister_item.find_all('div', recursive=False)[-1].find_all('p')[-2].find_all('a')[0].get_text()

def getStars(lister_item):
	crew_soup = getCrewSoup(lister_item)
	stars = list()
	for index in range(1,len(crew_soup)):
		stars.append(crew_soup[index].get_text())

	return stars


def getCrewSoup(lister_item):
	return lister_item.find_all('div', recursive=False)[-1].find_all('p')[-2].find_all('a')




	return None



def main():
	NPAGES = 1
	parseHtml(getPages())

	
	
	

if __name__ == '__main__':
	main()
