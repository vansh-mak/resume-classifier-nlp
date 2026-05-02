import re

def classify_role(text, category):
    text = str(text).lower()

    # Direct mapping
    if category in ["FINANCE", "BANKING", "ACCOUNTANT", "BUSINESS-DEVELOPMENT"]:
        return "Data Analyst"

    if category in ["DESIGNER", "DIGITAL-MEDIA", "ARTS"]:
        return "UI/UX Designer"

    ml_keywords = [
        "python","pandas","numpy","scikit","sklearn","tensorflow",
        "keras","pytorch","machine learning","deep learning",
        "nlp","data science","opencv","jupyter"
    ]

    web_keywords = [
        "html","css","javascript","react","node","angular",
        "bootstrap","php","frontend","backend","web development"
    ]

    if category in ["INFORMATION-TECHNOLOGY", "ENGINEERING"]:

        ml_score = sum(word in text for word in ml_keywords)
        web_score = sum(word in text for word in web_keywords)

        if ml_score >= 2 and ml_score > web_score:
            return "ML Engineer"
        else:
            return "Web Developer"

    return None

df["Final_Label"] = df.apply(
    lambda x: classify_role(x["Resume_str"], x["Category"]),
    axis=1
)

print(df["Final_Label"].value_counts())