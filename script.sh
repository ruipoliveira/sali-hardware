#!/bin/bash

sleep 10

wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    cd ~/sali-sensor
    python3 script.py &  PIDIOS=$!

    raspivid -o - -t 0 -vf -hf -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/ux4a-v8x7-3yws-635b &  PIDMIX=$!

    wait $PIDIOS
	wait $PIDMIX

else
    echo "Offline :("
fi