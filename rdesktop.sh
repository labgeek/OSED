#!/bin/sh
 
rdesktop 192.168.175.10 \
    -u offsec \
    -g 1596x1170 \
    -x l \
    -a 32 \
    -r clipboard:CLIPBOARD \
    -r sound:local:alsa \
    -r disk:linux=/home/kali/OSED/share
