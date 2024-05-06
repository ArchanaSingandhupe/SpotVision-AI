import PIL
import streamlit as st
import tensorflow as tf

st.set_page_config(
    page_title="SpotVision.AI",
    page_icon="♋",
    layout="centered",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("./model/model.h5")
    return model


st.title("SpotVision.AI")

pic = st.file_uploader(
    label="Upload a picture",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False,
    help="Upload a picture of your skin to get a diagnosis",
)

if st.button("Predict"):
    if not pic:
        st.error("Please upload an image")
    else:
        st.header("Results")

        cols = st.columns([1, 2])
        with cols[0]:
            st.image(pic, caption=pic.name, use_column_width=True)

        with cols[1]:
            labels = [
                "actinic keratosis",
                "basal cell carcinoma",
                "dermatofibroma",
                "melanoma",
                "nevus",
                "pigmented benign keratosis",
                "seborrheic keratosis",
                "squamous cell carcinoma",
                "vascular lesion",
            ]

            with st.spinner("Loading model..."):
                model = load_model()

            with st.spinner("Processing image..."):
                img = PIL.Image.open(pic)
                img = img.resize((180, 180))
                img = tf.keras.preprocessing.image.img_to_array(img)
                img = tf.expand_dims(img, axis=0)

                prediction = model.predict(img)
                prediction = tf.nn.softmax(prediction)

                score = tf.reduce_max(prediction)
                score = tf.round(score * 100, 2)

            with st.spinner("Predicting..."):
                prediction = tf.argmax(prediction, axis=1)
                prediction = prediction.numpy()
                prediction = prediction[0]

                disease = str(labels[prediction]).title()
                st.metric("Prediction", disease, delta_color="off")
                st.metric("Confidence", f"{score:.2f}%", delta_color="off")
                # st.info(f"The model predicts that the lesion is a **{prediction}** with a confidence of {score}%")

        st.warning(
            "This is not a medical diagnosis. Please consult a doctor for a professional diagnosis.",
            icon="⚠️",
        )
