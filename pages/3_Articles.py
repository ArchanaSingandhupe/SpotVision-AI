import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Skin Cancer",
    page_icon="♋",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_lottieurl(url: str):
    """Load an Lottie animation from a URL."""

    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return None
    return r.json()


lottie_disease = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_gkgqj2yq.json"
)

# st.title("Main Page")
st.title("Learn More")
st_lottie(lottie_disease, height=300, key="disease")
st.subheader(
    "Read articles about some common skin diseases that are usually found in people."
)

with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.header("Actinic keratosis")
        st.markdown("##")

        st.markdown(
            """
        Actinic keratoses (also called solar keratoses) are dry scaly patches of skin that have been damaged by the sun.
        The patches are not usually serious. But there's a small chance they could become skin cancer, so it's important to avoid further damage to your skin.
        Treatments for actinic keratoses include:
        - prescription creams and gels
        - freezing the patches (cryotherapy), this makes the patches turn into blisters and fall off after a few weeks
        - surgery to cut out or scrape away the patches - you will be given a local anaesthetic first, so it does not hurt
        - photodynamic therapy (PDT), where special cream is applied to the patches and a light is shone onto them to kill abnormal skin cells

        [Learn More](https://www.nhs.uk/conditions/actinic-keratoses)
        """
        )
    with cols[1]:
        st.image(
            "./images/Actinic_Keratosis.jpg",
            caption="Actinic keratoses",
            use_column_width=True,
        )

with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.image(
            "./images/basal-cell-carcinoma.jpg",
            caption="Basal cell carcinoma",
            use_column_width=True,
        )

    with cols[1]:
        st.header("Basal cell carcinoma")
        st.markdown(
            """
            Basal cell carcinoma is a type of skin cancer. Basal cell carcinoma begins in the basal cells — a type of cell within the skin that produces new skin cells as old ones die off.
            Basal cell carcinoma often appears as a slightly transparent bump on the skin, though it can take other forms. Basal cell carcinoma occurs most often on areas of the skin that are exposed to the sun, such as your head and neck.
            Most basal cell carcinomas are thought to be caused by long-term exposure to ultraviolet (UV) radiation from sunlight. Avoiding the sun and using sunscreen may help protect against basal cell carcinoma.
            Basal cell carcinoma appears as a change in the skin, such as a growth or a sore that won't heal. These changes in the skin (lesions) usually have one of the following characteristics:
            - A shiny, skin-colored bump that's translucent, meaning you can see a bit through the surface. The bump can look pearly white or pink on white skin. On brown and Black skin, the bump often looks brown or glossy black. Tiny blood vessels might be visible, though they may be difficult to see on brown and Black skin. The bump may bleed and scab over.
            - A brown, black or blue lesion — or a lesion with dark spots — with a slightly raised, translucent border.
            - A flat, scaly patch with a raised edge. Over time, these patches can grow quite large.
            - A white, waxy, scar-like lesion without a clearly defined border.

            To reduce your risk of basal cell carcinoma you can:
            - Avoid the sun during the middle of the day
            - Wear sunscreen year-round
            - Wear protective clothing
            - Avoid tanning beds
            - Check your skin regularly and report changes to your doctor

            [Learn More](https://www.mayoclinic.org/diseases-conditions/basal-cell-carcinoma/symptoms-causes/syc-20354187#:~:text=on%20brown%20skin-,Basal%20cell%20carcinoma%20is%20a%20type%20of%20skin%20cancer%20that,a%20type%20of%20skin%20cancer.)
            """
        )

