import boto3
import botocore

GAME = "Minecraft"
REGION = "ap-southeast-1"

class AWS:

    def __init__(self, region=REGION, ec2=None):
        self.region = region
        self.ec2 = ec2
        self.ec2r = boto3.resource("ec2")

    def __enter__(self):
        self.ec2 = boto3.client("ec2", region_name=self.region)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.ec2.close()

    def get_server_status(self, game):    

        status = {"game": game, "status": "Unknown"}

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
                server["instance_type"] = instances[0]["InstanceType"]
                server["network_interface_id"] = instances[0]["NetworkInterfaces"][0]["NetworkInterfaceId"]

                if ("PublicIpAddress" in instances[0]):
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


    def start_server(self, game, configs):

        server = self.get_server_status(game)
        templateId = self._get_launch_template_id(game)

        instances = self.ec2r.create_instances(
            LaunchTemplate={
                "LaunchTemplateId": templateId,
            },
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'DeleteOnTermination': False,
                        'VolumeSize': configs["volume_size"],
                        'VolumeType': 'gp2',
                    }
                },
            ],
            InstanceType= configs["instance_type"],
            ImageId=server["ami_id"],
            MinCount=1,
            MaxCount=1,
        )

        return instances


    def _get_launch_template_id(self, game):
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

    def stop_server(self, game):

        server = self.get_server_status(game)

        response = self.ec2.terminate_instances(
            InstanceIds=[
                server["instance_id"],
            ],
        )

        return response

    def wait_for_server_to_stop(self, game):
        
        server = self.get_server_status(game)

        waiter = self.ec2.get_waiter('instance_terminated')
        waiter.wait(
            InstanceIds=[
                server["instance_id"],
            ],
        )

    def wait_for_server_ip(self, game):

        server = self.get_server_status(game)

        waiter = self.ec2.get_waiter('instance_running')
        waiter.wait(
            InstanceIds=[
                server["instance_id"],
            ],
        )