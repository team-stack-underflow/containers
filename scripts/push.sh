#!/bin/bash
AWS_ID=878159486267
for IMAGE_NAME in $(cat ../image-names.txt)
do
    REPO=$IMAGE_NAME
    REPO_FULL=runnable/$REPO
    sudo docker tag $REPO $AWS_ID.dkr.ecr.us-east-1.amazonaws.com/$REPO_FULL
    sudo docker push $AWS_ID.dkr.ecr.us-east-1.amazonaws.com/$REPO_FULL
done
