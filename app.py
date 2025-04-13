import streamlit as st
from openai import OpenAI

# Set OpenAI client using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.title("Ad Creative Generator")
st.subheader("Built with Streamlit + OpenAI")

# Empty input fields
brand = st.text_input("Brand Name", value="")
product = st.text_input("Product/Service", value="")
primary_color = st.text_input("Primary Color", value="")
secondary_color = st.text_input("Secondary Color", value="")
tone = st.selectbox("Tone", ["Friendly", "Professional", "Playful", "Bold", "Minimal"])
platform = st.selectbox("Platform", ["Instagram", "Google Ads", "LinkedIn", "Facebook", "Email"])

# Generate Ad
if st.button("Generate Ad Creative"):
    if not all([brand, product, primary_color, secondary_color, tone, platform]):
        st.warning("Please fill in all fields before generating.")
    else:
        with st.spinner("Generating your ad..."):
            prompt = (
                f"Generate a {tone.lower()} ad creative for {brand} promoting {product}. "
                f"The ad is for {platform}. Use {primary_color} as the primary color and {secondary_color} as the secondary color. "
                f"Include a catchy headline, a short body text, and a call-to-action."
            )

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a creative digital marketing assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )

                output = response.choices[0].message.content
                st.success("Ad Creative Generated:")
                st.markdown(output)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
