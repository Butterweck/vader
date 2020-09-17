# Prerequisites

make user pi autologin

configure wifi

give the pi 16MB of gfx mem

sudo apt-get install git

mkdir /home/pi/git

cd /home/pi/git

git clone https://www.github.com/Butterweck/vader.git

sudo cp /home/pi/git/vader/sample_.asoundrc /etc/asound.conf #check hardware cards with aplay -l and arecord -l. Watch out! They might change when connecting an hdmi device.

sudo apt-get install sox

alsamixer #check volume levels of in and output

crontab -e: @reboot sh /home/pi/git/vader/performance.sh; cp /home/pi/vader.log /home/pi/vader.log.backup; sh /home/pi/git/vader/vader.sh > /home/pi/vader.log 2>&1

#Overclocking
- sudo nano /boot/config.txt
#add
- force_turbo=1
- arm_freq=1085
- gpu_freq=530
- over_voltage=2
- core_freq=515
- sdram_freq=533
- over_voltage_sdram=1
