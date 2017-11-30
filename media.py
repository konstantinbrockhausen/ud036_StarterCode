#Creates the class Movie with the methods "title", "poster_image_url", and "trailer_youtube_url"
class Movie():
    def __init__(self, movie_title, box_art_url, youtube_url):
        self.title = movie_title
        self.poster_image_url = box_art_url
        self.trailer_youtube_url = youtube_url
