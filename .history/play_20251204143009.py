class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

        def Show(self):
            print("MOVIE NAME:", self.title, "DIRECTOR:", self.director, "YEAR:", self.year)