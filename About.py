import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.set_page_config(
    page_title="SpotVision.AI",
    page_icon="♋",
    layout="wide",
    initial_sidebar_state="expanded",
)

lottie_healthy = load_lottieurl(
    "https://lottie.host/9d26c484-b36e-4b60-97bb-49b76ce151a3/wTGZmPt9UQ.json"
)
lottie_welcome = load_lottieurl(
    "https://lottie.host/4fb4b5a8-321a-4f7c-9fca-3c726f39f332/inNEpphRng.json"
)
lottie_health= load_lottieurl(
    "https://lottie.host/926b19b6-5f0b-40cf-bdd9-4cd7ccd91886/O5buMUWQ9o.json"
)

st.title("Final Year Project (B-Tech) 2023-24")
st.subheader(" Wainganga College Of Engineering And Management, Dongargoan, Nagpur ")
st.write(" Department of Electronics & Telecommunication Engineering ")


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
                Developed By:-

                1. Archana Singandhupe 
        

                Under the Guidance of Prof. Malvika Saraf """)
    with right_column:
        st_lottie(lottie_welcome, height=300, key="welcome")
# st.header("Melanoma detection at your skin images.")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            Melanoma is one of the deadliest forms of skin cancer, responsible for 75% of all skin cancer-related deaths. Early detection is critical for survival. SpotVision.Ai offers a reliable solution by identifying melanoma through skin images. We specialize in detecting various types of skin lesions.

            SpotVision.AI detects the following diseases:
            * Actinic keratosis,
            * Basal cell carcinoma,
            * Dermatofibroma,
            * Melanoma,
            * Nevus,
            * Pigmented benign keratosis,
            * Squamous cell carcinoma,
            * Vascular lesion.
            """
        )
        st.write("##")
        st.write(
            "[Learn More >](https://www.researchgate.net/publication/356093241_Characteristics_of_publicly_available_skin_cancer_image_datasets_a_systematic_review)"
        )
    with right_column:
        st_lottie(lottie_health, height=500, key="check")

with st.container():
    st.write("---")
    cols = st.columns(2)
    with cols[0]:
        st.header("How it works?")
        """
        Our cutting-edge application harnesses the power of deep learning and computer vision to analyze skin images and predict potential diseases with remarkable accuracy of 71% 
        ##
        [Learn More >](https://youtu.be/IDWixA8eeG8?si=oxa1TgBEP8VZnN-2)
        """
    with cols[1]:
        st_lottie(lottie_healthy, height=300, key="healthy")
