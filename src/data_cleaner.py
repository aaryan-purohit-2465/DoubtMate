import pandas as pd

# 1. Load dataset
df = pd.read_csv("data/faq.csv")

# 2. Remove rows where question OR answer is empty
df = df.dropna(subset=["question", "answer"])

# 3. Remove duplicate questions (keep the first occurrence)
df = df.drop_duplicates(subset=["question"], keep="first")

# 4. Add a topic column
df["topic"] = "Python Basics"

# 5. Reset index numbers
df = df.reset_index(drop=True)

# 6. Save cleaned dataset
df.to_csv("data/faq_cleaned.csv", index=False)

print("Dataset cleaned and saved as faq_cleaned.csv")