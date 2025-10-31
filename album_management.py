# Program showcasing album management

class Album():
    # Constructor with following instance variables
    def __init__(self,album_name,album_artist,number_of_songs):
            self.album_name = album_name
            self.album_artist = album_artist
            self.number_of_songs = number_of_songs

    # _str_ method returing Album object
    def __str__(self):
            return (f"{self.album_name},{self.album_artist},{self.number_of_songs}")



# -------------------------
# Top Level Helper Functions 
# --------------------------   


    # Funtion to find index of album name in albums2
def find_index(album_name,album_list):
        for index, album in enumerate(album_list):
            if album.album_name == album_name:
                return index
           
        return None

    # Function sorting albums within list via the number of songs
def sort_album_according_to_no_of_songs(album_list):
        sort_by_no_of_songs = sorted((album_list), key =lambda album: album.number_of_songs) 
        for album in sort_by_no_of_songs:
            print(album)

    # Function sorting albums within list by name 
def sort_album_by_name(album_list):
        albums_sorted_by_name = sorted((album_list),key = lambda album:album.album_name)
        print("Sorted by album name:")
        for album in albums_sorted_by_name:
            print(album)

def displaying_album(album_list):
        for album in album_list:
            print(album)


# Example usage
    
albums1 = [Album("NBA","NBA Younboy", 10), 
           Album("Flowers","Bucie", 9),
           Album("KOP","Kabza de small",22),
           Album("Sunday", "Jimmy Swaggert",10),
           Album("Zulu","Simi",12)
           ]

# Displaying Album 1 
print("Album 1: ")
displaying_album(albums1)
print("\n")

# Sorting albums according to the number of songs
print("Sorted according to the number of songs in Album 1: ")
sort_album_according_to_no_of_songs(albums1)
print("\n")
    

# Tuple Unpacking - to swap the first and second element respectively
print("Swapped element 1 & 2: ")
albums1[0],albums1[1] = albums1[1],albums1[0]
displaying_album(albums1)
print("\n")

# List of albums in albums2
albums2 = [Album("Levels","AKA",13),
           Album("Yellow","Shane Eagle",10),
           Album("ZWMSP","Nasty C",11),
           Album("Wena","Anatii",14),
           Album("Fire", "Ta Fire",4)
           ]

print("Album 2: ")
displaying_album(albums2)
print("\n")

# Copying album1 'albums' to album2
print("album1 copied into album2: ")
albums2.extend(albums1)
displaying_album(albums2)
print("\n")


# Adding 2 new albums into album2
print("Adding 2 new albums: ")
albums3 = [ Album("Dark Side of the Moon","Pink Floyd",9),
            Album("Oops!...I Did It Again","Britney Spears",16)
           ]

albums2.extend(albums3)
displaying_album(albums2)
print("\n")

# Sorting albums in albums2 alphabetically
print("Album 2 sorted in alphabetical order:")
sort_album_by_name(albums2)
print("\n")

# Searching for album in albums2 list & printing its index in the list
print("The index for the following:")
result = find_index("Dark Side of the Moon",albums2)
print(result)






