'''
Created on Mon Nov 19 15:17:34 2018

@author: George Manakanatas

Play audio file or beep from speeker to signal that the script is finished.
'''
import wave
import pyaudio
import pyttsx3
import winsound


def text_to_speech(text):
    '''
    Tryinng to get text to speech to work

    Arguments
        text(str): The text we want read

    Returns
        nothing
    '''
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# alternative to just beep
class PlayTheAudioFile:
    '''
    Alternative to windows beep.

    Arguments
        filepath(str): Path to the file we want to play
    '''
    #
    chunk = 1024*1024
    #

    def __init__(self, file):
        """ Init audio stream """
        self.wave_file = wave.open(file, 'rb')
        self.py_audio = pyaudio.PyAudio()
        self.stream = self.py_audio.open(
            format=self.py_audio.get_format_from_width(self.wave_file.getsampwidth()),
            channels=self.wave_file.getnchannels(),
            rate=self.wave_file.getframerate(),
            output=True
        )

    def play(self):
        """ Play entire file """
        data = self.wave_file.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wave_file.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """
        self.stream.close()
        self.py_audio.terminate()


class MakeBeep:
    '''
    Simple windows beep
    '''
    # frequency = 1500  # Frequency in Hertz
    # duration = 2000  # Duration in ms
    def __init__(self, frequency, duration):
        try:
            winsound.Beep(frequency, duration)
        except RuntimeError:
            print("The system is not able to beep the speaker")
        except ImportError:
            print("Can't import winsound module")
