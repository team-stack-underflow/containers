#!/bin/bash
for IMAGE_NAME in $(cat ../image-names.txt)
do
    REPO_FULL=runnable/$IMAGE_NAME
    aws ecr create-repository --repository-name $REPO_FULL --image-scanning-configuration scanOnPush=false --region us-east-1
done
