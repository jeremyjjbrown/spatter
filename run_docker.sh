#!/bin/bash

sudo docker run \
    -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    -e S3_BUCKET_NAME=$S3_BUCKET_NAME \
    -p 80:8000 jeremyjjbrown/spatter
