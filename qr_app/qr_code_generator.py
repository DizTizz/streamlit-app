import streamlit as st
import segno
import time

def generator():
    st.header('QR-Code Generator')

    url = st.text_input("Please write a url that you'd like to make a QR from")
    dark_colour = st.color_picker("Pick a colour for the dark squares", "#8569a8")
    generate_button = st.button('Click here to generate')

    if generate_button and url:
        with st.spinner('Generating QR-Code'):
            time.sleep(1.5)
        qr_code = segno.make(url)
        qr_code = qr_code.to_pil(scale=10, dark=dark_colour)
        qr_code.save("qr_app/images/qrcode.png")
        st.image("images/qrcode.png", width=200)