import boto3
import botocore

GAMING_INSTANCE_NAME = "Core Keeper"
GAMING_INSTANCE_REGION = "ap-southeast-1"
GAMING_INSTANCE_SIZE_GB = 8


def lambda_handler(object, context):

    # Connect to region
    ec2 = boto3.client("ec2", region_name=GAMING_INSTANCE_REGION)

    # Delete any current AMIs
    images = ec2.describe_images(Owners=["self"])["Images"]
    for ami in images:
        if ami["Name"] == GAMING_INSTANCE_NAME:
            print("Deleting image {}".format(ami["ImageId"]))
            ec2.deregister_image(DryRun=False, ImageId=ami["ImageId"])

    # Get existing snapshot
    response = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:Name",
                "Values": [
                    "Snapshot of Core Keeper",
                ],
            },
        ],
    )

    snapshot = response["Snapshots"][0]["SnapshotId"]
    print("Using snapshot {}".format(snapshot))

    # Create a new AMI
    ami = ec2.register_image(
        Name=GAMING_INSTANCE_NAME,
        Description=GAMING_INSTANCE_NAME + " Automatic AMI",
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/sda1",
                "Ebs": {
                    "DeleteOnTermination": False,
                    "SnapshotId": snapshot,
                    "VolumeSize": GAMING_INSTANCE_SIZE_GB,
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
            {"Key": "Name", "Value": GAMING_INSTANCE_NAME},
        ],
    )
