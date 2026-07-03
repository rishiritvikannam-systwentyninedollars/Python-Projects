class playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

pop_mix = playlist("Billie Jean", "Pop")