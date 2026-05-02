ml_samples = [
    "Python TensorFlow PyTorch Deep Learning NLP Machine Learning Pandas NumPy SQL",
    "Machine Learning Engineer with Python Scikit-learn TensorFlow Keras NLP",
    "Built predictive models using Python Pandas NumPy Scikit-learn Matplotlib",
    "Deep Learning Computer Vision OpenCV CNN TensorFlow PyTorch Python",
    "Natural Language Processing NLP Transformers BERT Python PyTorch",
    "Data Science Machine Learning Regression Classification Python SQL",
    "MLOps Docker AWS FastAPI TensorFlow Machine Learning Deployment",
]

import random

synthetic_ml = []

for _ in range(150):
    text = " ".join(random.sample(ml_samples, k=3))
    synthetic_ml.append({
        "Resume_str": text,
        "Final_Label": "ML Engineer"
    })

ml_df = pd.DataFrame(synthetic_ml)

real_df = df[["Resume_str", "Final_Label"]]

final_df = pd.concat([real_df, ml_df], ignore_index=True)

print(final_df["Final_Label"].value_counts())