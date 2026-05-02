import streamlit as st
import fitz  # PyMuPDF
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# Load model
model_path = "resume_classifier_model"

tokenizer = DistilBertTokenizerFast.from_pretrained(model_path)
model = DistilBertForSequenceClassification.from_pretrained(model_path)

labels = {
    0: "Data Analyst",
    1: "ML Engineer",
    2: "UI/UX Designer",
    3: "Web Developer"
}

skills_db = {
    "Data Analyst": ["SQL", "Excel", "Power BI", "Tableau", "Python"],
    "ML Engineer": ["Python", "TensorFlow", "PyTorch", "NLP", "Docker"],
    "UI/UX Designer": ["Figma", "Adobe XD", "Wireframing", "Prototyping"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
}

jobs_db = {
    "Data Analyst": ["Junior Data Analyst", "BI Analyst", "Reporting Analyst"],
    "ML Engineer": ["ML Engineer", "AI Intern", "NLP Engineer"],
    "UI/UX Designer": ["UI Designer", "UX Researcher", "Product Designer"],
    "Web Developer": ["Frontend Developer", "Backend Developer", "Full Stack Developer"]
}

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def predict_role(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    pred = torch.argmax(outputs.logits, dim=1).item()
    return labels[pred]

def missing_skills(role, text):
    text = text.lower()
    missing = []

    for skill in skills_db[role]:
        if skill.lower() not in text:
            missing.append(skill)

    return missing

# UI
st.title("Smart Resume Classifier")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)

    role = predict_role(text)

    st.success(f"Predicted Role: {role}")

    st.subheader("Recommended Jobs")
    for job in jobs_db[role]:
        st.write("-", job)

    st.subheader("Missing Skills")
    for skill in missing_skills(role, text):
        st.write("-", skill)