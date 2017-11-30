import media
# In the following, instances of class Movie for my three favorite movies are created
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
"https://images-na.ssl-images-amazon.com/images/I/519NBNHX5BL._SY445_.jpg",
"https://youtu.be/6hB3S9bIaco")

the_departed = media.Movie("The Departed",
"https://images-na.ssl-images-amazon.com/images/I/A1HL9+eKMyL._RI_.jpg",
"https://youtu.be/SGWvwjZ0eDc")

one_flew_over_the_cuckoos_nest = media.Movie("One Flew Over the Cuckoo's Nest",
"https://upload.wikimedia.org/wikipedia/en/2/26/One_Flew_Over_the_Cuckoo%27s_Nest_poster.jpg",
"https://youtu.be/2WSyJgydTsA")

# store the class Movie instances in a list for further usage within the fresh_tomates program
movies = [the_shawshank_redemption, the_departed, one_flew_over_the_cuckoos_nest]
