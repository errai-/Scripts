#!/bin/bash
set -e

LANG=en_US.UTF-8
LC_NUMERIC=en_US.UTF-8
TFILE=tmpstudy.html
FILE=study.html

while true; do
  clear;
  wget -O $TFILE https://www.att.hel.fi/fi/omistusasunnot/asunto-oy-helsingin-l%C3%A4rkaninpolku || true
  wait
  if [ -f $TFILE ]; then
    rm -f $FILE
    wait
    mv $TFILE $FILE
    wait
  fi
  if [ -f $FILE ]; then
    python genhelp2.py
    wait
  fi
  sleep 30;
done;
