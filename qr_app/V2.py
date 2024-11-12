import streamlit as st
from decode_qrcode import decode_qrcode
from qr_code_generator import generator

menu_options = ['Homepage 🏠','Generate QR-Code', 'Decode QR code', 'About me']
st.set_page_config(page_title='QR Code generator', page_icon='👾')

with st.sidebar:
    page_selection = st.selectbox('Menu', menu_options)

if page_selection == 'Generate QR-Code':
    generator()
elif page_selection == 'Decode QR code':
    decode_qrcode()
elif page_selection == 'About me':
    st.title('Hewwo OwO')
elif page_selection == 'Homepage 🏠':
    st.header('Hello, welcome to my page OwO')
    st.image('qr_app/images/main_banner.jpg')