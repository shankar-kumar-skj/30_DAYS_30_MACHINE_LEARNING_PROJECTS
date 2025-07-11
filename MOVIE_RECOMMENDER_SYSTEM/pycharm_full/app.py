# tmdb api key = 8265bd1679663a7ea12ac168da84d2e8
# https://api.themoviedb.org/3/movie/11?api_key=8265bd1679663a7ea12ac168da84d2e8

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    # first findig the title => index number in dataframe
    movie_index=movies[movies['title']==movie].index[0]
    # finding cosine_similarity of that vector of that index
    distances=similarity[movie_index]
    # shorting the similarity in revese order to get higher priority first
    # that more similar come first
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        # fetch poster from API

        # printing the name with the help of index of the similar vector finded by cosine similarity
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('D:/FINAL_YEAR_PROJECTS/MACHINE_LEARNING_PROJECT/MOVIE_RECOMMENDER_SYSTEM/pycharm_full/movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity = pickle.load(open('D:/FINAL_YEAR_PROJECTS/MACHINE_LEARNING_PROJECT/MOVIE_RECOMMENDER_SYSTEM/pycharm_full/similarity.pkl', 'rb'))
# print in streamlit
st.title('Movie Recommender System')
# giving option to the user
selected_movie_name= st.selectbox('How would you like to be select?', movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend (selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

