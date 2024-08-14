#!/bin/sh
sudo chmod u+x $1
sed -i "N;N;N;N;N;N;N;N;N;N;N;N;s/\n/ /g" "$1"
