import pandas as pd
import plotly.express as px

# reads csv file from netflix
netflix_df = pd.read_csv("datasets\\netflix_titles.csv", usecols=["type", "listed_in"])

# reads csv file from amazon prime
prime_df = pd.read_csv("datasets\\amazon_prime_titles.csv", usecols=["type", "listed_in"])

# reads csv file from hulu
hulu_df = pd.read_csv("datasets\\hulu_titles.csv", usecols=["type", "listed_in"])

# reads csv file from disney+
disney_df = pd.read_csv("datasets\\disney_plus_titles.csv", usecols=["type", "listed_in"])

# splits up the multiple genres per film by commas
netflix_df['listed_in'] = netflix_df['listed_in'].str.split(", ")
prime_df['listed_in'] = prime_df['listed_in'].str.split(", ")
hulu_df['listed_in'] = hulu_df['listed_in'].str.split(", ")
disney_df['listed_in'] = disney_df['listed_in'].str.split(", ")

genres = set()
# gets all available genres in netflix, prime, hulu, and disney+
for row in netflix_df.itertuples():
    genres.update(row.listed_in)

for row in prime_df.itertuples():
    genres.update(row.listed_in)

for row in hulu_df.itertuples():
    genres.update(row.listed_in)

for row in disney_df.itertuples():
    genres.update(row.listed_in)

# makes empty dictionaries for netflix
netflix_genre_count = {}
netflix_genre_count_movie_and_shows = {"Movie": {}, "TV Show": {}}
for genre in genres:
    netflix_genre_count[genre] = 0
    netflix_genre_count_movie_and_shows["Movie"][genre] = 0
    netflix_genre_count_movie_and_shows["TV Show"][genre] = 0

# makes empty dictionaries for prime
prime_genre_count = {}
prime_genre_count_movie_and_shows = {"Movie": {}, "TV Show": {}}
for genre in genres:
    prime_genre_count[genre] = 0
    prime_genre_count_movie_and_shows["Movie"][genre] = 0
    prime_genre_count_movie_and_shows["TV Show"][genre] = 0

# makes empty dictionaries for hulu
hulu_genre_count = {}
hulu_genre_count_movie_and_shows = {"Movie": {}, "TV Show": {}}
for genre in genres:
    hulu_genre_count[genre] = 0
    hulu_genre_count_movie_and_shows["Movie"][genre] = 0
    hulu_genre_count_movie_and_shows["TV Show"][genre] = 0

# makes empty dictionaries for disney
disney_genre_count = {}
disney_genre_count_movie_and_shows = {"Movie": {}, "TV Show": {}}
for genre in genres:
    disney_genre_count[genre] = 0
    disney_genre_count_movie_and_shows["Movie"][genre] = 0
    disney_genre_count_movie_and_shows["TV Show"][genre] = 0
    
# populates netflix dictionaries
for row in netflix_df.itertuples():
    for genre in netflix_genre_count:
        if genre in row.listed_in:
            netflix_genre_count[genre] += 1

            if row.type == "Movie":
                netflix_genre_count_movie_and_shows["Movie"][genre] += 1
            elif row.type == "TV Show":
                netflix_genre_count_movie_and_shows["TV Show"][genre] += 1

# populates prime dictionaries
for row in prime_df.itertuples():
    for genre in prime_genre_count:
        if genre in row.listed_in:
            prime_genre_count[genre] += 1

            if row.type == "Movie":
                prime_genre_count_movie_and_shows["Movie"][genre] += 1
            elif row.type == "TV Show":
                prime_genre_count_movie_and_shows["TV Show"][genre] += 1

# populates hulu dictionaries
for row in hulu_df.itertuples():
    for genre in hulu_genre_count:
        if genre in row.listed_in:
            hulu_genre_count[genre] += 1

            if row.type == "Movie":
                hulu_genre_count_movie_and_shows["Movie"][genre] += 1
            elif row.type == "TV Show":
                hulu_genre_count_movie_and_shows["TV Show"][genre] += 1

