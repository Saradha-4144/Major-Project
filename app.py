import joblib
import streamlit as st
model = joblib.load('sentiment_analysis')
st.title('Sentiment Classifier')
ip = st.text_input('Enter your message : ')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
