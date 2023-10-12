from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

# Input and output files
input_file = "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/combined_text.txt"
output_file = "summary.txt"

with open(input_file, "r") as file:
    content = file.read()

# Tokenize the content into words and sentences
sentences = sent_tokenize(content)
words = word_tokenize(content)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Calculate word frequencies
word_freq = FreqDist(filtered_words)

# Sort sentences by the sum of their words frequencies
ranked_sentences = sorted(sentences, key=lambda sentence: sum(word_freq[word] for word in word_tokenize(sentence)), reverse=True)

# Creating a summary with the top N sentences
summary = ranked_sentences[:3]  # adjust the number of sentences

# Detokenize the summary
summary = TreebankWordDetokenizer().detokenize(summary)

# Save the summary to the output file
with open(output_file, "w") as file:
    file.write(summary)
print("Summary has been saved to", output_file)
