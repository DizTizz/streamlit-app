import streamlit as st
import numpy as np
import cv2

def decode_qrcode():
    st.header('QR-Decoder')

    # add a file to be decoded
    qrcode = st.file_uploader('Upload a QR_Code',
                     type=['jpg', 'png', 'jpeg', 'gif'])
    decode_button = st.button('Do you want to Decode?')

    if qrcode and decode_button:
        # annoying code to convert image
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # place the converted qr code
        st.image(opencv_image)

        detector = cv2.QRCodeDetector()

        decode_info, point, straight_qr = detector.detectAndDecode(opencv_image)

        st.write(f"This is what the QR-Code contains {decode_info}")