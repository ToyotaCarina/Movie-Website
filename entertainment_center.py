# -*- coding: utf-8 -*-
# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# This file contains instances of the class Movie, defined in media.py.
# Instances filles data to such attributes as title, year, duration,
# genre, storyline, url til poster (poster_image_url) and
# trailer (trailer_youtube_url)

# After you run this code, file fresh_tomatoes.html creates in the same
# directory and opens

import media
import fresh_tomatoes

insidious = media.Movie(
    "Insidious", year = 2010, duration = 103, genre = ["Horror", "Thriller"],
    storyline = "A family discovers that dark spirits have invaded their home after their son inexplicably falls into an endless sleep. When they reach out to a professional for help, they learn things are a lot more personal than they thought.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyOTAxMDA0OF5BMl5BanBnXkFtZTcwNzgwNTc1NA@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/0Q0x8KYwnns")

saw = media.Movie(
    "Saw", year = 2004, duration = 103, genre = ["Horror", "Mystery", "Crime"],
    storyline = "Obsessed with teaching his victims the value of life, a deranged, sadistic serial killer abducts the morally wayward. Once captured, they must face impossible choices in a horrific game of survival. The victims must fight to win their lives back, or die trying...",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMzQ2ZTBhNmEtZDBmYi00ODU0LTgzZmQtNmMxM2M4NzM1ZjE4XkEyXkFqcGdeQXVyNjE5MjUyOTM@._V1_.jpg",
    trailer_youtube_url =  "https://youtu.be/gRmmYX1rW6A")

lovely_bones = media.Movie(
    "The Lovely Bones", year = 2009, duration = 136, genre = ["Fantasy", "Drama"],
    storyline = "After being brutally murdered, 14-year-old Susie Salmon watches from heaven over her grief-stricken family -- and her killer. As she observes their daily lives, she must balance her thirst for revenge with her desire for her family to heal.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwNDA1MTM2MF5BMl5BanBnXkFtZTcwMzg3NDcwMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/PTZYYtUJpak")

repo_opera = media.Movie(
    "Repo! The Genetic Opera", year = 2008, duration = 98 , genre = ["Horror", "Comedy", "Music", "Science Fiction"],
    storyline = "A worldwide epidemic encourages a bio-tech company to launch an organ-financing program similar in nature to a standard car loan. The repossession clause is a killer, however.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BYTkyZWEzYmYtMTFhMi00YTkzLTkyOWQtMDg1MTQwMTE3M2Y0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/3_V_mkBp93Y")

lamb_silence = media.Movie(
    "The Silence of the Lambs", year = 1991, duration = 119 , genre = ["Crime", "Drama", "Thriller"],
    storyline = "FBI trainee, Clarice Starling ventures into a maximum-security asylum to pick the diseased brain of Hannibal Lecter, a psychiatrist turned homicidal cannibal. Starling needs clues to help her capture a serial killer. But her Faustian relationship with Lecter soon leads to his escape, and now two deranged killers are on the loose.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BNjNhZTk0ZmEtNjJhMi00YzFlLWE1MmEtYzM1M2ZmMGMwMTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/RuX2MQeb8UM")

