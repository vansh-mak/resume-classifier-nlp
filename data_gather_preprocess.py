import pandas as pd
df = pd.read_csv(r"C:\Users\ASUS\Desktop\Resume_classifier\resume_dataset\Resume\Resume.csv")

# Keep useful categories only
keep = [
    "FINANCE",
    "BANKING",
    "ACCOUNTANT",
    "BUSINESS-DEVELOPMENT",
    "INFORMATION-TECHNOLOGY",
    "ENGINEERING",
    "DESIGNER",
    "DIGITAL-MEDIA",
    "ARTS"
]

df = df[df["Category"].isin(keep)].copy()

