sleep 60s
play /home/pi/git/vader/sf_laser_18.mp3
while [ true ]; do
  sudo nice --10 play --buffer 1024 "| BUF_0_=1024 BUF_1_=1024 rec --buffer 1024 -d overdrive 10 echo 0.8 0.8 5 0.7 echo 0.8 0.7 6 0.7 echo 0.8 0.7 10 0.7 echo 0.8 0.7 12 0.7 echo 0.8 0.88 12 0.7 echo 0.8 0.88 30 0.7 echo 0.6 0.6 60 0.7";
done
