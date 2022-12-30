import boto3
from datetime import datetime, timedelta, timezone

GAME = "Core Keeper"
REGION = "ap-southeast-1"
INSTANCE_SIZE = 8
INACTIVITY_PERIOD = 30 # in days

def lambda_handler():

    # Connect to region
    ec2 = boto3.client("ec2", region_name=REGION)

    # Get existing snapshot
    response = ec2.describe_snapshots(
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
    )

    # Check for any snapshots older than INACTIVITY_PERIOD
    for snapshot in response["Snapshots"]:
        if snapshot["StartTime"] < (datetime.now() - timedelta(days=INACTIVITY_PERIOD)).replace(
            tzinfo=timezone(offset=timedelta())
        ):
            # Delete any current AMIs
            images = ec2.describe_images(Filters=[
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
            Owners=["self"])["Images"]
            for ami in images:
                print("Deleting image {}".format(ami["ImageId"]))
                ec2.deregister_image(DryRun=False, ImageId=ami["ImageId"])

            # Archive snapshot
            ec2.modify_snapshot_tier(
                SnapshotId=snapshot["SnapshotId"], StorageTier="archive"
            )
            print("Archiving snapshot: {}".format(snapshot["SnapshotId"]))

