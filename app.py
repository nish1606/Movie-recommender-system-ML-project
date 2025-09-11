import streamlit as st
import pickle
import pandas as pd 
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    try:
        response = requests.get(url, timeout=5) # Add a timeout for better practice
        response.raise_for_status() # Raises an exception for bad status codes
        data = response.json()
        
        if 'poster_path' in data and data['poster_path'] is not None:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
    except (requests.exceptions.RequestException, KeyError):
        return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"

def recommend(movie):
  movie_index = movies[movies['title']==movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
  
  recommended_movies = []
  recommended_movies_posters = []
  for i in movies_list:
    index = i[0]
    movie_id = movies.iloc[index]['id']
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies  = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie do you like?',
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    st.markdown("""
        <style>
        .stImage > img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            transition: transform 0.2s;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .stImage > img:hover {
            transform: scale(1.05);
        }
        .stHeader {
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            color: #f0f0f0;
            margin-bottom: 10px;
        }
        .stContainer {
            padding: 10px;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Create and display movie posters in a grid
    cols = st.columns(5)
    
    for i in range(5):
        with cols[i]:
            st.markdown(f'<div class="stContainer"><p class="stHeader">{names[i]}</p></div>', unsafe_allow_html=True)
            st.image(posters[i])