import streamlit as st
from genrator import generate_post,generate_image


st.set_page_config(page_title="GenAI Social Media Post Generator", page_icon="📣")
st.title("📣 GenAI Social Post Generator")

social_media = ["Twitter", "Linkedin", "Instagram"]
platform = st.selectbox("Choose platform", options=social_media)
topic = st.text_input("What's the topic?")
tone = st.selectbox("Tone", ["Professional", "Funny", "Inspiring", "Casual", "Urgent"])
audience = st.text_input("Target audience (e.g. 'tech CEOs', 'fitness enthusiasts')")
language = st.selectbox("Language", ["English", "Hindi", "French", "Spanish", "German"])

if st.button("✨ Generate Post"):
    if topic and audience:
        with st.spinner("Generating post..."):
            post = generate_post(platform, topic, tone, audience, language).content
            image_url = generate_image(post)
            st.image(image_url, caption="AI-Generated Image", width=512 ,use_container_width=True)
            st.success("Here's your post:")
            st.text_area("Generated Post", post, height=200)
            st.download_button("📥 Download as .txt", post, file_name="social_post.txt")
    else:
        st.warning("Please fill in all fields.")