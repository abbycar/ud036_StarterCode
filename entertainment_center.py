"""This module is where movies are initialized, stored, and displayed to the
movie trailer webpage.
"""
import media
import fresh_tomatoes

""" Six movies are created to populate the webpage.
Each movie contains its title, a short description, a source for it's box art,
and a link to it's trailer on YouTube.

For this version of the webpage, no short description will be displayed.
"""

# Toy Story movie: movie title, short summary, box art, and YouTube movie trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

# Avatar movie: movie title, short summary, box art, and YouTube movie trailer
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

# Princess Mononoke movie: movie title, short summary, box art, and YouTube movie trailer
princess_mononoke = media.Movie(
    "Princess Mononoke",
    "A guy tries to save a forest",
    "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
    "https://www.youtube.com/watch?v=pkWWWKKA8jY"
    )

# Pride and Prejudice movie: movie title, short summary, box art, and YouTube movie trailer
pride_and_prejudice = media.Movie(
    "Pride and Prejudice",
    "Love story",
    "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
    "https://www.youtube.com/watch?v=1dYv5u6v55Y"
    )

# The Scorpion King movie: movie title, short summary, box art, and YouTube movie trailer
the_scorpion_king = media.Movie(
    "The Scorpion King",
    "Cool egyptian movie",
    "https://upload.wikimedia.org/wikipedia/en/1/1d/The_Scorpion_King_poster.jpg",
    "https://www.youtube.com/watch?v=CmEKTae2iys"
    )

# Hell Boy movie: movie title, short summary, box art, and YouTube movie trailer
hellboy = media.Movie(
    "Hellboy",
    "Devil looking dude",
    "https://upload.wikimedia.org/wikipedia/en/6/6b/Hellboy_poster.jpg",
    "https://www.youtube.com/watch?v=Ob9J3kCELXE")

# Add all the movies to a list
movies = [
    toy_story,
    avatar,
    princess_mononoke,
    pride_and_prejudice,
    the_scorpion_king, hellboy
    ]

# Open the webpage in a browser and display the movies from the movies list
fresh_tomatoes.open_movies_page(movies)
