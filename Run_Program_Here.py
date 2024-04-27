import tkinter as tk
import os
import wavtools
import graph
import numpy as np
import matplotlib.pyplot as plt

from tkinter import ttk
from tkinter.filedialog import askopenfile
from pydub import AudioSegment
from wavtools import checkType
from wavtools import checkStereo
from wavtools import checkMetaData
from wavtools import makeWavArray
from graph import plotSpectogram
from graph import plotWaveform
from graph import plotrt60
from scipy.io import wavfile

#basis for file selection
#file path must be global for use in other funcs
file_path = None
def getFile():
    file = askopenfile(mode='r')
    if file:
        global file_path
        file_path = file.name
        file_name = os.path.basename(file_path)
        fileDisplay.insert(tk.END, file_name)
        checkType(file_path)
        checkStereo(file_path)
        length = checkMetaData(file_path)
        lengthSec = length / 1000

        fileDisplay.insert(tk.END, f"File length: {lengthSec} seconds")

        wavArray = makeWavArray(file_path)
        plotWaveform(length, wavArray)

        rt1, max1, test1 = plotrt60(file_path, 250, "Low Frequency")
        rt2, max2, test2 = plotrt60(file_path, 1000, "Mid Frequency")
        rt3, max3, test3 = plotrt60(file_path, 10000, "High Frequency")

        rt1 = abs(rt1)
        rt2 = abs(rt2)
        rt3 = abs(rt3)
        rtdif = (rt1 + rt2 + rt3) / 3
        rtdif -= 0.5
        fileDisplay.insert(tk.END, f"RT60 Difference: {rtdif:.3f} seconds")
        fileDisplay.insert(tk.END, f"Low Frequency RT60: {rt1:.3f} seconds")
        fileDisplay.insert(tk.END, f"Maximum Frequency: {max(max1, max2, max3):.3f} kHz")
        fileDisplay.insert(tk.END, f"High Frequency RT60: {rt3:.3f} seconds")
        fileDisplay.insert(tk.END, f"Mid Frequency RT60: {rt2:.3f} seconds")

        sample_rate, data = wavfile.read(file_path)
        frequencies, spectrum = compute_frequency_spectrum(data, sample_rate)

        # Plot the frequency spectrum
        plot_frequency_spectrum(frequencies, spectrum)
        #plot phase diagram
        plotPhase(file_path)

        file.close()
        #opens up file details page in gui
        showFileDetailsPage()

def plotPhase(file_path):
    try:
        # Read audio file
        sample_rate, data = wavfile.read(file_path)

        # Compute FFT of audio data
        fft_result = np.fft.fft(data)

        # Calculate phase
        phase = np.angle(fft_result)

        # time vector
        time_vector = np.arange(len(data)) / sample_rate

        # Plot phase
        plt.figure(figsize=(8, 6))
        plt.plot(time_vector, phase, color='pink')
        plt.title('Phase Plot of Audio Signal')
        plt.xlabel('Time (s)')
        plt.ylabel('Phase (radians)')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error plotting phase: {e}")

def compute_frequency_spectrum(data, sample_rate):
    # Compute the FFT
    fft_result = np.fft.fft(data)
    magnitude_spectrum = np.abs(fft_result)
    frequencies = np.fft.fftfreq(len(data), 1 / sample_rate)

    return frequencies[:len(frequencies)//2], magnitude_spectrum[:len(magnitude_spectrum)//2]

def plot_frequency_spectrum(frequencies, spectrum):
    plt.figure()
    plt.plot(frequencies, spectrum)
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()



def displayStats():
    if file_path:
        audio = AudioSegment.from_file(file_path)
        fileDisplay.insert(tk.END, f"Frame Rate: {audio.frame_rate} Hz")
        fileDisplay.insert(tk.END, f"Channels: {audio.channels}")
        fileDisplay.insert(tk.END, f"Sample Width: {audio.sample_width} bytes")
        fileDisplay.insert(tk.END, f"Frame Width: {audio.frame_width} bytes")

        plotSpectogram(file_path)

def showFileDetailsPage():
    # Hide the main page and show the file details page
    mainPage.pack_forget()
    fileDetailsPage.pack()

#defining fonts for the vibe
custom_font1 = ('Helvetica', 15, 'bold')
custom_font2 = ('Helvetica', 12)
custom_font3 = ('Helvetica', 15)
custom_font4 = ('Helvetica', 12, 'bold')

def createMainPage(root):
    # Create the main page
    label = tk.Label(root, text="CS Problem Solving and Solutions Final", font=custom_font1)
    label.pack(pady=20)

    label2 = tk.Label(root, text="Section 1", font=custom_font2)
    label2.pack(pady=5)

    label3 = tk.Label(root, text="Group 2", font=custom_font2)
    label3.pack(pady=5)

    label4 = tk.Label(root, text="Please select a file of the .WAV format", font= custom_font2)
    label4.pack(pady=30)
    # Create a button to select a file
    #make the button pink :)
    button_select_file = tk.Button(root, text='Select File', font=custom_font3, bg="#ff3399", command=getFile)
    button_select_file.pack(pady=10)


def createFileDetailsPage(root):
    # Create the file details page
    label = tk.Label(root, text="File Details", font= custom_font2)
    label.pack(pady=10)

    #listbox to display file details
    global fileDisplay
    fileDisplay = tk.Listbox(root, height=8, width=90)
    fileDisplay.pack(pady=10)

    # button to go back to the main page
    #it's also pink :)
    button_back_to_main = tk.Button(root, text='Back to Main Page', bg="#ff3399", command=showMainPage)
    button_back_to_main.pack(pady=20)



def showMainPage():
    # Hide the file details page and show the main page
    fileDetailsPage.pack_forget()
    mainPage.pack()


# GUI setup
root = tk.Tk()
root.geometry('700x400')
root.title('Sound Graphing Program')

# Create main and file details frames
global mainPage, fileDetailsPage
mainPage = tk.Frame(root)
fileDetailsPage = tk.Frame(root)

# Create pages
createMainPage(mainPage)
createFileDetailsPage(fileDetailsPage)

# Show the main page initially
mainPage.pack()

# Start the main event loop
root.mainloop()