import streamlit as st
from yt_an import youtube_agent

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)

st.title("🤖 AI Youtube Video Analyzer")

#
def get_agent():
    return youtube_agent()


agent = get_agent()


video_url = st.text_input("Enter Youtube Video Link")  
button = st.button("Analyze Video") 

if video_url and button:
    with st.spinner("Analyzing video...."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)