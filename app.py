import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs
from fpdf import FPDF
import markdown

load_dotenv()
GENAI_API_KEY = os.getenv("GOOGLE_API_KEY")

# For Streamlit Cloud
if not GENAI_API_KEY:
    GENAI_API_KEY = st.secrets["GOOGLE_API_KEY"]  

if not GENAI_API_KEY:
    st.error("Google API Key is missing! Please set it in Streamlit Secrets.")
else:
    st.success("Google API Key loaded successfully!")

genai.configure(api_key=GENAI_API_KEY)


def get_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if "youtube.com" in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [None])[0]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    return None


def extract_transcript_details(video_id):
    try:
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([i["text"] for i in transcript_text])
    except Exception as e:
        return f"Error: {str(e)}"


def generate_gemini_content(transcript_text, summary_type):
    summary_prompts = {
        "Short": "Summarize the transcript in 100 words:",
        "Medium": "Summarize the transcript in 250 words:",
        "Detailed": "Summarize the transcript in detailed bullet points within 500 words:",
    }
    prompt = summary_prompts.get(summary_type, summary_prompts["Medium"])
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


def save_as_pdf(summary, filename="summary.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.output(filename)
    return filename


def save_as_markdown(summary, filename="summary.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown.markdown(summary))
    return filename


# Streamlit app
st.title("📺 YouTube Video Summarizer")
youtube_link = st.text_input("Enter YouTube Video Link:")
summary_type = st.selectbox("Select Summary Type:", ["Short", "Medium", "Detailed"])


if youtube_link:
    video_id = get_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
    else:
        st.error("Invalid YouTube URL. Please enter a valid video link.")


if st.button("Get Summary"):
    if not youtube_link:
        st.error("Please enter a YouTube video link.")
   
    elif not video_id:
        st.error("Could not extract video ID. Please check the link format.")
   
    else:
        with st.spinner("Extracting transcript and generating summary..."):
            transcript_text = extract_transcript_details(video_id)
   
            if transcript_text.startswith("Error"):
                st.error(transcript_text)
   
            elif "No transcripts" in transcript_text:
                st.error("No transcript available for this video!")
   
            else:
                summary = generate_gemini_content(transcript_text, summary_type)
                st.markdown("## 📄 Generated Summary:")
                st.write(summary)
                st.success("Summary generated successfully!")
                
                pdf_file = save_as_pdf(summary)
                md_file = save_as_markdown(summary)
                
                with open(pdf_file, "rb") as pdf:
                    st.download_button("📥 Download as PDF", pdf, file_name="summary.pdf", mime="application/pdf")
                with open(md_file, "r", encoding="utf-8") as md:
                    st.download_button("📥 Download as Markdown", md, file_name="summary.md", mime="text/markdown")
