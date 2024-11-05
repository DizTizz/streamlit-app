import streamlit as st
import segno

def generate_qr_code(url):
    qr_code = segno.make(url)
    qr_code.save("images/qrcode.png")


st.set_page_config(page_title='QR-Code Generator', page_icon="👾")
st.image("images/banner2.jpg", width=500)
st.title("QR-Code Generator")
url = st.text_input("Please write a url that you'd like to make a QR from")

if url:
    generate_qr_code(url)
    st.image("images/qrcode.png", width=200)