import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('lr.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.set_page_config(page_title="Student Performance",page_icon=":student:")
st.title(":red[Student Performance Predictor]:student:")

Hours_Studied = st.number_input('Daily Study Hours')

Previous_Scores = st.slider(
    "Previous Exam Score",
    min_value=0, max_value=100,
    value=(100))

Extracurricular_Activities = st.selectbox('Involment in Extracurricular Activities ',['Yes','No'],index=None,placeholder = "Choose an option")

Sleep_Hours = st.number_input('Daily Sleep Hours')

Practice = st.number_input('Sample Practice Paper Solved',step=1)

if st.button('Predict Performance'):
    # query
    if Extracurricular_Activities == 'Yes':
        Extracurricular_Activities = 1
    else: 
        Extracurricular_Activities = 0

    query = np.array([Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Practice])

    query = query.reshape(1,5)
    st.title("The performance index of this student out of 100 is " + str(int((pipe.predict(query)[0]))))