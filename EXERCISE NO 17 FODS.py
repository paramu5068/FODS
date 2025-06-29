import pandas as pd
import re
import string
import nltk
from collections import Counter
import matplotlib.pyplot as plt

# Download stopwords if not already present
nltk.download('stopwords')
from nltk.corpus import stopwords

# Step 1: Load the dataset
df = pd.read_csv("data.csv")  # Ensure data.csv has a 'feedback' column

# Step 2: Preprocess text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # Tokenize and remove stopwords
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    return words

# Combine and preprocess all feedback
all_feedback = df['feedback'].dropna().astype(str).apply(preprocess_text)
all_words = [word for feedback in all_feedback for word in feedback]

# Step 3: Calculate frequency distribution
word_freq = Counter(all_words)

# Step 4: Get user input for N
N = int(input("Enter the number of top frequent words to display: "))
top_words = word_freq.most_common(N)

# Step 5: Display top N words and frequencies
print(f"\nTop {N} most frequent words:\n")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Step 6: Plot bar graph
words, freqs = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, freqs, color='skyblue')
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top {N} Most Frequent Words in Customer Feedback")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
