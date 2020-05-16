#!/bin/bash
cd ../dockerfiles
sudo docker build -t base -f base-dockerfile .
for IMAGE_NAME in $(cat ../image-names.txt)
do
    sudo docker build -t $IMAGE_NAME -f $IMAGE_NAME .
done
