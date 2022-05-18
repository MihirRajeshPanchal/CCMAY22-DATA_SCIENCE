from imdb import Cinemagoer
import imdb
from matplotlib.pyplot import title
from TTS import *
from STT import *


moviesDB = imdb.IMDb()
ia = Cinemagoer()

def movieSearch():
    titlelist=[]
    ratinglist=[]
    yearlist=[]
    voteslist=[]
    tts("Enter Number of Movies")
    n=int(input("Enter Number of Movies : "))
    # n=stt() #for speech search
    for i in range(n):
        tts("Movie Search")
        movies = moviesDB.search_movie(input())
        # movies = moviesDB.search_movie(stt()) #==for speech search
        id = movies[0].getID()
        movie = ia.get_movie(id)
        titlelist.append(movie['title'])
        ratinglist.append(movie['rating'])
        yearlist.append(movie['year'])
        voteslist.append(movie['votes'])
    # print(titlelist)
    # print(ratinglist)
    # print(yearlist)
    # print(voteslist)
    return titlelist,ratinglist,yearlist,voteslist