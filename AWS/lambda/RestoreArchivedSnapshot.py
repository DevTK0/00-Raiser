import boto3
from datetime import datetime, timedelta, timezone

GAMING_INSTANCE_NAME = "Core Keeper"
GAMING_INSTANCE_REGION = "ap-southeast-1"
GAMING_INSTANCE_SIZE_GB = 8


def lambda_handler(object, context):

    # Connect to region
    ec2 = boto3.client("ec2", region_name=GAMING_INSTANCE_REGION)

    # Get existing snapshot
    response = ec2.describe_snapshots(
        Filters=[
            {
                "Name": "tag:Name",
                "Values": [
                    "Snapshot of Core Keeper",
                ],
            },
        ],
    )

    for snapshot in response["Snapshots"]:
        if snapshot["StartTime"] < (datetime.now() - timedelta(days=0)).replace(
            tzinfo=timezone(offset=timedelta())
        ):
            response = ec2.restore_snapshot_tier(
                SnapshotId=snapshot["SnapshotId"],
                PermanentRestore=True,
            )
            print("Restored snapshot {}".format(snapshot["SnapshotId"]))
