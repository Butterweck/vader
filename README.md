# Prerequisites

make user pi autologin

configure wifi

configure autostart for vader.py
* screen -d -m jackd -d alsa --capture hw:2 --playback hw:1 --rate 44100
* cd /home/pi/git/vader; python3 vader.py

sudo apt-get install python2-numpy

sudo apt-get install python2-scipy

sudo apt-get install python2-pyaudio

sudo apt-get install alsa-utilssudo aplay 

sudo apt-get install alsa-tools

sudo apt-get install jackd2

sudo apt-get install screen

sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

Find cards with:	cat /proc/asound/cards 

sudo nano ~/.asoundrc

pcm.!default { 
    type asym playback.pcm { type plug slave.pcm “hw:1” }
    capture.pcm { type plug slave.pcm “hw:2” }
    }