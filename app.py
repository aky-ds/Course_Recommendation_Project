import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title('Course Recommendation APP')
books=pickle.load(open('pkl files/books.pkl','rb'))
similarity=pickle.load(open('pkl files/similarity.pkl','rb'))
def recommend(book):
    book_index=books[books.course_title==book]
    index=book_index.index[0]
    book_list=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[0:6]
    recommend=[]
    for i in book_list:
        recommend.append(books.iloc[i[0]].course_title)
    return recommend

books_list=st.selectbox(
    'Please select the Course:',
    books['course_title']
)

if st.button('recommended'):
    recommdations=recommend(books_list)
    st.write(recommdations)