split = media.Movie(
    "Split", year = 2016, duration = 117, genre = ["Horror", "Thriller"],
    storyline = "Though Kevin has evidenced 23 personalities to his trusted psychiatrist, Dr. Fletcher, there remains one still submerged who is set to materialize and dominate all the others. Compelled to abduct three teenage girls led by the willful, observant Casey, Kevin reaches a war for survival among all of those contained within him — as well as everyone around him — as the walls between his compartments shatter apart.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BZTJiNGM2NjItNDRiYy00ZjY0LTgwNTItZDBmZGRlODQ4YThkL2ltYWdlXkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    trailer_youtube_url = "https://youtu.be/fAN_lkPEg4M")

illusionist = media.Movie(
    "The Illusionist", year = 2006, duration = 110, genre = ["Fantasy", "Drama", "Thriller", "Romance"],
    storyline = "With his eye on a lovely aristocrat, a gifted illusionist named Eisenheim uses his powers to win her away from her betrothed, a crowned prince. But Eisenheim's scheme creates tumult within the monarchy and ignites the suspicion of a dogged inspector.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BY2VkMzZlZDAtNTkzNS00MDIzLWFmOTctMWQwZjQ1OWJiYzQ1XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX700_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/i0xO64icGSY")

chloe = media.Movie(
    "Chloe", year = 2009, duration = 96, genre = ["Drama", "Thriller", "Mystery"],
    storyline = "A doctor hires an escort to seduce her husband, whom she suspects of cheating, though unforeseen events put the family in danger.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMzExNTkyMV5BMl5BanBnXkFtZTcwODUyMzAyMw@@._V1_SY1000_CR0,0,690,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/a13PqQq4fv0")

hard_candy = media.Movie(
    "Hard Candy", year = 2005, duration = 103, genre = ["Drama", "Thriller"],
    storyline = "A mature 14-year old girl meets a charming 32-year old photographer on the Internet. Suspecting that he is a pedophile, she goes to his home in an attempt to expose him.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0MzgzNTI3N15BMl5BanBnXkFtZTcwNDk3MDIzMQ@@._V1_SY1000_SX675_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/1PXYjFl0uXg")

mrs_doubtfire = media.Movie(
    "Mrs. Doubtfire", year = 1993, duration = 125, genre = ["Comedy", "Drama", "Family"],
    storyline = "Loving but irresponsible dad Daniel Hillard, estranged from his exasperated spouse, is crushed by a court order allowing only weekly visits with his kids. When Daniel learns his ex needs a housekeeper, he gets the job -- disguised as an English nanny. Soon he becomes not only his children's best pal but the kind of parent he should have been from the start.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMDUzODE1N15BMl5BanBnXkFtZTgwNTU5NTYxMTE@._V1_.jpg",
    trailer_youtube_url =  "https://youtu.be/Ec3vg-n9yK8")

breakfast_on_pluto = media.Movie(
    "Breakfast on Pluto", year = 2005, duration = 128, genre = ["Comedy", "Drama"],
    storyline = "In the 1970s, a foundling lad, Patrick 'Kitten' Braden, comes of age by leaving his Irish town for London, in part to look for his mother and in part because his trans-gender nature is beyond the town's understanding.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BYmU5YjJlYjEtNGE5Ni00ODA5LWE4ZTAtNzZlNDhlODIzMzE4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/5blVrqSKiRc")

peacock = media.Movie(
    "Peacock", year = 2010, duration = 90, genre = ["Mystery", "Thriller"],
    storyline = "A man with a split personality fools his small town into believing his two alter egos are man and wife, although a struggling young mother holds the key to his past and sparks a battle between the personalities.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA3MTg2NDA0Ml5BMl5BanBnXkFtZTcwNzI4ODIzMw@@._V1_SY1000_CR0,0,702,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/NPEzcAG4E5s")

danish_girl = media.Movie(
    "The Danish Girl", year = 2015, duration = 120, genre = ["Drama"],
    storyline = "When Gerda Wegener asks her husband Einar to fill in as a portrait model, Einar discovers the person she's meant to be and begins living her life as Lili Elbe. Having realized her true self and with Gerda's love and support, Lili embarks on a groundbreaking journey as a transgender pioneer.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA0NjA4NjE2Nl5BMl5BanBnXkFtZTgwNzIxNTY2NjE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/7lQJRdTfdmY")

miserables = media.Movie(
    "Les Misérables", year = 2012, duration = 157, genre = ["Drama", "Music", "Romance"],
    storyline = "An adaptation of the successful stage musical based on Victor Hugo's classic novel set in 19th-century France, in which a paroled prisoner named Jean Valjean seeks redemption.",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ4NDI3NDg4M15BMl5BanBnXkFtZTcwMjY5OTI1OA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/YmvHzCLP6ug")

phantom_of_the_opera = media.Movie(
    "The Phantom of the Opera", year = 2004, duration = 143, genre = ["Drama", "Thriller", "Romance"],
    storyline = "Deformed since birth, a bitter man known only as the Phantom lives in the sewers underneath the Paris Opera House. He falls in love with the obscure chorus singer Christine, and privately tutors her while terrorizing the rest of the opera house and demanding Christine be given lead roles. Things get worse when Christine meets back up with her childhood acquaintance Raoul and the two fall in love",
    poster_image_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BNDczNzg4OTM3MV5BMl5BanBnXkFtZTcwOTQzMTEzMw@@._V1_SY1000_CR0,0,676,1000_AL_.jpg",
    trailer_youtube_url =  "https://youtu.be/y3ExznvzqGU")

movies = [
    insidious, saw, lovely_bones, repo_opera, lamb_silence,
    split, illusionist, chloe, hard_candy, mrs_doubtfire,
    breakfast_on_pluto, peacock, danish_girl, miserables,
    phantom_of_the_opera
    ]

# Creates and opens fresh_tomatoes.html file
fresh_tomatoes.open_movies_page(movies)
