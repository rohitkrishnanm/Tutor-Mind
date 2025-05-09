import streamlit as st
import PyPDF2
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Set page title and header
st.title("🧠 Plagiarism Checker")
st.subheader("Check originality and receive rephrasing suggestions using AI")

# Load API key and model
api_key = st.secrets["GROQ_API_KEY"]
llm = ChatGroq(groq_api_key=api_key, model_name="compound-beta-mini", temperature=1.0, max_tokens=8000)

# Prompt Template
plagiarism_prompt = PromptTemplate.from_template("""
You are an AI trained to detect potential plagiarism and help with rephrasing. Analyze the following content and do the following:
1. Identify any parts that are potentially copied or repetitive.
2. Estimate a plagiarism score out of 100 (0 = fully original, 100 = completely copied).
3. Suggest rewritten versions for the copied parts to make them more original.

Text to Analyze:
{text}

Return the result as:
- Plagiarism Score
- Highlighted copied parts
- Suggestions to improve
""")

# Text input method
input_option = st.radio("Choose input method", ("📄 Upload PDF", "✍️ Paste Text"))
user_text = ""

if input_option == "📄 Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        reader = PyPDF2.PdfReader(uploaded_file)
        user_text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

elif input_option == "✍️ Paste Text":
    user_text = st.text_area("Paste the content you want to check:", height=250)

# Process
if user_text and st.button("🔍 Check for Plagiarism"):
    with st.spinner("Analyzing text..."):
        prompt = plagiarism_prompt.format(text=user_text)
        response = llm.invoke(prompt)
        report = response.content if hasattr(response, "content") else str(response)

        st.markdown("## 📝 Report")
        st.write(report)

        st.download_button("📥 Download Report", data=report, file_name="plagiarism_report.txt")
        st.success("Report generated successfully!")