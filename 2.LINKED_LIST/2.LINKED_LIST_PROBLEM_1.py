"""
In this example we will learn how to build a Music Player
using Linked Lists.
You will be able to solve Problem #2 with this example.

The operators we will be handling are the following:
Add Head song - insert(Node)

"""
# Playlist Class will be your LinkedList
class PlayList():
    # Class Song will hold the Nodes or songs in Playlist:
    class Song():
        
        def __init__(self, data):
            
            self.song_name = data
            
            # Pointers directed to next or previous song
            # are currently empty because we have no song in
            # playlist, yet.
            self.next_song = None
            self.prev_song = None
        
        # Method will allow us return Song value as string:
        def __str__(self):
            return self.song_name

    def __init__(self):
        # Initialize empty Playlist:
        # Create a spot for first and last song
        # in playlist.
        # Set to None because a new playlist is empty:
        
        # Head:
        self.first_song = None
        
        # Tail:
        self.last_song = None
    
    def add_first_song(self, song_name):
        
        # Add first song to beginning of Playlist
        new_song = PlayList.Song(song_name)
        
        # If playlist empty, head and tail point to new_song:
        if self.first_song is None:
            self.first_song = new_song
            self.last_song = new_song
        else:
            
            # Here you will connect new song to previous first_song
            # also known as the head of the playlist:
            new_song.next_song = self.first_song
            
            # Connect previous head to the new song:
            self.first_song.prev_song = new_song
            
            # Here, first song points to new_song:
            self.first_song = new_song 
    #This method will iterate through input and yield all to user 
    def __iter__(self):
        
        song = self.first_song
        
        while song is not None:
            
            yield song.song_name
            song = song.next_song
    
    # The next method returns user input in String Value:
    def __str__(self):
        return ", ".join(self)
        
print("\n==============\n")
print("\n MUSIC PLAYER QUEUE: \n")
music_player = PlayList()
music_player.add_first_song("Hey Jude - The Beatles")
music_player.add_first_song("Teen Spirit - Nirvana")
music_player.add_first_song("Bohemian Rhapsody - Queen ")
music_player.add_first_song("Lullaby - Atlas Bound")
music_player.add_first_song("Space Song - Beach House")
print(music_player)
print("\n==============\n")
"""
OUTPUT PROBLEM #1:


==============


MUSIC PLAYER QUEUE:

Space Song - Beach House, Lullaby - Atlas Bound, Bohemian Rhapsody - Queen , Teen Spirit - Nirvana, Hey Jude - The Beatles

==============

OBSERVE:


Observe that the output of this playlist is backwards. It's what we need it to be,
however, we want the first song on the list to be "Hey Jude - The Beatles" and the last song
to be Space Song - Beach House

Right now, each instance of adding first_song replaces the first_song, and pushes to the end
of the list the original first song. 

Continue to problem #2 to solve the problem.

"""