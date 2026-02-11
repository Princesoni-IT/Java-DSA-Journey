import streamlit as st
import os
from PIL import Image
from rembg import remove


st.title ("🖼️ AI Background Remover")

upload_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="file_uploader")

if upload_file is not None:
  img = Image.open(upload_file)

  st.subheader("Original Image")

  st.image(img, use_container_width=True)

  if st.button("Remove Background"):
    with st.spinner("Processing..."):
      output = remove(img)

    st.subheader("Image with Background Removed")

    st.image(output)

