class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    

    def Release(self):
        print(self.title, self.director, self.year)

NewRelease = Movie("Sonic The Hedgehog 3", "Jeff Fowler", 2024)
NewRelease.Release()

print(NewRelease.title)

print("My favorite filem is", NewRelease.title, "directed by", NewRelease.director, "released in", NewRelease.year)

print(NewRelease)