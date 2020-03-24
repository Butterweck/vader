# Prerequisites

make user pi autologin

configure wifi

sudo apt -get install 

mkdir /home/pi/git

cd /home/pi/git

git clone https://www.github.com/Butterweck/vader.git

sudo apt-get install python2-numpy

sudo apt-get install python2-scipy

sudo apt-get install python2-pyaudio

sudo apt-get install alsa-utils

sudo apt-get install alsa-tools

sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev

Find cards with: cat /proc/asound/cards and use them as device index in vader.py

configure autostart for vader.py
* cd /home/pi/git/vader; python3 vader.py