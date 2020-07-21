sleep 60s
#play /home/pi/git/vader/imperial.wav
play /home/pi/git/vader/breathe.wav
while [ true ]; do
  sudo nice --10 play "| BUF_0_=1 BUF_1_=1 rec --buffer 512 -d pitch -350 echos 0.8 0.88 10 0.6 band 1.5k 1k bass 20 reverb";
done
