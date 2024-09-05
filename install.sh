#! /bin/sh

sudo cp nv.py /usr/local/bin/nv.py
sudo convert -geometry 48x48 images/NTPview.png /usr/share/NTPview.xpm
sudo cp NTPview.desktop /usr/share/applications/
