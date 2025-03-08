import streamlit as st

# Sidebar Navigation
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Contact"])  # "Contact" must match exactly

# Home Page
if page == "Home":
    st.title("👋 About Me")

    # Short introduction
    st.subheader("😊 Hello! I'm Muhammad Shees")
    st.write("""
    I am a passionate individual who loves technology, coding, and exploring new things!  
    Currently, I'm learning **Python** and building amazing projects with **Streamlit**. 🚀  
    """)

    # Skills section
    st.subheader("💡 Skills & Interests")
    st.write("🔥 Python | 🎨 Web Development | 🤖 AI & ML | 🎮 Gaming")

# Contact Page (Fixed)
elif page == "Contact":  # "Contact" must match exactly as in the radio button
    st.title("📞 Contact")
    st.subheader("🤝 Get in Touch")
    st.write("📧 My Email: **shees7795@gmail.com**")
    st.write("📞phone:03333604659")





