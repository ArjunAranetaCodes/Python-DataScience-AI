#streamlit run app.py
import streamlit as st
import replicate
import time
from dotenv import load_dotenv

load_dotenv()

st.title("AI Image Generator")

prompt = st.text_input("Enter a prompt for the image:")

# Add a button to generate the image
if st.button("Generate Image"):
    with st.spinner('Generating image...'):
        start_time = time.time()
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": prompt,
                "refine": "expert_ensemble_refiner",
                "num_outputs": 1,
                "apply_watermark": False,
                "negative_prompt": "low quality, worst quality",
                "num_inference_steps": 25
            }
        )

        # Display the generated image
        st.image(output)
        end_time = time.time()
        elapsed_time = end_time - start_time
        st.write(f"Image generated in {elapsed_time:.2f} seconds")


