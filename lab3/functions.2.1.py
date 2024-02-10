def hoho(movies):
    result = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            return True
    return False       

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
]
print(hoho(movies))

