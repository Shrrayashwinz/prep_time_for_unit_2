class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

        def Show(self):
            print("MOVIE NAME:", self.title, "DIRECTOR:", self.director, "YEAR:", self.year)

NewMovie = Movie("Sonic The Hedgehog 3", "Jeff Fowler", 2024)
NewMovie.Show()

print(NewMovie)
print(NewMovie.title, NewMovie.director, NewMovie.year)