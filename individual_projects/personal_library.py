# JS, 1st, Personal Library Program

# ----- PSEUDOCODE -----
# list of a bunch of songs
# define view function with parameter songs
#   loop through songs
#       print the title and artist of each song
#   ask user if they want to leave and keep asking until not no
# define add function with parameter songs
#   ask user for the song title
#   ask user for the song artist
#   create a new song dictionary with that information
#   append the new song dictionary to songs
#   print a confirmation message
#   return songs
# define search function with parameter songs
#   ask user for their search
#   loop through songs
#       if user input in song name or artist
#           print that song
#   if no songs matched
#       print a message saying nothing was found
#   ask user if they want to leave and keep asking until not no
#   return songs
# define remove function with parameter songs
#   display all songs as a numbered list (index + 1)
#   ask user for the number of the song they want to remove
#   remove the song at that number - 1 from songs
#   print a confirmation message
#   ask user if they want to leave and keep asking until not no
#   return songs
# define main function
#   print introduction explaining what the program does
#   always loop:
#       ask user for their menu choice
#       if choice is 1
#           call view function
#       if choice is 2
#           call add function
#       if choice is 3
#           call remove function
#       if choice is 4
#           call search function
#       if choice is 5
#           print exit message
#           break out of loop
# call main function

# ----- CODE & PSUEDOCODE -----
# list of a bunch of songs
songs = [{"name": "smth idk", "artist": "idk"}, {"name": "smth idk 2", "artist": "idk 2"}, {"name": "smth idk 3", "artist": "idk 3"}]
# define view function with parameter songs
def view(songs):
#   loop through songs
    for song in songs:
#       print the title and artist of each song
        print(f" {song["name"]}, {song["artist"]}")
#   ask user if they want to leave and keep asking until not no
    leave = input("Would you like to leave? (y/n) ")
    while leave != "y" and leave != "yes":
        leave = input("Would you like to leave? (y/n) ")
# define add function with parameter songs
def add(songs):
#   ask user for the song title
    name = input("What is the song called? ").strip().title()
#   ask user for the song artist
    artist = input("Who is the artist? ").strip().title()
#   create a new song dictionary with that information
    new_song = {"name": name, "artist": artist}
#   append the new song dictionary to songs
    songs.append(new_song)
#   print a confirmation message
    print("Your song has been added.")
#   ask user if they want to leave and keep asking until not no
    leave = input("Would you like to leave? (y/n) ")
    while leave != "y" and leave != "yes":
        leave = input("Would you like to leave? (y/n) ")
#   return songs
    return songs
# define search function with parameter songs
def search(songs):
#   ask user for their search
    search = input("Input the name of your song or it's artist: ")
#   loop through songs
    count = 0
    for song in songs:
#       if user input in song name or artist
        if search in song["name"] or song["artist"]:
#           print that song
            print(f"{song["name"]}, {song["artist"]}")
    count += 1
#   if no songs matched
    if count == 0:
#       print a message saying nothing was found
        print("No song with that search was found.")
#   ask user if they want to leave and keep asking until not no
    leave = input("Would you like to leave? (y/n) ")
    while leave != "y" and leave != "yes":
        leave = input("Would you like to leave? (y/n) ")
#   return songs
    return songs
# define remove function with parameter songs
def remove(songs):
#   display all songs as a numbered list (index + 1)
    for song in songs:
        print(f"{songs.index(song)}, {song["name"]}")
#   ask user for the number of the song they want to remove
    number = input("What number song do you want to remove? ")
#   remove the song at that number - 1 from songs
    songs.remove(songs[number - 1])
#   print a confirmation message
    print("Your song has been removed. ")
#   ask user if they want to leave and keep asking until not no
    leave = input("Would you like to leave? (y/n) ")
    while leave != "y" and leave != "yes":
        leave = input("Would you like to leave? (y/n) ")
#   return songs
    return songs
# define main function
def main():
#   print introduction explaining what the program does
    print("stuff")
#   always loop:
    while True:
#       ask user for their menu choice
        menu = input("options")
        while menu == "1" and menu == "2" and menu == "3" and menu == "4" and menu == "5":
            menu = input("options but again")
#       if choice is 1
        if menu == "1":
#           call view function
            view(songs)
#       if choice is 2
        if menu == "2":
#           call add function
            add(songs)
#       if choice is 3
        if menu == "3":
#           call remove function
            remove(songs)
#       if choice is 4
        if menu == "4":
#           call search function
            search(songs)
#       if choice is 5
        if menu == "5":
#           print exit message
            print("Thanks for using the program!")
#           break out of loop
            break
# call main function
main()