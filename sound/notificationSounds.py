"""
Created on Mon Nov 19 15:17:34 2018

@author: George Manakanatas

Play audio file or beep from speeker to signal that the script is finished.
"""

# import winsound
import pyaudio
import wave
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# alternative to just beep
class play_audio_file:
    #
    chunk = 1024*1024
    #
    def __init__(self, file):
        """ Init audio stream """
        print(file)
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """
        self.stream.close()
        self.p.terminate()

#  # simple beep for windows
# class MakeBeep:
#     #frequency = 1500  # Frequency in Hertz
#     #duration = 2000  # Duration in ms
#     def __init__(self, frequency, duration):
#             try:
#                 winsound.Beep(frequency, duration)
#             except RuntimeError:
#                 print("The system is not able to beep the speaker")
#             except ImportError:
#                 print("Can't import winsound module")
