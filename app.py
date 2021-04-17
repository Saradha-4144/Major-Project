import joblib
import streamlit as st
model = joblib.load('review_sentiment_analysis')
st.title('Review Analysis')
ip = st.text_input('Enter your review : ')
op = model.predict([ip])
if st.button('Analyse'):
  st.title(op[0])
