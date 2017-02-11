# import webbrowser to open our youtube trailer.
import webbrowser

'''
Creates a Movie class for adding movie titles, and youtube trailers to a web page.
'''

# create movie class
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

# create function to show the movie trailer
	def show_trailer(self):
		webbrowser.Open(self.trailer_youtube_url)

