# import modules
import fresh_tomatoes
import media

# create movie instances
edwardscissorhands = media.Movie("Edward Scissorhands",
								 "Story about a scientists creation who has scissors for hands",
								 "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Edwardscissorhandsposter.JPG/220px-Edwardscissorhandsposter.JPG",
								 "https://www.youtube.com/watch?v=M94yyfWy-KI")

tnbc = media.Movie("The Nightmare Before Christmas",
				   "Christmas and Halloween meet, and things go terribly wrong...",
				   "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/The_nightmare_before_christmas_poster.jpg/220px-The_nightmare_before_christmas_poster.jpg",
				   "https://www.youtube.com/watch?v=wr6N_hZyBCk")

edwood = media.Movie("Ed Wood",
					 "Based on the true story or the worst director in Hollywood history, Edward Wood.",
					 "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Ed_Wood_film_poster.jpg/220px-Ed_Wood_film_poster.jpg",
					 "https://www.youtube.com/watch?v=CawVaHxWvnA")

sleepyhollow = media.Movie("Sleepy Hollow",
						   "Based on the popular New England tale, Washington Irving's, Sleepy Hollow.",
						   "https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Sleepy_hollow_ver2.jpg/220px-Sleepy_hollow_ver2.jpg",
						   "https://www.youtube.com/watch?v=R6O4Himch7g")

batman = media.Movie("Batman",
					 "Based on the comic book series, Tim Burton's Batman.",
					 "https://upload.wikimedia.org/wikipedia/en/5/5a/Batman_(1989)_theatrical_poster.jpg",
					 "https://www.youtube.com/watch?v=VRqa47-jv0M")

frankenweenie = media.Movie("Frankenweenie",
						    "Boy brings his dog back to life after a terrible accident.",
						    "https://upload.wikimedia.org/wikipedia/en/f/f7/Frankenweenie_(1984_film)_poster.jpg",
						    "https://www.youtube.com/watch?v=MqJ7etOk618")

# initialize a list of movie instaces to be passed to fresh_tomatoes.open_movies_page()
movies = [edwood,sleepyhollow,batman,frankenweenie,edwardscissorhands,tnbc]

# pass movies array 
fresh_tomatoes.open_movies_page(movies)