import boto3
import botocore

GAME = "Minecraft"
REGION = "ap-southeast-1"

class AWS:

    def __init__(self, region=REGION, ec2=None):
        self.region = region
        self.ec2 = ec2

    def __enter__(self):
        self.ec2 = boto3.client("ec2", region_name=self.region)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.ec2.close()

    def get_server_status(self, game):    

        status = { "status": "Unknown" }

        if (self._check_server_is_running(game, status)): 
            return status
        if (self._check_server_is_stopping(game, status)): 
            return status
        if (self._check_if_image_exists(game, status)): 
            return status
        if (self._check_if_snapshot_archived(game, status)): 
            return status    

        return status

    def _check_server_is_running(self, game, server):
        reservations = self.ec2.describe_instances(
                Filters=[
                    {
                        "Name": "tag:Game",
                        "Values": [
                            game,
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


    def _check_server_is_stopping(self, game, server):
        reservations = self.ec2.describe_instances(
            Filters=[
                {
                    "Name": "tag:Game",
                    "Values": [
                        game,
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

    def _check_if_image_exists(self, game, server):
        images = self.ec2.describe_images(
            Filters=[
                {
                    "Name": "tag:Game",
                    "Values": [
                        game,
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

    def _check_if_snapshot_archived(self, game, server):
        response = self.ec2.describe_snapshots(
            Filters=[
                {
                    "Name": "tag:Game",
                    "Values": [
                        game,
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


    def start_server(self, templateId, imageId):

        instances = self.ec2.create_instances(
            LaunchTemplate={
                "LaunchTemplateId": templateId,
                "Version": "1",
            },
            ImageId=imageId,
            MinCount=1,
            MaxCount=1,
        )

        return instances

    def get_launch_template_id(self, game):
        response = self.ec2.describe_launch_templates(
            Filters=[
                {
                    "Name": "tag:Game",
                    "Values": [
                        game,
                    ],
                },
                {
                    "Name": "tag:InstanceType",
                    "Values": [
                        "GAME_SERVER",
                    ],
                },
            ]
        )

        if (len(response["LaunchTemplates"]) > 1):
            raise Exception("More than one launch template")

        if (len(response["LaunchTemplates"]) == 1):
            return response["LaunchTemplates"][0]["LaunchTemplateId"]
        
        raise Exception("No launch template found")


with AWS() as aws:
    response = aws.get_launch_template_id(GAME) 