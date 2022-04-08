"""
If you did not read the end of PROBLEM #1, here is the overview of what is expected 
to solve  PROBLEM #2:

Observe that the output of this playlist is backwards. It's what we need it to be,
however, we want the first song on the list to be "Hey Jude - The Beatles" and the last song
to be Space Song - Beach House

Right now, each instance of adding first_song replaces the first_song, and pushes to the end
of the list the original first song. 

Add Head song - insert front(Node), which is an O(1) for our Linked List Example.
Add Last song - insert last(Node), which is an O(1) for our Linked List Example.

You will need to solve add_last_song() method to have the playlist music the order in which
we actually want the music to display:

Current OUTPUT:

==============


 MUSIC PLAYER QUEUE:

Hey Jude - The Beatles

==============

EXPECTED OUTPUT PROBLEM #2:

==============


 MUSIC PLAYER QUEUE: 

Hey Jude - The Beatles, Teen Spirit - Nirvana, Bohemian Rhapsody - Queen , Lullaby - Atlas Bound, Space Song - Beach House

==============

You should be able to solve this using the hints provided and Problem #1. Use the solution to comapre and contrast your solution.

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
    
    def add_last_song (self, song_name): #Method to be solved is here:
        # Same to adding head, create new_song:
        new_song = PlayList.Song(song_name)
        
        
        if self.last_song is None:
            # INSERT CODE BELOW: Self tail for last song:
            
            
            # INSERT CODE BELOW: Self head for last song:
            pass#remove this line before running with solution    
            
        else:
            # INSERT CODE BELOW: Point new song PREVIOUS  to first_song(head):
            
            
            # INSERT CODE BELOW: Point new song NEXT to new_song:
            
            
            #INSERT CODE BELOW: First song now points to new_song:
            
            pass#remove this line before running with solution         
    
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
music_player.add_last_song("Teen Spirit - Nirvana")
music_player.add_last_song("Bohemian Rhapsody - Queen ")
music_player.add_last_song("Lullaby - Atlas Bound")
music_player.add_last_song("Space Song - Beach House")
print(music_player) 
print("\n==============\n")
"""
OUTPUT:
==============


 MUSIC PLAYER QUEUE: 

Hey Jude - The Beatles, Teen Spirit - Nirvana, Bohemian Rhapsody - Queen , Lullaby - Atlas Bound, Space Song - Beach House

==============

"""