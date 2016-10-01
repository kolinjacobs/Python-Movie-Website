import media
import fresh_tomatoes

# creates 6 movie objects for later use
toy_story = media.Movie("The Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, \
                        finding solace and eventual redemption through acts \
                        of common decency.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=NmzuHjWmXOc")
avatar = media.Movie("The Godfather",
                        "The aging patriarch of an organized crime \
                        dynasty transfers control of his clandestine \
                        empire to his reluctant son.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")
school_of_rock = media.Movie("Pulp Fiction",
                        "The lives of two mob hit men, a boxer,\
                        a gangster's wife, and a pair of diner bandits \
                        intertwine in four tales of violence and redemption.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=s7EdQ4FqbhY")
ratatouille = media.Movie("Fight Club",
                        "An insomniac office worker, looking for a way to\
                        change his life, crosses paths with a devil-may-care\
                        soap maker, forming an underground fight club that evolves\
                        into something much, much more.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")
midnight_in_paris = media.Movie("Forrest Gump",
                        "Forrest Gump, while not intelligent, has accidentally\
                        been present at many historic moments, but his true love,\
                        Jenny Curran, eludes him.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=bLvqoHBptjg")
hunger_games = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing\
                        technology, is given the inverse task of planting an idea\
                        into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

# adds movie objects to a list
movies = [toy_story, avatar, school_of_rock, ratatouille,midnight_in_paris, hunger_games]

# passes list into the open_movies_page funtion inorder to create the webpage
fresh_tomatoes.open_movies_page(movies)
