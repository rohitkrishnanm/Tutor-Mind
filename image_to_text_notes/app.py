import streamlit as st
import pytesseract
from PIL import Image
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Page setup
st.title("🖼️ Image-to-Text Notes Generator")
st.subheader("Upload an image and generate structured notes using AI")

# Load Groq API
api_key = st.secrets["GROQ_API_KEY"]
llm = ChatGroq(groq_api_key=api_key, model_name="compound-beta", temperature=1.0, max_tokens=8000)

# Prompt template
summary_prompt = PromptTemplate.from_template("""
You are an AI assistant that helps students create summarized and structured notes from raw content.
Given the following raw extracted text from an image, generate concise and clear study notes:
- Use bullet points where appropriate
- Add headings if relevant
- Ensure clarity and readability for exam prep

Raw Extracted Text:
{text}

Return:
Well-formatted notes
""")

# Image upload
uploaded_image = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    extracted_text = pytesseract.image_to_string(image)
    st.text_area("📄 Extracted Text", extracted_text, height=200)

    if st.button("📝 Generate Notes"):
        with st.spinner("Analyzing and summarizing the content..."):
            prompt = summary_prompt.format(text=extracted_text)
            response = llm.invoke(prompt)
            notes = response.content if hasattr(response, "content") else str(response)

            st.markdown("## 🧾 Generated Notes")
            st.write(notes)

            st.download_button("📥 Download Notes", data=notes, file_name="image_notes.txt")
            st.success("Notes generated successfully!")
