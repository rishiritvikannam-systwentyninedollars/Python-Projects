class Playlist:

    # Step 1 - Parameterized Constructor: runs the moment te playlist is created
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print("Playlist", self.name, self.genre, "is ready!!")

    # Step 2 - Add a song to the playlist
    def add_song(self, song):
        self.songs.append(song)
        print(song, "added to", self.name)

    # Step 3 - Remove a song from the playlist
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(song, "removed")
        else:
            print(song, "not found in the playlist.")
    
    # Step 4 - Display all songs
    def display(self):
        print(self.name, self.genre)
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(i, song)
        else:
            print("No songs yet. Add some more!")

        # Step 5 - Destructor: rins automatically when the playlist is deleted
        def __del__(self):
            print("playlist", self.name, "has been deleted, goodbye!")

# Object Creation (constructor fires here)
my_playlist = Playlist("Rock", "Pop")