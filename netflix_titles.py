import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Plot number of TV shows vs Movies by type
# Load the data to the Data Frame
df = pd.read_csv("./data/netflix_titles.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)
print("-" * 100)

# Plot number of TV shows vs Movies by type use plt
plt.figure(figsize=(10, 8))
sns.countplot(x="type", data=df)
plt.title("Number of TV Shows vs Movies")
plt.show()

# Plot number of TV shows vs Movies by type as a pie chart
plt.figure(figsize=(10, 8))
df["type"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Number of TV Shows vs Movies")
plt.ylabel('')  
plt.show()

# Count the number of documentaries in the data frame
count_documentaries = df["listed_in"].str.contains("Documentaries", case=False)
print(count_documentaries.sum())

# Fixture of ratings and ages
ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}
# line break
print("-" * 100)

# fill the missing values in the rating column with NR
df["rating"] = df["rating"].fillna("NR")
# map each rating to the appropriate age group
df["age_group"] = df["rating"].map(ratings_ages) 
print(df["age_group"].value_counts())
print("-" * 100)

df["rating"] = df["rating"].replace(ratings_ages)
print(df["rating"].value_counts())
print("-" * 100)
# How many movies are made for kids
kid_movies = df[(df["rating"] == "Kids") & (df["type"] == "Movie")] # list comprehension for filtering
print(f"Number of movies made for kids:\n{kid_movies.shape[0]}")
print("-" * 100)
# use the str contains to filter the data frame for movies made for kids
kid_stuff = df[df["rating"].str.contains("Kids", case=False) & (df["type"] == "Movie")]
print(f"Number of movies made for kids:\n{kid_stuff.shape[0]}")
print("-" * 100)

# What is the earliest TV show that was added to Netlfix and then plot number of movies by release year
df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')
earliest_tv_show = df[(df["type"] == "TV Show") & (df["date_added"].notnull())]["release_year"].min()
print(f"Earliest TV Show on Netflix is from \n{earliest_tv_show}")
print("-" * 100)

# When the earliest TV show was added to Netflix 
earliest_tv_show_added = df[(df["type"] == "TV Show") & (df["date_added"].notnull())]["date_added"].min()
print(f"Earliest TV Show on Netflix was added on \n{earliest_tv_show_added}")
print("-" * 100)

# Print the number of movies by release year in ascending order by release year
added_to_netflix = df[df["date_added"].notnull()]["release_year"].value_counts().sort_index()
print("Number of movies by release year: \n", added_to_netflix)
print("-" * 100)

#! Plot the number of movies by release year (scatter plot) AND it is NOT when they were added to NETFLIX
plt.figure(figsize=(10, 8))
sns.scatterplot(x=added_to_netflix.index, y=added_to_netflix.values)
plt.title("Number of Movies by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Movies")
plt.show()

# Get the top 10 directors by number of movies in the US
condition_us = df["country"].str.contains("United States", case=False, na=False)
top_10_directors_us = df[condition_us]["director"].fillna("Unknown").value_counts().head(10)
print("Top 10 directors by number of movies in the US: \n", top_10_directors_us)
print("-" * 100)

# Create a list to explode the data and duplicate the rows in the data frame in order to have one country per row 
df["country"] = df["country"].str.split(",")
df_new = df.explode("country")
print(df_new.head(10))
print("-" * 100)