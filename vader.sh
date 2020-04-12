
sleep 60s
sudo nice --20 play "| BUF_0_=1 BUF_1_=1 rec --buffer 256 -d pitch -500 echos 0.8 0.88 10 0.6 band 1.5k 1k bass 20 reverb"
