import PIL
import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
import os 

st.set_page_config(
    page_title="SpotVision.AI",
    page_icon="♋",
    layout="centered",
    initial_sidebar_state="expanded",
)

from tensorflow.keras import backend as K
def focal_loss(gamma=2., alpha=0.25):
    def focal_loss_fixed(y_true, y_pred):
        y_pred = K.clip(y_pred, K.epsilon(), 1 - K.epsilon())
        cross_entropy = -y_true * K.log(y_pred)
        loss = alpha * K.pow(1 - y_pred, gamma) * cross_entropy
        return K.sum(loss, axis=1)
    return focal_loss_fixed

# Load the custom loss function
custom_loss = focal_loss(gamma=2., alpha=0.25)
@st.cache_resource
def load_model():
    # model = tf.keras.models.load_model("./model/model.h5")
    model = tf.keras.models.load_model('./model/best_model_inception_v2.h5', custom_objects={'focal_loss_fixed': custom_loss})
    # model = tf.keras.models.load_model("./model/modelv1.h5")
    return model


st.title("SpotVision.AI")


# Function to preprocess the uploaded image
def preprocess_image(image_path, target_size=(100, 100)):
    # Read image using OpenCV
    image = cv2.imread(image_path)
    # Resize and normalize the image
    image = cv2.resize(image, target_size)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Define labels based on your training classes
LABELS = [
    'actinic keratosis',
    'basal cell carcinoma',
    'dermatofibroma',
    'melanoma',
    'nevus',
    'pigmented benign keratosis',
    'squamous cell carcinoma',
    'vascular lesion'
]

pic = st.file_uploader(
    label="Upload a picture",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False,
    help="Upload a picture of your skin to get a diagnosis",
)

UPLOAD_DIR = './uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

if st.button("Predict"):
    if not pic:
        st.error("Please upload an image")
    else:
        st.header("Results")
        # Save uploaded image to disk
        image_path = os.path.join(UPLOAD_DIR, 'temp.jpg')
        with open(image_path, "wb") as f:
            f.write(pic.getbuffer())
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(pic, caption=pic.name, use_column_width=True)

        with cols[1]:
            with st.spinner("Loading model..."):
                model = load_model()

            with st.spinner("Processing image..."):
                img = preprocess_image(image_path)
                # prediction = tf.nn.softmax(prediction) # Already softmax in the model

            with st.spinner("Predicting..."):
                # prediction = model.predict(img)
                # predicted_class = np.argmax(prediction)
                # score = tf.reduce_max(prediction)
                # score = tf.round(score * 100, 2)
                # prediction = prediction[0]
                disease = str(LABELS[1]).title()
                st.metric("Prediction", disease, delta_color="off")
                st.metric("Confidence", f"{2:.2f}%", delta_color="off")
                # st.info(f"The model predicts that the lesion is a **{prediction}** with a confidence of {score}%")

        st.warning(
            "This is not a medical diagnosis. Please consult a doctor for a professional diagnosis.",
            icon="⚠️",
        )
