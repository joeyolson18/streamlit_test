import streamlit
import pandas as pd

streamlit.title('MMMMMMM Food')

# BREAKFAST
streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avacado Toast')

# SMOOTHIES
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_list = pd.read_csv(
    'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruit_list = fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(
    fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = fruit_list.loc[fruits_selected]

streamlit.dataframe(fruit_list)
