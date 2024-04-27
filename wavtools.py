import os.path
from pydub import AudioSegment
from scipy.io import wavfile
import numpy as np

#check file extension
#incase they didn't read my instructions I worked hard on
def checkType(file):
    fileExtension = os.path.splitext(file)[1]
    if fileExtension == ".WAV":
        return
    elif fileExtension == ".mp3":
        t = AudioSegment.from_mp3(file)
        t.export(file, format='wav')
        print(t)
        return
    elif fileExtension == ".aac":
        t = AudioSegment.from_file(file, format='aac') #needs to be changed to aac not mp3
        t.export(file, format='wav')
        print(t)
        return
    else:
        print("Wrong file type")
        return


#metadata related to the sound file
def checkMetaData(file):
    audio = AudioSegment.from_file(file)

    print("Audio Info:")
    print(f"Channels: {audio.channels}")
    print(f"Sample Width: {audio.sample_width} bytes")
    print(f"Frame Rate: {audio.frame_rate} Hz")
    print(f"Frame Width: {audio.frame_width} bytes")
    print(f"Length: {len(audio)} milliseconds")
    return len(audio)


#converts to monophonic
def checkStereo(file):
    raw_audio = AudioSegment.from_file(file, format="wav")
    mono_audio = raw_audio.set_channels(1)
    mono_audio.export(file, format="wav")


#array for waveform plot
def makeWavArray(file_path):
    data = wavfile.read(file_path)
    data = np.array(data[1], dtype=np.float32)
    normalized_data = data / np.max(np.abs(data), axis=0)
    return normalized_data

