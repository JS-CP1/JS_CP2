# JS, 1st, Personal Library Program

# ----- PSUEDOCODE -----
#list of a bunch of songs
#define song function with parameter song
#   print all song details
#   ask user if they want to leave until their answer is yes
#define add function with parameter songs
#   ask the user what song they would like along with all the details of that song
#   append that info to songs
#   return songs
#define search function with parameter songs
#   ask the user for an input
#   pull up all songs with their input in it
#   return songs
#define remove function with parameter songs
#   ask the user for an input
#   
#   return songs

# ----- CODE & PSUEDOCODE -----
def song(song):
    #print song details
    leave = input("Would you like to leave? (y/n) ")
    print("\x1b[2K\r", end="")
    while leave != "y":
        leave = input("Would you like to leave? (y/n) ")
    print("\033c", end="")
def add(songs):

    return songs
def search(songs):
    return songs
def remove(songs):
    return songs
song(song="a")