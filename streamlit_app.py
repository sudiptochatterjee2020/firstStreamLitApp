import streamlit as st;
import pandas as pd;

st.title("Mel and Igor's new healthy diner!");

st.header("\N{flexed biceps} Breakfast Menu - Champs Only \N{flexed biceps}");
st.text("\N{pot of food} Idli + Sambhar Chutney");
st.text("\N{stuffed flatbread} Poha mixed not fried!");
st.text("\N{bread} \N{leafy green} \N{egg} Roti and Subzi and Boiled egg");
st.text("\N{hot beverage} Healthy wali Chai");
st.header("\N{grapes} \N{watermelon} \N{banana} DYI Smoothie \N{mango} \N{pineapple} \N{red apple}");

#read a csv file and display it using pandas and streamlit
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
st.dataframe(my_fruit_list);
