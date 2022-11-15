import spacy
import textwrap
nlp = spacy.load('en_core_web_md')

### This program takes the description of a movie that the user has just watched,
### then returns the movie with the highest similarity in movies.txt using spacy

def watch_next(desc):
    highest_similarity = None
    desc = nlp(desc)
    #Opening file and reading it
    try:
        with open("movies.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No movies found.")
        return False
    
    #iterating through lines
    for line in lines:
        movie_list = line.split(":")
        current_desc = nlp(movie_list[1])
        #getting similarity between 2 descriptions
        similarity = desc.similarity(current_desc)
        #If similarity is more than highest similarity, this is highest similarity movie.
        if highest_similarity == None or similarity > highest_similarity:
            highest_similarity = similarity
            next_movie = movie_list[0]
            next_desc = movie_list[1]
    #Returning movie, description, and similarity
    return next_movie, next_desc, highest_similarity



desc = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""
#Putting Planet Hulk description into function
movie, description, similarity = watch_next(desc)
#getting the percentage similarity
percent_similarity = round((similarity*100), 2)
#printing the movie, description (text wrapped), and the similarity percentage to userasd

print("""======== WATCH NEXT ========""")
print(f"{movie}")
print(textwrap.fill(f"{description}", width=80))
print(f"{percent_similarity}% Match")