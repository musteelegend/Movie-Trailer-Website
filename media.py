import webbrowser

# The parent class from which Movies inherits
class Videos():

    # Constructor for videos class
     def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
# Child class inheriting from parent
class Movie(Videos):
    """The class provides a way to provide related information.
    This information will be based on its blueprint."""

    # Class variable for rating of the movies
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor for movie class
    def __init__(self, title, duration, movie_storyline, poster_image,
                 trailer_youtube):
        Videos.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Instance method for movie class
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
