# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    """Class provides a way to store movie related information.

    Attributes:
        title (str): Movie title.
        storyline (str, optional): Movie plot summary.
        poster_image_url (str, optional): URL to movie poster.
        trailer_youtube_url (str, optional): URL til trailer on YouTube website.
        year (int, optional): Release year.
        duration (int, optional): Duration in minutes.
        genre ('list', optional): Movie genres. 

    Methods:
        show_trailer (self): Opens trailer url if movie instance in browser.
    """
    
    def __init__(self, title, **kwargs):
        """Initializes instance of class Movie.

        Since there are many arguments in this function,
            **kwargs is used to ommit many lines of similar code.
            
        Args:
            title (str): Movie title.
            **kwargs: Arbitrary keyword arguments.
            
        Keyword Arguments:
            storyline (str, optional): Movie plot summary.
            poster_image_url (str, optional): URL to movie poster.
            trailer_youtube_url (str, optional): URL til trailer on YouTube website.
            year (int, optional): Release year.
            duration (int, optional): Duration in minutes.
            genre ('list', optional): Movie genres. 
        """

        self.title = title
        valid_args = [
            "storyline", "poster_image_url",
            "trailer_youtube_url", "year", "duration", "genre"
            ]
        for key in valid_args:
            self.__dict__[key] = kwargs.get(key)
       
    def show_trailer(self):
        """Opens trailer url in browser.
        """
        webbrowser.open(self.trailer_youtube_url)
