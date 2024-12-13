from flask import Flask, render_template_string, request, redirect
import random 

app = Flask(__name__)

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

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        choice = request.form.get("choice")
        if choice == "random-genre":
            return redirect("/random-genre")
        elif choice == "custom-movie-list":
            return redirect("/custom-movie-list")
    return render_template_string("""
        <h1>Welcome to the Random Movie Selector!</h1>
        <form method="post">
            <label for="choice"> Select an option: </label><br><br>
            <input type="radio" id="random-genre" name ="choice" value= "random-genre">
            <label for="random-genre">Random Genre</label><br>
            <input type="radio" id="custom-movie-list" name="choice" value="custom-movie-list">
            <label for="custom-movie-list">Create a custom movie list</label><br><br>
            <input type="submit" value="Submit">
        </form>
        """)

@app.route("/random-genre")

def random_genre():
    genre, link = random.choice(list(genres.items()))
    return render_template_string(
        f"<h1>Random Genre: {genre}</h1>"
        f"<p><a href = '{link}' target = '_blank'>Explore top {genre} movies </a></p>"
    )

@app.route("/custom-movie-list", methods = ["POST","GET"])
def custom_movie_list():
    if request.method=="POST":
        custom_movies = request.form.get("custom-movies")
        if custom_movies:
            movie_list = custom_movies.split("\n")
            selected_movie = random.choice(movie_list)
            return render_template_string(
                f"<h1>Your custom movie list</h1>"
                f"<p>You should watch {selected_movie}</p>"
            )
        else:
            return render_template_string(
                f"<h1>Your custom movie list</h1>"
                f"<p>Nothing was entered. Please add some movies to the list.</p>"
            )
    return render_template_string("""
        <h1>Create your custom movie</h1>
        <form method="post">
            <label for="custom-movies">Enter some movies, one per line:</label><br><br>       
            <textarea id = "custom-movies" name = "custom-movies" rows="10" cols ="30"></textarea><br><br>
            <input type = "submit" value="Submit">
        </form>  
    """)
    
if __name__ == "__main__":
    app.run(debug=True)
