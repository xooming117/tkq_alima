#!/bin/sh
export DISPLAY=:1
Xvfb $DISPLAY -ac -screen 0 1280x1024x8 &
sleep 1
ps -aux
tail -f start.sh #测试用，为了阻塞住容器内的进程