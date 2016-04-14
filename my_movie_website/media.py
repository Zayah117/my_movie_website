import webbrowser


class Movie():
        '''This class creates instances of movies. It holds
        information such as the movies title, storyline, poster
        image, trailer, and rating.'''

        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

        def __init__(self, movie_title, movie_storyline,
                     poster_image, youtube_trailer, rating):
                '''My __init__ function takes all kinds of information about
                the movie as inputs and uses them to set the self variables.'''

                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = youtube_trailer
                self.rating = rating

        def show_trailer(self):
                '''I can use this function to open a movies trailer
                in a webbrowser'''
                webbrowser.open(self.trailer_youtube_url)
