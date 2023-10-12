from pydub import AudioSegment

# Load the audio from out1.wav and out2.wav
audio1 = AudioSegment.from_file("C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/out.wav")
audio2 = AudioSegment.from_file("C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/out2.wav")

# Ensure both audio tracks have the same number of channels and sample rate
audio1 = audio1.set_channels(2)
audio2 = audio2.set_channels(2)
audio2 = audio2.set_frame_rate(audio1.frame_rate)

# Boost the volume of the microphone audio (audio2) to match the speaker audio level
amplification_factor = 10.0
amplified_audio2 = audio2.apply_gain(amplification_factor)

# Overlap (mix) the amplified microphone audio with the speaker audio
overlapped_audio = audio1.overlay(amplified_audio2)

# Export the overlapped audio to out.wav
overlapped_audio.export("combine_out.wav", format="wav")