with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.header("Dermatofibroma")
        st.markdown(
            """
            Dermatofibromas are harmless growths within the skin that usually have a small diameter. They can vary in color but are typically pink to light brown in light skin and dark brown or black in dark skin. They may appear more pink or darker if a person accidentally irritates them — for example, when shaving.
            As they are dense and firm to the touch, many people say that they feel like a small stone underneath or raised above the skin. Most dermatofibromas are painless, but some people experience itching, irritation, or tenderness at the site of the growth.
            Some doctors or medical researchers may referTrusted Source to dermatofibromas as benign fibrous histiocytomas.
            Key markers of a dermatofibroma are:
            - Appearance: A dermatofibroma presents as a round bump that is mostly under the skin.
            - Size: The normal range is about 0.5–1.5 centimeters (cm), with most lesions being 0.7–1.0 cm in diameter. The size will usually remain stable.
            - Color: The growths vary in color among individuals but will generally be pink, red, gray, brown, or black.
            - Location: Dermatofibromas are most common on the legs, but they sometimes appear on the arms, trunk, and, less commonly, elsewhere on the body.
            - Additional symptoms: Although they are usually harmless and painless, these growths may occasionally be itchy, tender, painful, or inflamed.

            [Learn More](https://www.medicalnewstoday.com/articles/318870#treatment)
            """
        )
    with cols[1]:
        st.image(
            "./images/Dermatofibroma.jpg",
            caption="Dermatofibroma",
            use_column_width=True,
        )

with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.image(
            "./images/Melanoma.jpg",
            caption="Melanoma",
            use_column_width=True,
        )
    with cols[1]:
        st.header("Melanoma")
        st.markdown(
            """
            Melanoma, the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. Melanoma can also form in your eyes and, rarely, inside your body, such as in your nose or throat.
            The exact cause of all melanomas isn't clear, but exposure to ultraviolet (UV) radiation from sunlight or tanning lamps and beds increases your risk of developing melanoma. Limiting your exposure to UV radiation can help reduce your risk of melanoma.
            The risk of melanoma seems to be increasing in people under 40, especially women. Knowing the warning signs of skin cancer can help ensure that cancerous changes are detected and treated before the cancer has spread. Melanoma can be treated successfully if it is detected early.
            The first melanoma signs and symptoms often are:
            - A change in an existing mole
            - The development of a new pigmented or unusual-looking growth on your skin

            Melanoma doesn't always begin as a mole. It can also occur on otherwise normal-appearing skin.
            Hidden melanomas include:
            - Melanoma under a nail
            - Melanoma in the mouth, digestive tract, urinary tract or vagina
            - Melanoma in the eye

            Make an appointment with your doctor if you notice any skin changes that seem unusual.

            [Learn More](https://www.mayoclinic.org/diseases-conditions/melanoma/symptoms-causes/syc-20374884#:~:text=Melanoma%2C%20the%20most%20serious%20type,in%20your%20nose%20or%20throat.)
            """
        )

with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.header("Nevus")
        st.markdown(
            """
            Nevus (plural: nevi) is the medical term for a mole. Nevi are very common. Most peopleTrusted Source have between 10 and 40. Common nevi are harmless collections of colored cells. They typically appear as small brown, tan, or pink spots.
            You can be born with moles or develop them later. Moles that you're born with are known as congenital moles. However, most moles develop during childhood and adolescence. This is known as an acquired nevus. Moles can also develop later in life as a result of sun exposure.
            There are many types of nevi. Some of them are harmless and others more serious. Read on to learn about the different types and how to know whether you should get one checked out by your doctor.
            If you're unsure of what type of nevus you have, it's best to have your doctor or dermatologist take a look.
            If your nevus seems to be changing or your doctor isn't sure what it is, they might perform a skin biopsy. This is the only way to confirm or rule out skin cancer.
            There are a few ways to do this:
            - Shave biopsy. Your doctor uses a razor to shave off a sample of the top layers of your skin
            - Punch biopsy. Your doctor uses a special punch tool to remove a sample of skin that contains both the top and deeper layers of skin.
            - Excisional biopsy. Your doctor uses a scalpel to remove your entire mole and some of the other skin around it.

            [Learn More](https://www.healthline.com/health/nevus#diagnosis)
            """
        )
    with cols[1]:
        st.image(
            "./images/Nevus.jpg",
            caption="Nevus",
            use_column_width=True,
        )


