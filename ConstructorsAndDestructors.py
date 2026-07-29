class playlist:
    def __init__(self, name, genre): # It is the special _init_ method that runs the moment you create an object.
        self.name = name
        self.genre = genre
        self.songs = []

    def __del__(self): # A method that automatically runs when you delete an object.
            print("playlist", self.name, "has been deleted, Goodbye!")

my_mix = playlist("Rock", "Pop")


