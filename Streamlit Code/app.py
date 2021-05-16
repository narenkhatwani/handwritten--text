#import libraries
import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import base64
import webbrowser
import pywhatkit
from PIL import Image
import io
import os
import img2pdf

st.title("Handwritten Text")
st.header("Bored of making handwritten notes?")
st.markdown("<h6 style='text-align: justify;font-size:100%;font-family:Arial,sans-serif;line-height: 1.0;'>Making handwritten documents may sound like a tiring job, especially when the text is too long. Wouldn't it be convenient if you could just type the text, and convert it to a handwritten PDF? Well, this app does just that!</h6>",unsafe_allow_html=True)
st.markdown("")

st.sidebar.title("Text-to-Handwriting")

text = st.text_input('Enter some text here')

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

if st.button("Convert to handwritten text"):
    pywhatkit.text_to_handwriting(text,rgb=[0,0,0])
    st.markdown("Here is your handwritten text -")
    st.image('./pywhatkit.png')
    st.markdown(get_binary_file_downloader_html('pywhatkit.png', 'Picture (.png)'), unsafe_allow_html=True)
    #convert to pdf
    ImgFile = Image.open("pywhatkit.png")
    # Cheaking if Image File is in 'RGBA' Mode
    if ImgFile.mode == "RGBA":
    # If in 'RGBA' Mode Convert to 'RGB' Mode
        ImgFile = ImgFile.convert("RGB")
    # Converting and Saving file in PDF format
    ImgFile.save("text.pdf","PDF")
    # Closing the Image File Object
    ImgFile.close()
    #option to download pdf file
    st.markdown(get_binary_file_downloader_html('text.pdf', 'Pdf file'), unsafe_allow_html=True)