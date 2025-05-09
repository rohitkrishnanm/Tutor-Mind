import os
import streamlit as st
import io
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load API Key from secrets
groq_api_key = st.secrets["GROQ_API_KEY"]

# Initialize LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0.5
)

st.title("📄 PDF SmartNotes")
st.subheader("Upload your PDFs and get summarized, exam-ready notes instantly")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)
submit = st.button("📝 Generate Notes")

if uploaded_files and submit:
    with st.spinner("Summarizing, please wait..."):
        documents = []
        for uploaded_file in uploaded_files:
            temp_path = f"./temp_{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getvalue())

            loader = PyPDFLoader(temp_path)
            docs = loader.load()
            documents.extend(docs)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
        splits = text_splitter.split_documents(documents)

        map_prompt_template = PromptTemplate(
            input_variables=["text"],
            template="""
            Please summarize the below text:
            Text: "{text}"
            Summary:
            """
        )

        final_prompt_template = PromptTemplate(
            input_variables=["text"],
            template="""
            Provide comprehensive and detailed notes based on the given documents, focusing on key concepts, explanations, and examples. The notes should help college students not only understand the topics thoroughly but also prepare effectively for their exams. Ensure the content is organized, with clear headings, subheadings, bullet points, and concise explanations where necessary.
            Documents: {text}
            """
        )

        summary_chain = load_summarize_chain(
            llm=llm,
            chain_type="map_reduce",
            map_prompt=map_prompt_template,
            combine_prompt=final_prompt_template,
            verbose=True
        )

        output = summary_chain.run(splits)

        st.markdown("## 🧠 Smart Notes")
        st.markdown(output)

        st.download_button(
            label="📥 Download Notes",
            data=output,
            file_name="smart_notes.txt",
            mime="text/plain"
        )
