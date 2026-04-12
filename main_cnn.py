import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

st.set_page_config(
    page_title="AI vs Real Image Detector",
    page_icon="..",
    layout="centered"
)

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model/best_model.keras")
    return model

model = load_model()

IMG_HEIGHT = 128
IMG_WIDTH  = 128

def predict_image(image: Image.Image):
    img = image.convert("RGB").resize((IMG_WIDTH, IMG_HEIGHT))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array, verbose=0)[0][0]
    label      = "Real Image" if prediction > 0.5 else "AI-Generated (Fake)"
    confidence = float(prediction) if prediction > 0.5 else float(1 - prediction)
    return label, confidence, float(prediction)

st.title("AI vs Real Image Detector")
st.markdown("Upload an image to find out whether it is a **real** or **AI-generated**.")
st.divider()

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, width="stretch")

    with col2:
        st.subheader("Prediction Result")
        with st.spinner("Analysing image ..."):
            label, confidence, raw_score = predict_image(image)

        if "Real" in label:
            st.success(f"✅ {label}")
        else:
            st.error(f"🤖 {label}")

        st.metric("Confidence", f"{confidence:.2%}")

        st.progress(confidence)

        st.divider()
