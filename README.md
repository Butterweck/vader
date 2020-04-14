# Prerequisites

make user pi autologin

configure wifi

sudo apt-get install git

mkdir /home/pi/git

cd /home/pi/git

git clone https://www.github.com/Butterweck/vader.git

sudo cp /home/pi/git/vader/sample_.asoundrc /etc/asound.conf #check hardware cards with aplay -l and arecord -l

sudo apt-get install sox

alsamixer #check volume levels of in and output

crontab -e: @reboot sh /home/pi/git/vader/vader.sh > /home/pi/vader.log 2>&1
crontab -e: @reboot sh /home/pi/git/vader/breathe.sh > /home/pi/breathe.log 2>&1

sudo nano /boot/config.txt #add force_turbo=1
