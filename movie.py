import random

def random_movie(movies):
    return random.choice(movies)

def random_genre(genres):
    genre, link = random.choice(list(genres.items()))
    return genre,link

def main():
    print ("Welcome to the random movie selector!")
    genres = {
        "Action" : "https://www.imdb.com/list/ls003041915/?view=compact",
        "Horror" : "https://www.imdb.com/list/ls003174642/?view=compact",
        "Comedy" : "https://www.imdb.com/list/ls000551766/?view=compact",
        "Romantic Comedy" : "https://www.imdb.com/list/ls058479560/?view=compact",
        "Science Fiction" : "https://www.imdb.com/list/ls055874673/?view=compact",
        "Drama" : "https://www.imdb.com/list/ls003196995/?view=compact",
        "Thriller" : "https://www.imdb.com/list/ls076166467/?view=compact",
        "Superhero" : "https://www.imdb.com/list/ls025474839/?view=compact",
        "Musical" : "https://www.imdb.com/list/ls028390287/?view=compact",
        "Animated" : "https://www.forbes.com/sites/entertainment/article/best-animated-movies/",
        "Crime" : "https://www.imdb.com/list/ls005762897/?view=compact",
        "History" : "https://www.imdb.com/list/ls000020512/?view=compact",
    }
    
    print("Did you need help selecting a genre or did you want to make a customized movie list?")
    print("1: Select a random genre\n2: Create a custom movie list")
    
    try:
        choice = int(input("Enter '1' or '2': ").strip())
    except ValueError:
        print("Invalid input. Try again. Make sure you enter '1' or '2'.")
        return
        
    
    if choice == 1:
        genre , link = random_genre(genres)
        print(f"Random genre: {genre}")
        print(f"You can find the best {genre} movies here: {link}")
    elif choice == 2:
        print("Enter your watchlist one by one. Type 'done' when finished")
        custom_movie_list = []
        while True:
            movie = input("Movie name: ").strip()
            if movie.lower() == "done":
                break
            custom_movie_list.append(movie)
        if custom_movie_list:
            print("Selecting random movie from your list...")
            selected_movie = random_movie(custom_movie_list)
            print(f"You should watch {selected_movie}")
        else:
            print("No movies were entered. Try again")
    else:
        print("Invalid choices. Please try again.")
        
if __name__ == "__main__":
    main()
