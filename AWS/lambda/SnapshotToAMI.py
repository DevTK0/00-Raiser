import boto3
import botocore

GAME = "Core Keeper"
REGION = "ap-southeast-1"
INSTANCE_SIZE = 8


def lambda_handler():

    # Connect to region
    ec2 = boto3.client("ec2", region_name=REGION)

    # Delete any current AMIs
    images = ec2.describe_images(
        Filters=[
            {
                "Name": "tag:Game",
                "Values": [
                    GAME,
                ],
            },
            {
                "Name": "tag:InstanceType",
                "Values": [
                    "GAME_SERVER",
                ],
            },
        ],
        OwnerIds=["self"]
    )["Images"]
    for ami in images:
        if ami["Name"] == GAME:
            print("Deleting image {}".format(ami["ImageId"]))
            ec2.deregister_image(DryRun=False, ImageId=ami["ImageId"])

    # Get existing snapshot
    response = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:Game",
                "Values": [
                    GAME,
                ],
            },
            {
                "Name": "tag:InstanceType",
                "Values": [
                    "GAME_SERVER",
                ],
            },
        ],
    )

    snapshot = response["Snapshots"][0]["SnapshotId"]
    print("Using snapshot {}".format(snapshot))

    # Create a new AMI
    ami = ec2.register_image(
        Name= GAME + " Server",
        Description= GAME + " Automatic AMI",
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/sda1",
                "Ebs": {
                    "DeleteOnTermination": False,
                    "SnapshotId": snapshot,
                    "VolumeSize": INSTANCE_SIZE,
                    "VolumeType": "gp2",
                },
            },
        ],
        Architecture="x86_64",
        RootDeviceName="/dev/sda1",
        DryRun=False,
        VirtualizationType="hvm",
    )
    print("Created image {}".format(ami["ImageId"]))

    ec2.create_tags(
        Resources=[ami["ImageId"]],
        Tags=[
            {"Key": "Name", "Value": GAME + " Server"},
            {"Key": "Game", "Value": GAME},
            {"Key": "InstanceType", "Value": "GAME_SERVER"},
        ],
    )
