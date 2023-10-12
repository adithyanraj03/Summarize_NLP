import soundcard as sc
import soundfile as sf
import tkinter as tk
import threading

OUTPUT_FILE_NAME = "out.wav"
SAMPLE_RATE = 48000

# Create a global variable to control recording state
recording = False
recorded_data = []
recording_thread = None

# Function to start or stop recording
def toggle_recording():
    global recording, recorded_data, recording_thread

    if not recording:
        recorded_data.clear()

        def record_audio():
            with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
                while recording:
                    data = mic.record(numframes=SAMPLE_RATE)
                    recorded_data.extend(data[:, 0])

        recording_thread = threading.Thread(target=record_audio)
        recording_thread.start()
        recording = True
        start_stop_button.config(text="Stop Recording")
    else:
        recording = False
        start_stop_button.config(text="Start Recording")
        if recording_thread:
            recording_thread.join()

# Function to save recorded data and run a subprocess
def save_recorded_data():
    global recording
    recording = False
    start_stop_button.config(text="Start Recording")
    if recorded_data:
        sf.write(file=OUTPUT_FILE_NAME, data=recorded_data, samplerate=SAMPLE_RATE)
        recorded_data.clear()
    root.quit()
def on_closing():
    if recording:
        toggle_recording()
    save_recorded_data()

# Create a GUI window
root = tk.Tk()
root.title("Audio Recorder")

root.protocol("WM_DELETE_WINDOW", on_closing)

# "Start/Stop" button
start_stop_button = tk.Button(root, text="Start Recording", command=toggle_recording)
start_stop_button.pack()

save_button = tk.Button(root, text="Save Recording and Run Subprocess", command=save_recorded_data)
save_button.pack()

root.mainloop()
