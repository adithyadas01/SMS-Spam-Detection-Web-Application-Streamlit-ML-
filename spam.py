# import streamlit as st
# import pickle
# import base64

# def add_bg_image(image_file):
#     with open(image_file, "rb") as img:
#         encoded = base64.b64encode(img.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpg;base64,{encoded}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#         .main-container {{
#             background: rgba(255,255,255,0.75);
#             padding: 20px;
#             border-radius: 15px;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# add_bg_image("spam.jpg")

# @st.cache_resource
# def load_model():
#     model = pickle.load(open("Multinomial_NB", "rb"))          # your model file
#     vectorizer = pickle.load(open("CountVectorizer.pkl", "rb")) # your vectorizer
#     return model, vectorizer

# model, vectorizer = load_model()

# st.markdown('<div class="main-container">', unsafe_allow_html=True)

# st.title("📩 Spam Detection System")

# input_text = st.text_area("Enter your message:")

# if st.button("Predict"):
#     if input_text.strip() == "":
#         st.warning("Please enter a message.")
#     else:
#         transformed = vectorizer.transform([input_text])
#         prediction = model.predict(transformed)[0]

#         if prediction == 1:
#             st.error("🚨 This message is **SPAM**!")
#         else:
#             st.success("✔️ This message is **NOT SPAM**.")

# st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
import pickle
import base64

# -----------------------------------
# Background Image
# -----------------------------------
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }}

        /* Glass Card */
        .glass {{
            background: rgba(255, 255, 255, 0.22);
            border-radius: 20px;
            padding: 40px 35px;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
            margin: auto;
            width: 60%;
        }}

        .title-text {{
            text-align: center;
            font-size: 42px;
            font-weight: 700;
            color: #ffffff;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.6);
        }}

        .result-box {{
            font-size: 26px;
            padding: 18px;
            border-radius: 12px;
            font-weight: 600;
            margin-top: 10px;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_bg("spam.jpg")

# -----------------------------------
# Load Model & Vectorizer
# -----------------------------------
@st.cache_resource
def load_model():
    model = pickle.load(open("Multinomial_NB", "rb"))  # your model
    vectorizer = pickle.load(open("CountVectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# -----------------------------------
# UI Layout
# -----------------------------------
st.markdown("<h1 class='title-text'>📨 Spam Detection System</h1>", unsafe_allow_html=True)
st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.write("### 🔎 Enter a message below and check whether it's **Spam** or **Not Spam**.")

input_text = st.text_area("✉️ Your Message:", height=120)

if st.button("🔍 Predict", use_container_width=True):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        transformed = vectorizer.transform([input_text])
        prediction = model.predict(transformed)[0]

        if prediction == 1:
            st.markdown(
                "<div class='result-box' style='background:#ff4d4f;color:white;'>🚨 SPAM DETECTED!</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div class='result-box' style='background:#4CAF50;color:white;'>✔️ NOT SPAM</div>",
                unsafe_allow_html=True,
            )

st.markdown("</div>", unsafe_allow_html=True)
