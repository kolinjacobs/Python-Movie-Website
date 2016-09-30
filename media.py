import webbrowser
class Movie():

    #movie contructer, used to create a movie object with various variable
    def __init__ (self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #opens the movie trailer in the users web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
