# Importing my modules
import media
import fresh_tomatoes

# creating instances of the Movie class
napoleon_dynamite = media.Movie("Napoleon Dynamite",
                                "An epic adventure of the coolest guy ever.",
                                "http://ecx.images-amazon.com/images/I/51HzaJNRugL.jpg",  # noqa
                                "https://www.youtube.com/watch?v=ZHDi_AnqwN4",  # noqa
                                media.Movie.VALID_RATINGS[1])

nacho_libre = media.Movie("Nacho Libre",
                          "An epic adventure of an even cooler guy.",
                          "http://content8.flixster.com/movie/11/16/89/11168958_800.jpg",  # noqa
                          "https://www.youtube.com/watch?v=ElVSw6xpQ70",
                          media.Movie.VALID_RATINGS[1])

lord_of_the_rings = media.Movie("Lord of the Rings",
                                "An epic adventure about a bunch of dudes trying to destroy a ring.",  # noqa
                                "http://vignette3.wikia.nocookie.net/lotr/images/7/74/LOTRFOTRmovie.jpg/revision/latest?cb=20150203040819",  # noqa
                                "https://www.youtube.com/watch?v=Pki6jbSbXIY",
                                media.Movie.VALID_RATINGS[2])

despicable_me = media.Movie("Despicable Me",
                            "A story about an evil scientist and his orphan children.",  # noqa
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=nVwae09eSpo",
                            media.Movie.VALID_RATINGS[0])

avatar = media.Movie("Avatar",
                     "A story about blue guys.",
                     "http://s3.foxfilm.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",  # noqa
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4",
                     media.Movie.VALID_RATINGS[2])

mad_max = media.Movie("Mad Max Fury Road",
                      "A two hour long car chase scene.",
                      "http://cdn2-www.superherohype.com/assets/uploads/gallery/mad-max-fury-road_1/11110866_658246694280855_1682386295316885693_o.jpg",  # noqa
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8",
                      media.Movie.VALID_RATINGS[3])

# A list with all my movies in it
movies = [napoleon_dynamite, nacho_libre,
          lord_of_the_rings, despicable_me, avatar, mad_max]

# Use the open_movies function from fresh_tomatoes to create my html file
fresh_tomatoes.open_movies_page(movies)
