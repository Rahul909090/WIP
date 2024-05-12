# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:21:25 2024

@author: noodl

count_words(words (comma-separated string)):
    Return: occurrences (dict)
"""
#Question 1
books_genres = ["Horror", "Sci-Fi", "Horror", "Comedy",  "Comedy", "Horror", "Horror", "Comedy"]
genre_counts = {}

for x in books_genres:
    if x in genre_counts:
        genre_counts[x] = genre_counts[x] + 1
    else:
        genre_counts[x] = 1

print(genre_counts)

#Question 2
def count_words(words):
    dict = {}
    for x in words.split(","):
        if x in dict:
            dict[x] = dict[x] + 1
        else:
            dict[x] = 1
        
    return dict

print(count_words("the,university,of,north,florida,is,a,public,research,university,in,jacksonville,florida"))


#Question 3
dict = {"Doe": "A female deer.", "Ray": "A drop of golden sun.", "Me": "A name I call myself.", "Far": "A long way to run.", "Sew": "A needle pulling thread."}
print(dict["Ray"])
