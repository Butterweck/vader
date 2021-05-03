sleep 60s
play /home/pi/git/vader/sf_laser_18.mp3
while [ true ]; do
  sudo nice --10 play --buffer 1024 "| BUF_0_=1024 BUF_1_=1024 rec --buffer 1024 -d overdrive 30 pitch -100 bass 20 reverb echo 0.8 0.88 6 0.4 ";
done
