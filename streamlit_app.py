import requests;

import streamlit as st;
import pandas as pd;

import snowflake.connector as cnx;

st.title("Mel and Igor's very healthy diner!");

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

st.header("Fruityvice Fruit Advice!");
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi');
st.write('The user entered ', fruit_choice);
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice);
# format the response json into a pandas dataframe
fruityvice_normalized = pd.json_normalize(fruityvice_response.json());
# and display the pandas dataframe using streamlit  
st.dataframe(fruityvice_normalized);

my_cnx = cnx.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
