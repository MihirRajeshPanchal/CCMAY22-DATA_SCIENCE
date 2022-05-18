# importing the required module
import matplotlib.pyplot as plt
from Movie_Analysis import *


title,rating,year,votes=movieSearch()
# title=['Lagaan: Once Upon a Time in India', 'Golmaal Again', 'Dhamaal']
# rating=[8.1, 4.9, 7.4]
# year=[2001, 2017, 2007]
print("Movie in Plot Graph")
print(title)
print(rating)
print(year)
print(votes)

# Title-Rating Graph
plt.bar(title, rating, color ='blue',width = 0.4)
plt.xlabel('Movie Title')
plt.ylabel('Movie Rating')
plt.title('Title-Rating Graph')
plt.show()


# Title-Year Graph
plt.plot(title, year)
plt.xlabel('Movie Title')
plt.ylabel('Movie Rating')
plt.title('Title-Year Graph')
plt.show()

# Title-Votes Graph
plt.bar(title, votes, color ='blue',width = 0.4)
plt.xlabel('Movie Title')
plt.ylabel('Movie Rating')
plt.title('Title-Votes Graph')
plt.show()
