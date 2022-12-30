import boto3
import botocore

GAME = "V Rising"
REGION = "ap-southeast-1"
INSTANCE_SIZE = 8

def lambda_handler():

    # Connect to region
    ec2 = boto3.client("ec2", region_name=REGION)

    status = { "status": "Unknown" }

    if (check_server_is_running(ec2, status)): 
        return status
    if (check_server_is_stopping(ec2, status)): 
        return status
    if (check_if_image_exists(ec2, status)): 
        return status
    if (check_if_snapshot_archived(ec2, status)): 
        return status    

    return status

def check_server_is_running(ec2, server):
    reservations = ec2.describe_instances(
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
                    "Name": "instance-state-name",
                    "Values": [
                        "pending", "running"
                    ],
                }
            ],
        )["Reservations"]

    if (len(reservations) > 1):
        raise Exception("More than one reservation")

    if (len(reservations) == 1):
        instances = reservations[0]["Instances"]

        # Server is running
        if (len(instances) == 1):
            server["status"] = "running"
            server["instance_id"] = instances[0]["InstanceId"]
            server["ip_address"] = instances[0]["PublicIpAddress"]
        return True
    
    return False


def check_server_is_stopping(ec2, server):
    reservations = ec2.describe_instances(
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
                "Name": "instance-state-name",
                "Values": [
                    "stopping", "shutting-down"
                ],
            }
                    
        ],
    )["Reservations"]

    if (len(reservations) > 1):
        raise Exception("More than one reservation")

    if (len(reservations) == 1):
        instances = reservations[0]["Instances"]
        # Server is stopping
        if (len(instances) != 0):
            server["status"] = "stopping"
            server["instance_id"] = instances[0]["InstanceId"]
            return True
    
    return False

def check_if_image_exists(ec2, server):
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
        ]
    )["Images"]

    if (len(images) > 1):
        raise Exception("More than one image")

    if (len(images) == 1):
        server["status"] = "stopped"
        server["ami_id"] = images[0]["ImageId"]
        return True
    
    return False

def check_if_snapshot_archived(ec2, server):
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
    )

    if (len(response["Snapshots"]) > 1):
        raise Exception("More than one snapshot")

    if (len(response["Snapshots"]) == 1):
        server["status"] = "archived"
        server["snapshot_id"] = response["Snapshots"][0]["SnapshotId"]
        return True
    
    return False

print(lambda_handler())