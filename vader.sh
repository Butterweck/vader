sleep 60s
#play /home/pi/git/vader/imperial.wav
play /home/pi/git/vader/breathe.wav
while [ true ]; do
  sudo nice --10 play --buffer 1024 "| BUF_0_=1024 BUF_1_=1024 rec --buffer 1024 -d pitch -400 echos 0.8 0.88 10 0.6 band 1.5k 1k bass 20 reverb";
done
