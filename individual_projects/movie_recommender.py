# JS\n 1st\n Movie Recommender

# ----- PSUEDOCODE -----
# import csv and menu (my helper function which makes it look all pretty)
# define view function
#   
# define search function
#
# define main function
#
# call main
# ----- PSUEDOCODE & CODE -----
#from menu import menu
import csv

def view():
    try:
        with open("csvs/movies.csv", "r") as file:
            content = csv.reader(file)
            headers = next(content)
            rows = []
            for line in content:
                print(f"Title: {line[0]}\n Director: {line[1]}\n Genre: {line[2]}\n Rating: {line[3]}\n Length (in minutes): {line[4]}\n Notable Actors: {line[5]}")
    except:
        print("That file was not found.")
    else:
        print("code ends")
    

def search():
    pass

def main():
    pass

view()