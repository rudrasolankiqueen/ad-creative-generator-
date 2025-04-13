streamlit
openai 
import streamlit as st
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title
st.set_page_config(page_title="AI Ad Creative Generator", layout="centered")
st.title("AI Ad Creative Generator")
st.caption("Create platform-optimized ad creatives with the power of AI")

# Form inputs
with st.form("ad_form"):
    st.subheader("Enter Campaign Details")
    brand = st.text_input("Brand Name", "EcoRun")
    industry = st.text_input("Industry Sector", "Fitness / Sportswear")
    goal = st.selectbox("Campaign Objective", ["Brand Awareness", "Lead Generation", "Sales Conversion"])
    audience = st.text_area("Target Audience", "Gen Z, eco-conscious, 18–25, urban")
    style = st.text_input("Visual Style", "Bold, vibrant, eco-friendly")
    primary_color = st.text_input("Primary Color", "Neon Green")
    secondary_color = st.text_input("Secondary Color", "Black")
    submitted = st.form_submit_button("Generate Ad Creative")

if submitted:
    with st.spinner("Generating..."):
        prompt = f"""
You are a creative marketing assistant. Based on the brand and campaign info below, generate the following:

1. A catchy ad headline
2. A 2-line ad copy
3. A visual image prompt for DALL·E
4. A strong call-to-action (CTA)
5. Platform-specific ad variations (Instagram, Google Display, Email Banner)

Brand Name: {brand}
Industry Sector: {industry}
Campaign Objective: {goal}
Target Audience: {audience}
Visual Style: {style}
Primary Color: {primary_color}
Secondary Color: {secondary_color}
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful AI marketing assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            output = response['choices'][0]['message']['content']
            st.success("Ad creative generated successfully!")
            st.markdown("### Output:")
            st.markdown(output)

        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Built with Streamlit + OpenAI")
