import streamlit as st
import replicate
import time


def remove_background():
    st.subheader("Background Remover")
    uploaded_file = st.file_uploader(label="Upload an image", type=["png", "jpg", "jpeg"], key="remove_background")

    if uploaded_file is not None:
        st.image(uploaded_file)
        if st.button("Generate Image"):
            with st.spinner('Generating image...'):
                start_time = time.time()
                input = {
                    "image": uploaded_file
                }
                output = replicate.run(
                    "cjwbw/rembg:fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003",
                    input=input
                )
                end_time = time.time()
                elapsed_time = end_time - start_time
                st.write(f"Image generated in {elapsed_time:.2f} seconds")
                st.image(output)