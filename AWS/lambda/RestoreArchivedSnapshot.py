import boto3
from datetime import datetime, timedelta, timezone

GAME = "Core Keeper"
REGION = "ap-southeast-1"
INSTANCE_SIZE = 8


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
            {
                "Name": "storage-tier",
                "Values": [
                    "archive",
                ],
            }
        ],
        OwnerIds=["self"],
    )

    for snapshot in response["Snapshots"]:
        response = ec2.restore_snapshot_tier(
            SnapshotId=snapshot["SnapshotId"],
            PermanentRestore=True,
        )
        print("Restored snapshot {}".format(snapshot["SnapshotId"]))
