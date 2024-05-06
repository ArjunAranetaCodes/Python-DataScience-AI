import streamlit as st
import replicate
import time


def image_to_prompt():
    st.subheader("Image to Prompt")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="image_to_prompt_upload")

    if uploaded_file is not None:
        st.image(uploaded_file)
        if st.button("Generate Prompt"):
            with st.spinner('Generating prompt...'):
                start_time = time.time()
                input = {
                    "image": uploaded_file
                }
                output = replicate.run(
                    "methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",
                    input=input
                )
                st.write(f"Prompt: {output}")
                end_time = time.time()
                elapsed_time = end_time - start_time
                st.write(f"Prompt generated in {elapsed_time:.2f} seconds")