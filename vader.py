# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

#imports
from pyaudio import PyAudio, paFloat32, paInt16, paContinue, paComplete
from time import sleep
from AudioProcessing import AudioProcessing
import numpy as np
import io
from scipy.io.wavfile import write
import wave

#global vars
pa = PyAudio()
sample_rate = 44100
frames = 1024
silence_count = 0
breathe_after = 50
silence_threshold = 2

#methods
def callback(in_data, frame_count, time_info, flag):
	global silence_count
	if flag:
		print("Playback Error: %i" % flag)
	
	# bytes to numpy array
	numpy_in_data = np.frombuffer(in_data, dtype=np.int16)
	if np.average(numpy_in_data) < silence_threshold and np.average(numpy_in_data) > (silence_threshold * -1):
		silence_count = silence_count + 1
	else:
		silence_count = 0
	
	# audio manipulation
	out_data = AudioProcessing(sample_rate, numpy_in_data)
	out_data.set_audio_speed(.7)
	out_data.set_lowpass(2000)
	out_data.set_echo(0.02)
	numpy_out_data = out_data.get_audio()
	
	# numpy array to bytes
	output_binary = numpy_out_data.tobytes('C')
	
	return output_binary, paContinue

def play_a_breathe():
	#defining a stream for the breath
	breathe = wave.open("breathe.wav", 'rb')
	stream_breathe = pa.open(format = pa.get_format_from_width(breathe.getsampwidth()),
                channels = breathe.getnchannels(),
                rate = breathe.getframerate(),
                output = True)
	data_breathe = breathe.readframes(frames)
	
	#start stream
	stream_breathe.start_stream()
	
	#play a breathe
	while len(data_breathe) > 0:
		stream_breathe.write(data_breathe)
		data_breathe = breathe.readframes(frames)
	
	#cleanup
	stream_breathe.stop_stream()
	stream_breathe.close()
	
#defining a stream for voice processing
stream_voice = pa.open(format = paInt16,
                 channels = 1,
                 rate = sample_rate,
                 input = True,
                 output = True,
                 frames_per_buffer = frames,
                 stream_callback = callback)

#start stream
stream_voice.start_stream()

#running the streams
while stream_voice.is_active():
	sleep(0.1)
	if silence_count > breathe_after:
		stream_voice.stop_stream()
		play_a_breathe()
		silence_count = 0
		stream_voice.start_stream()

#cleanup
stream_voice.stop_stream()
stream_voice.close()
pa.terminate()

