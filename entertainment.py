import media
import fresh_tomatoes

# Create the instances for the movie class
toy_story = media.Movie("Toy Story",
                        "80 minutes",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avator = media.Movie("Avator",
                     "162 minutes",
                     "A story of a marine on another planet. ",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

rogue_one = media.Movie("ROGUE ONE: A STAR WARS STORY",
                        "133 minutes",
                        "In a time of conflict, a group of unlikely heroes band"
                        " together on a mission to steal the plans to the Death"
                        " Star, the Empire's ultimate weapon of destruction.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png", # noqa
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

la_la_land = media.Movie("La La Land",
                         "128 minutes",
                         "Set in modern day Los Angeles, this original musical "
                         "about everyday life explores the joy and pain of "
                         "pursuing your dreams.",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png", # noqa
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

doctor_strange = media.Movie("Doctor Strange",
                             "130 minutes",
                             "A disgraced former surgeon named Stephen Strange "
                             "becomes a powerful sorcerer under the tutelage of"
                             " a mystic known as the Ancient One",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg", # noqa
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

the_godfather = media.Movie("The Godfather",
                            "175 minutes",
                            "Michael, a free thinker who defied his father by "
                            "enlisting in the Marines to fight in World War "
                            " II, has returned a captain and a war hero.",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg", # noqa
                            "https://www.youtube.com/watch?v=sY1S34973zA")

# Store all the movies instances in a list
movies = [toy_story, avator, rogue_one, la_la_land, doctor_strange, 
         the_godfather]

# Call the fresh tomatoes method that takes the list of movies and creates a
#website
fresh_tomatoes.open_movies_page(movies)

