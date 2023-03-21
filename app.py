import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

st.set_page_config(layout="wide")


def get_poster(movie_id):
    json_file = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a958ef580cc1af01ad3200dd4faf3c97&language=en-US'.format(movie_id))
    data = json_file.json()
    return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommender(movie):
    lst = []
    movie_index = movies_tmdb[movies_tmdb['title'] == movie].index[0]
    distances_list = cosine_sim[movie_index]
    movie_list = sorted(list(enumerate(distances_list)), reverse=True, key=lambda x: x[-1])[1:11]
    movie_poster = []
    for j in movie_list:
        lst.append(movies_tmdb.iloc[j[0]].title)
        movie_poster.append(get_poster(movies_tmdb.iloc[j[0]].movie_id))
    return lst, movie_poster


movies_tmdb = pickle.load(open('movies_tmdb.pkl', 'rb'))
movies_tmdb = pd.DataFrame(movies_tmdb)

cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))
cosine_sim = pd.DataFrame(cosine_sim)

st.title("Movie Recommender System")

movie_selected = st.selectbox(
    'Choose a movie you want recommendations on',
    movies_tmdb['title'].values)

if st.button("Recommend"):
    recommendations, posters = recommender(movie_selected)
    # for i in recommendations:-*/=-
    #     st.write(i)

    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
        # , col9, col10 = st.columns(4)
    #
    with col1:
        st.text(recommendations[0])
        st.image(posters[0], width = 250)
    with col2:
        st.text(recommendations[1])
        st.image(posters[1], width = 250)
    with col3:
        st.text(recommendations[2])
        st.image(posters[2], width = 250)
    with col4:
        st.text(recommendations[3])
        st.image(posters[3], width = 250)
    with col5:
        st.text(recommendations[4])
        st.image(posters[4], width = 250)
    #     st.write("\n")
    with col6:
        st.text(recommendations[5])
        st.image(posters[5], width = 250)
    with col7:
        st.text(recommendations[6])
        st.image(posters[6], width = 250)
    with col8:
        st.text(recommendations[7])
        st.image(posters[7], width = 250)
    # with col9:
    #     st.text(recommendations[8])
    #     st.image(posters[8])
    # with col10:
    #     st.text(recommendations[9])
    #     st.image(posters[9])



