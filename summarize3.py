from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import pipeline

# Load the GPT-2 model and tokenizer
model_name = "gpt2"  # You can specify other GPT-2 variants
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Input text to summarize
input_text ="C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/combined_text.txt"

# Tokenize the input text
input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)

# Generate the summary using the GPT-2 model
output = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50)

# Decode the summary from the model's output
summary = tokenizer.decode(output[0], skip_special_tokens=True)

# Save the summary as meeting minutes
minutes_file = "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/gpt_minutes.txt"
with open(minutes_file, "w", encoding="utf-8") as file:
    file.write("Meeting Minutes\n")
    file.write("=" * 30 + "\n")
    file.write("Summary:\n")
    file.write(summary)
    file.write("\n" + "=" * 30 + "\n")
    file.write("Full Text:\n")
    file.write(input_text)

print(f"Meeting minutes saved to {minutes_file}")
