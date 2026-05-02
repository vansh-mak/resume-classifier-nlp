#  Smart Resume Classifier & Job Recommender

An end-to-end NLP + Deep Learning project that classifies resumes into job roles and provides personalized job recommendations along with missing skill analysis.


##  Problem Statement

Recruiters spend significant time manually screening resumes. This project automates the process by:

- Classifying resumes into job roles
- Recommending relevant job positions
- Identifying missing skills for targeted roles


##  Features

-  Resume parsing from PDF
-  Role classification using fine-tuned DistilBERT
-  Multi-class prediction (4 roles)
-  Job recommendations based on predicted role
-  Missing skill detection
-  Interactive web app using Streamlit



##  Model Details

- **Model:** DistilBERT (Transformer-based)
- **Task:** Multi-class text classification
- **Classes:**
  - Data Analyst
  - ML Engineer
  - Web Developer
  - UI/UX Designer
- **Accuracy:** ~93%
- **Evaluation Metrics:** Accuracy, Weighted F1-score



##  Tech Stack

- **Language:** Python  
- **Deep Learning:** PyTorch  
- **NLP:** Hugging Face Transformers  
- **Frontend:** Streamlit  
- **Data Processing:** Pandas, NumPy  
- **PDF Parsing:** PyMuPDF  