# populates disney dictionaries
for row in disney_df.itertuples():
    for genre in disney_genre_count:
        if genre in row.listed_in:
            disney_genre_count[genre] += 1

            if row.type == "Movie":
                disney_genre_count_movie_and_shows["Movie"][genre] += 1
            elif row.type == "TV Show":
                disney_genre_count_movie_and_shows["TV Show"][genre] += 1

# Sort netflix dictionaries by keys
netflix_genre_count = dict(sorted(netflix_genre_count.items()))
netflix_genre_count_movie_and_shows["Movie"] = dict(sorted(netflix_genre_count_movie_and_shows["Movie"].items()))
netflix_genre_count_movie_and_shows["TV Show"] = dict(sorted(netflix_genre_count_movie_and_shows["TV Show"].items()))

# Sort prime dictionaries by keys
prime_genre_count = dict(sorted(prime_genre_count.items()))
prime_genre_count_movie_and_shows["Movie"] = dict(sorted(prime_genre_count_movie_and_shows["Movie"].items()))
prime_genre_count_movie_and_shows["TV Show"] = dict(sorted(prime_genre_count_movie_and_shows["TV Show"].items()))

# Sort hulu dictionaries by keys
hulu_genre_count = dict(sorted(hulu_genre_count.items()))
hulu_genre_count_movie_and_shows["Movie"] = dict(sorted(hulu_genre_count_movie_and_shows["Movie"].items()))
hulu_genre_count_movie_and_shows["TV Show"] = dict(sorted(hulu_genre_count_movie_and_shows["TV Show"].items()))

# Sort disney+ dictionaries by keys
disney_genre_count = dict(sorted(disney_genre_count.items()))
disney_genre_count_movie_and_shows["Movie"] = dict(sorted(disney_genre_count_movie_and_shows["Movie"].items()))
disney_genre_count_movie_and_shows["TV Show"] = dict(sorted(disney_genre_count_movie_and_shows["TV Show"].items()))

# preparing the labels for the treemap
length = len(genres) * 2

netflix_list = ["Netflix"] * length
prime_list = ["Prime"] * length
hulu_list = ["Hulu"] * length
disney_list = ["Disney+"] * length

platforms = []
platforms.extend(netflix_list)
platforms.extend(prime_list)
platforms.extend(hulu_list)
platforms.extend(disney_list)


genre_list = sorted(list(genres)) * 8

types = []
types.extend(["Movie"] * len(genres))
types.extend(["TV Show"] * len(genres))
types.extend(["Movie"] * len(genres))
types.extend(["TV Show"] * len(genres))
types.extend(["Movie"] * len(genres))
types.extend(["TV Show"] * len(genres))
types.extend(["Movie"] * len(genres))
types.extend(["TV Show"] * len(genres))

values = []

# adds all values from netflix dict
for video in netflix_genre_count_movie_and_shows:
    for genre in netflix_genre_count_movie_and_shows[video]:
        values.append(netflix_genre_count_movie_and_shows[video][genre])\

# adds all values from prime dict
for video in prime_genre_count_movie_and_shows:
    for genre in prime_genre_count_movie_and_shows[video]:
        values.append(prime_genre_count_movie_and_shows[video][genre])

# adds all values from hulu dict
for video in hulu_genre_count_movie_and_shows:
    for genre in hulu_genre_count_movie_and_shows[video]:
        values.append(hulu_genre_count_movie_and_shows[video][genre])

# adds all values from disney+ dict
for video in disney_genre_count_movie_and_shows:
    for genre in disney_genre_count_movie_and_shows[video]:
        values.append(disney_genre_count_movie_and_shows[video][genre])
        

# Hierarchical data
data = {
    "Platform": platforms,
    
    "Genre": genre_list,
    
    "Type": types,
    
    "Value": values     
}

# creates a DataFrame for the newly transformed data
treemap_df = pd.DataFrame(data)

# Plotting the treemap
fig = px.treemap(
    treemap_df, 
    path=["Platform", "Genre", "Type"],    
    values="Value",                        
    color="Platform",                      
    color_discrete_map={                   
        "Netflix": "rgb(229, 9, 20)",
        "Hulu": "rgb(28, 231, 131)",
        "Prime Video": "rgb(0, 168, 225)",
        "Disney+": "rgb(17, 60, 207)"
    },
    title="Streaming Services by Genre and Type"
)

fig.show()




