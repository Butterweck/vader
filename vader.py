# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:10:10 2020

@author: sebas
"""

#imports
from pyaudio import PyAudio, paInt16, paContinue, paComplete
from time import sleep
from AudioProcessing import AudioProcessing
import numpy as np
import wave

#global vars
pa = PyAudio()
sample_rate = 44100
frames = 1024
silence_count = 0
breathe_after = 50
silence_threshold = 2

# callback method that is executed on every audio chunk recorded by the mic
# returns manipulated audio data that is played on the speakers then
def callback(in_data, frame_count, time_info, flag):
	global silence_count
	if flag:
		print("Playback Error: %i" % flag)
	
	# bytes to numpy array
	numpy_in_data = np.frombuffer(in_data, dtype=np.int16)
	
	# determine whether the current audio chunk is just silence
	if np.average(numpy_in_data) < silence_threshold and np.average(numpy_in_data) > (silence_threshold * -1):
		# increase a counter if yes
		silence_count = silence_count + 1
	else:
		# reset the counter if no
		silence_count = 0
	
	# vader effect audio manipulation
	out_data = AudioProcessing(sample_rate, numpy_in_data)
	out_data.set_audio_speed(.7)
	out_data.set_lowpass(2000)
	out_data.set_echo(0.02)
	numpy_out_data = out_data.get_audio()
	
	# numpy array to bytes
	output_binary = numpy_out_data.tobytes('C')
	
	return output_binary, paContinue

def play_a_breathe():
	# defining a stream for the breath and read the wav file
	breathe = wave.open("breathe.wav", 'rb')
	stream_breathe = pa.open(format = pa.get_format_from_width(breathe.getsampwidth()),
                channels = breathe.getnchannels(),
                rate = breathe.getframerate(),
                output = True)
	data_breathe = breathe.readframes(frames)
	
	# start stream
	stream_breathe.start_stream()
	
	# play a breathe
	while len(data_breathe) > 0:
		stream_breathe.write(data_breathe)
		data_breathe = breathe.readframes(frames)
	
	# cleanup
	stream_breathe.stop_stream()
	stream_breathe.close()
	
# defining a stream for voice processing
stream_voice = pa.open(format = paInt16,
                 channels = 1,
                 rate = sample_rate,
                 input = True,
                 output = True,
                 frames_per_buffer = frames,
                 stream_callback = callback)

# start stream
stream_voice.start_stream()

# run the stream
while stream_voice.is_active():
	sleep(0.1)
	# check whether there has been silence for a few chunks
	if silence_count > breathe_after:
		# stop the voice processing
		stream_voice.stop_stream()
		# play a vader breathe
		play_a_breathe()
		# reset the silence counter
		silence_count = 0
		# start voice processing again
		stream_voice.start_stream()

#cleanup
stream_voice.stop_stream()
stream_voice.close()
pa.terminate()

