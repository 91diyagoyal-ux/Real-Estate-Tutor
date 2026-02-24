import streamlit as st
import pandas as pd
import google.generativeai as genai
from vector_db import search_property

# ==========================
# CONFIGURE GEMINI
# ==========================

genai.configure(api_key="API KEY Here")
model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("Housing.csv")
df = df.dropna()

# ==========================
# GENERATE QUESTION
# ==========================

def generate_question():
    # Retrieve similar property
    property_data = search_property("affordable family home")

    property_text = property_data.iloc[0].to_dict()

    prompt = f"""
    You are a real estate quiz generator.

    Use this real property data:

    {property_text}

    Generate ONE analytical question based on this data.
    """

    response = model.generate_content(prompt)
    return response.text

# ==========================
# EVALUATE ANSWER
# ==========================

def evaluate_answer(question_block, user_answer):
    prompt = f"""
    You are a real estate tutor.

    Here is the property and question:
    {question_block}

    Student Answer:
    {user_answer}

    Evaluate strictly.

    Give:
    - Score out of 10
    - Correct solution
    - Explanation
    """

    response = model.generate_content(prompt)
    return response.text

def generate_question():
    prompt = """
    You are a real estate quiz generator.

    Generate:
    1. A realistic property listing with:
       - Price (in INR)
       - Area (in sqft)
       - Bedrooms
       - Bathrooms
       - Stories
       - Main Road Access (yes/no)
       - Air Conditioning (yes/no)
       - Parking Spaces
       - Preferred Area (yes/no)
       - Furnishing Status

    2. Ask ONE analytical question based on the property.
       (Example: calculate price per sqft OR evaluate pricing)

    Format clearly:

    Property Details:
    ...

    Question:
    ...
    """

    response = model.generate_content(prompt)
    return response.text

# ==========================
# STREAMLIT UI
# ==========================

# -----------------------------
# SESSION STATE
# -----------------------------
if "current_property" not in st.session_state:
    st.session_state.current_property = None

if "evaluation_done" not in st.session_state:
    st.session_state.evaluation_done = False

if "last_result" not in st.session_state:
    st.session_state.last_result = None


st.title("🏠 AI-Powered Real Estate Quiz")

# -----------------------------
# GENERATE QUESTION
# -----------------------------
if st.button("Generate New Question"):

    st.session_state.current_property = generate_question()
    st.session_state.evaluation_done = False
    st.session_state.last_result = None
    st.rerun()


# -----------------------------
# DISPLAY PROPERTY + QUESTION
# -----------------------------
if st.session_state.current_property:

    st.markdown("### 🏡 Property & Question")
    st.write(st.session_state.current_property)

    user_answer = st.text_area("Your Answer")

    if not st.session_state.evaluation_done:
        if st.button("Submit Answer"):

            if user_answer.strip() == "":
                st.warning("Please enter your answer.")
            else:
                result = evaluate_answer(
                    st.session_state.current_property,
                    user_answer
                )

                st.session_state.last_result = result
                st.session_state.evaluation_done = True
                st.rerun()

    if st.session_state.evaluation_done:
        st.markdown("### 📊 Evaluation")

        st.write(st.session_state.last_result)
