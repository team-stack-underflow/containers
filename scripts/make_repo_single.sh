#!/bin/bash
IMAGE_NAME=$1
REPO_FULL=runnable/$IMAGE_NAME
aws ecr create-repository --repository-name $REPO_FULL --image-scanning-configuration scanOnPush=false --region us-east-1
