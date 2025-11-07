
# Movie Recommender System – Machine Learning Project

This project implements a content-based movie recommender system using machine learning techniques. It analyzes movie metadata and suggests similar movies based on user input.

## Overview

The system uses the TMDB 5000 movie dataset to build a recommendation engine. It applies natural language processing and vector similarity to identify movies with similar content.

## Files

- `movie_recommender_system.ipynb`: Main notebook containing all code for data processing, feature engineering, and recommendation logic.
- `tmdb_5000_movies.csv`: Dataset with metadata for 5000 movies from TMDB.

## Features

- Content-based filtering using movie metadata (genres, keywords, cast, director)
- Text vectorization using CountVectorizer
- Cosine similarity for movie recommendations
- Simple interface for querying similar movies

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/nish1606/Movie-recommender-system-ML-project.git
   cd Movie-recommender-system-ML-project
   ```

2. Install required libraries:
   ```
   pip install pandas numpy scikit-learn nltk
   ```

3. Launch the notebook:
   ```
   jupyter notebook movie_recommender_system.ipynb
   ```

## How It Works

- The dataset is cleaned and merged to extract relevant features.
- A combined feature string is created for each movie.
- CountVectorizer converts text into numerical vectors.
- Cosine similarity is used to find movies with similar vectors.
- The user inputs a movie title, and the system returns the top 5 similar movies.

## Example

```python
recommend('Avatar')
```

Output:
- Guardians of the Galaxy
- Star Trek Into Darkness
- Star Wars: The Force Awakens
- John Carter
- The Avengers

## Future Enhancements

- Add collaborative filtering based on user ratings
- Build a web interface using Flask or Streamlit
- Integrate with TMDB API for real-time data

## License

This project is licensed under the MIT License.