with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.image(
            "./images/Seborrheic.jpg",
            caption="Seborrheic keratosis",
            use_column_width=True,
        )
    with cols[1]:
        st.header("Seborrheic keratosis")
        st.markdown(
            """
            A seborrheic keratosis (seb-o-REE-ik ker-uh-TOE-sis) is a common noncancerous (benign) skin growth. People tend to get more of them as they get older.
            Seborrheic keratoses are usually brown, black or light tan. The growths (lesions) look waxy or scaly and slightly raised. They appear gradually, usually on the face, neck, chest or back.
            Seborrheic keratoses are harmless and not contagious. They don't need treatment, but you may decide to have them removed if they become irritated by clothing or you don't like how they look.
            A seborrheic keratosis grows gradually. Signs and symptoms might include:
            - A round or oval-shaped waxy or rough bump, typically on the face, chest, a shoulder or the back
            - A flat growth or a slightly raised bump with a scaly surface, with a characteristic "pasted on" look
            - Varied size, from very small to more than 1 inch (2.5 centimeters) across
            - Varied number, ranging from a single growth to multiple growths
            - Very small growths clustered around the eyes or elsewhere on the face, sometimes called flesh moles or dermatosis papulosa nigra, common on Black or brown skin
            - Varied in color, ranging from light tan to brown or black
            - Itchiness

            [Learn More](https://www.mayoclinic.org/diseases-conditions/seborrheic-keratosis/symptoms-causes/syc-20374884)
            """
        )


with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.header("Squamous cell carcinoma")
        st.markdown(
            """
            Squamous cell carcinoma of the skin is a common form of skin cancer that develops in the squamous cells that make up the middle and outer layers of the skin.
            Squamous cell carcinoma of the skin is usually not life-threatening, though it can be aggressive. Untreated, squamous cell carcinoma of the skin can grow large or spread to other parts of your body, causing serious complications.
            Signs and symptoms of squamous cell carcinoma of the skin include:
            - A firm, red nodule
            - A flat sore with a scaly crust
            - A new sore or raised area on an old scar or ulcer
            - A rough, scaly patch on your lip that may evolve to an open sore
            - A red sore or rough patch inside your mouth
            - A red, raised patch or wartlike sore on or in the anus or on your genitals

            Make an appointment with your doctor if you have a sore or scab that doesn't heal in about two months or a flat patch of scaly skin that won't go away.

            [Learn More](https://www.mayoclinic.org/diseases-conditions/squamous-cell-carcinoma/symptoms-causes/syc-20352480)
            """
        )
    with cols[1]:
        st.image(
            "./images/Squamous.jpg",
            caption="Squamous cell carcinoma",
            use_column_width=True,
        )


with st.container(border=True):
    cols = st.columns(2)
    with cols[0]:
        st.image(
            "./images/Vascular.jpg",
            caption="Vascular lesion",
            use_column_width=True,
        )
    with cols[1]:
        st.header("Vascular lesion")
        st.markdown(
            """
            Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks. There are three major categories of vascular lesions: Hemangiomas, Vascular Malformations, and Pyogenic Granulomas. While these birthmarks can look similar at times, they each vary in terms of origin and necessary treatment.
            At SSM Health Cardinal Glennon Children’s hospital, the SLUCare Physician Group pediatric plastic surgery team is committed to creating an individualized care plan for vascular lesions that improves the physical and emotional well-being of your child.
            Vascular tumors may be benign (not cancer) or malignant (cancer) and can occur anywhere in the body. They may form on the skin, in the tissues below the skin, and/or in an organ. There are many types of vascular tumors.

            [Learn More](https://www.ssmhealth.com/cardinal-glennon/pediatric-plastic-reconstructive-surgery/hemangiomas)
            """
        )
