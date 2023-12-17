#!/bin/bash

sudo apt update -y

sudo apt install python3-pip

pip3 install aiogram
pip3 install pyttsx3
pip3 install torch
pip3 install soundfile
pip3 install gTTS
pip3 install pydub


echo 'Succes!'