import whisper
import subprocess
from loading import simulate_loading
from pydub import AudioSegment

subprocess.run(["python", "capture.py"])

model = whisper.load_model("base")

# Load the long audio file
long_audio_file = "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/out.wav"

# Split the audio file into segments
segment_duration = 30 * 1000  # Length of each segment in milliseconds
audio = AudioSegment.from_mp3(long_audio_file)
audio_segments = [audio[i:i + segment_duration] for i in range(0, len(audio), segment_duration)]

recognized_texts = []


def process_segment(segment):

    segment.export("temp_segment.wav", format="wav")

    audio_segment = whisper.load_audio("temp_segment.wav")
    audio_segment = whisper.pad_or_trim(audio_segment)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio_segment).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")

    # Decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    return result.text


# Process each segment
for i, segment in enumerate(audio_segments):
    recognized_text = process_segment(segment)
    recognized_texts.append(recognized_text)

    # Save the recognized text for each segment to a separate file
    with open(f"master_text_segment_{i}.txt", "w", encoding="utf-8") as master_text_file:
        master_text_file.write(recognized_text)

# Combine all recognized texts into a single text file
with open("combined_text.txt", "w", encoding="utf-8") as combined_file:
    combined_file.write("\n".join(recognized_texts))

try:
    simulate_loading()
except Exception as e:
    pass

subprocess.run(["python", "summarize.py"])
subprocess.run(["python", "summarize2.py"])

try:
    simulate_loading()
except Exception as e:
    pass
subprocess.run(["python", "mail.py"])

#subprocess.run(["python", "summarize3.py"])  # using GPT-2 model
