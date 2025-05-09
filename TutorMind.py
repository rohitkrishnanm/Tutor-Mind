"""
TutorMind - AI-Powered Study Assistant Suite

Author: Rohit Krishnan | Business and Technology Strategist  
Website: rohitkrishnan.co.in  
GitHub: github.com/rohitkrishnanm  
LinkedIn: linkedin.com/in/rohit-krishnan-320a5375  

© 2025 Rohit Krishnan. All rights reserved.  
Unauthorized copying, use, or distribution of this software is prohibited.
"""

import streamlit as st
import runpy

def main():
    # Set page configuration
    st.set_page_config(page_title="TutorMind", layout="wide")
    st.title("Welcome to TutorMind: Your AI-Powered Study Assistant Suite")
    st.title("BY ROHIT KRISHNAN")
    st.sidebar.title("Navigation")
    st.sidebar.title("© 2025 Rohit Krishnan. All rights reserved.")

    # Sidebar navigation
    page = st.sidebar.radio("Choose an option:", 
        ["📝 Documents Summarizer", 
         "📚 Chat with Your PDFs", 
         "🔍 Resume Checker", 
         "🌐 Website Content Summarizer", 
         "🎥 YouTube Video Summarizer",
         "🧠 Plagiarism Checker",
         "🖼️ Image-to-Text Notes Generator"]
    )

    # Page routing
    if page == "📝 Documents Summarizer":
        document_summarizer()
    elif page == "📚 Chat with Your PDFs":
        chat_with_pdf()
    elif page == "🔍 Resume Checker":
        resume_checker()
    elif page == "🌐 Website Content Summarizer":
        website_summarizer()
    elif page == "🎥 YouTube Video Summarizer":
        youtube_summarizer()
    elif page == "🧠 Plagiarism Checker":
        plagiarism_checker()
    elif page == "🖼️ Image-to-Text Notes Generator":
        image_to_text_notes()

    # Footer (Dark Mode Compatible)
    st.markdown("""<hr style="margin-top: 4em; border: 1px solid #444;">""", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; font-size: 0.85em; color: #aaa; margin-top: 30px;'>
            © 2025 <strong style='color:#ccc;'>Rohit Krishnan</strong> | Business and Technology Strategist<br>
            🌐 <a href="https://rohitkrishnan.co.in" target="_blank" style="color: #9cf;">rohitkrishnan.co.in</a> |
            🐙 <a href="https://github.com/rohitkrishnanm" target="_blank" style="color: #9cf;">GitHub</a> |
            💼 <a href="https://linkedin.com/in/rohit-krishnan-320a5375" target="_blank" style="color: #9cf;">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# App launchers for each module
def document_summarizer():
    st.subheader("Document Summarizer: Prepare Notes")
    runpy.run_path('text_summarizer/app11.py')

def chat_with_pdf():
    st.subheader("Chat with Your PDFs")
    runpy.run_path('chat_with_pdf/chat_with_pdf.py')

def youtube_summarizer():
    st.subheader("YouTube Video Summarizer: Prepare Notes")
    runpy.run_path('youtube_video_summarizer/app.py')

def resume_checker():
    st.subheader("Resume ATS Matcher")
    runpy.run_path('Resume_ATS_tracker/resume_analyser.py')

def website_summarizer():
    st.subheader("Website Content Summarizer: Prepare Notes")
    runpy.run_path('website_text_summarizer/app.py')

def plagiarism_checker():
    st.subheader("Plagiarism Checker")
    runpy.run_path('plagiarism_checker/app.py')

def image_to_text_notes():
    st.subheader("Image-to-Text Notes Generator")
    runpy.run_path('image_to_text_notes/app.py')

if __name__ == "__main__":
    main()
