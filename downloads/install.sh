#!/bin/bash

mkdir main
cd main
wget -b -q https://github.com/useeryous/lolz.git

if [ $? -ne 0 ]; then
    echo "Error: Failed to download the repository."
    exit 1
fi
git clone