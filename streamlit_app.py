import requests;

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
# Set the fruit name as the index
my_fruit_list = my_fruit_list.set_index('Fruit');
# Add a multiselect widget, have some fruits pre-selected for the user. The user can change them.
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Banana", "Kiwifruit"]);
# filter the pandas dataframe and only display to the user the selected fruits 
st.dataframe(my_fruit_list.loc[fruits_selected]); 

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
