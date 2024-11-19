import streamlit as st
import requests

API_KEY = st.secrets['unsplash_api_key']
BASE_URL = 'https://api.unsplash.com/photos/random'


def get_image(query, count):
    response = requests.get(BASE_URL, params={'query': query,
                                              'count': count,
                                              'client_id': API_KEY})
    image_data = response.json()
    return image_data


st.set_page_config(page_title='Pet Maker', page_icon='🐶')
st.header('Get some animal Pictures :3', divider='rainbow')

query = st.text_input("Write the name of the Animal")
count = st.slider('How many Images would you like?', min_value=1, max_value=10, value=1)

if query:
    images = get_image(query, count)
    if images:
        for idx, image_data in enumerate(images):
            image_url = image_data['urls']['regular']
            st.image(image_url)
    else:
        st.error("No images to display.")


