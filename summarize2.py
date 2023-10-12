import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
import string


# Input and output files
input_file = "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/combined_text.txt"
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize the text into sentences and words
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Remove punctuation and convert words to lowercase
table = str.maketrans("", "", string.punctuation)
cleaned_words = [word.lower() for word in words if word.isalpha()]

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in cleaned_words if word not in stop_words]

# Create a frequency distribution of words
fdist = FreqDist(filtered_words)

# Extract the most frequent words
top_words = [word for word, _ in fdist.most_common(10)]  # You can adjust the number of words to extract

# Combine the top words into a summary
summary = " ".join(top_words)

# Save the summary as meeting minutes
minutes_file = "meeting_minutes.txt"
with open(minutes_file, "w", encoding="utf-8") as file:
    file.write("Meeting Minutes\n")
    file.write("=" * 30 + "\n")
    file.write(f"Summary: {summary}\n")
    file.write("=" * 30 + "\n")
    file.write("Full Text:\n")
    file.write(text)

print(f"Meeting minutes saved to {minutes_file}")
