import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

princess_mononoke = media.Movie("Princess Mononoke",
                        "A guy tries to save a forest",
                        "https://upload.wikimedia.org/wikipedia/en/2/24/Princess_Mononoke_Japanese_Poster_%28Movie%29.jpg",
                        "https://www.youtube.com/watch?v=pkWWWKKA8jY")

pride_and_prejudice = media.Movie("Pride and Prejudice",
                        "Love story",
                        "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
                        "https://www.youtube.com/watch?v=1dYv5u6v55Y")
the_scorpion_king = media.Movie("The Scorpion King",
                        "Cool egyptian movie",
                        "https://upload.wikimedia.org/wikipedia/en/1/1d/The_Scorpion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=CmEKTae2iys")
hellboy = media.Movie("Hellboy",
                        "Devil looking dude",
                        "https://upload.wikimedia.org/wikipedia/en/6/6b/Hellboy_poster.jpg",
                        "https://www.youtube.com/watch?v=Ob9J3kCELXE")

movies = [toy_story, avatar, princess_mononoke, pride_and_prejudice, the_scorpion_king, hellboy]

fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
