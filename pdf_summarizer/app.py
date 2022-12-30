import streamlit as st
from transformers import pipeline

file_link: str = st.text_area("Put the PDF url here")
pipe = pipeline("summarization") #import a specific, lightweight model. 

def url_checker(file_link) -> bool:
    pdf_substring = ".pdf" or "/pdf"
    if pdf_substring not in file_link:
        st.write("Incorrect file type detected. Please link to pdfs only - file must end in .pdf")
    return True
#this is dumb with incorrect return types
url_checker(file_link)

#write a function for file ingestion and text extraction.
def text_extract(file) -> list:
    pass

user_selection_percent = st.slider(label = "What size would you like the document reduced to ?") #reword this
#def summarization_percentage(user_selection_percent):
def summmarizer(pipe, text_extract) -> list:
    for text in text_extract:
       st.write(pipe(text))
    return pipe(text)


summmarizer(pipe, text_extract)


