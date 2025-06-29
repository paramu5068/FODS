from collections import Counter
import string

# Step 1: Read the text from the file
with open("C:/Users/nasri/OneDrive/Documents/sample_text.txt") as file:
    text = file.read()

# Step 2: Preprocess the text
text = text.lower()  # Convert to lowercase
text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
words = text.split()  # Split into words

# Step 3: Count word frequencies
word_freq = Counter(words)

# Step 4: Display the frequency distribution
print("Word Frequency Distribution:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
