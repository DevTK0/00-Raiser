#!/bin/bash
GAMING_INSTANCE_NAME="00-Raiser Server"
LAUNCH_TEMPLATE="lt-0947934b416180025"

ami=`aws ec2 describe-images --filters Name=name,Values="$GAMING_INSTANCE_NAME" --output text --query 'Images[*].{ID:ImageId}'`

echo "Launching new instance with AMI id: $ami"
aws ec2 run-instances \
    --launch-template LaunchTemplateId=$LAUNCH_TEMPLATE,Version=1 --image-id $ami
