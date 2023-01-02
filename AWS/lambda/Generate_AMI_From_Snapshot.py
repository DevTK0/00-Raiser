import boto3
import botocore

GAMING_INSTANCE_REGION = 'ap-southeast-1'
INSTANCE_TYPE = "GAME_SERVER"

def lambda_handler(object, context):

    # Connect to region
    ec2 = boto3.client('ec2',region_name=GAMING_INSTANCE_REGION)
    res_client = boto3.resource('ec2', region_name=GAMING_INSTANCE_REGION)

    # Get all available volumes    
    volumes = ec2.describe_volumes( Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes'] 
    
    # Get all volumes for the given instance    
    volumes_to_delete = []
    for volume in volumes:
        if 'Tags' not in volume:
            continue
        for tag in volume['Tags']:
            if tag['Key'] == 'InstanceType' and tag['Value'] == INSTANCE_TYPE:
                volumes_to_delete.append(volume)
                
    if len(volumes_to_delete) == 0:
        print('No volumes found. Nothing to do! Aborting...')
        return

    for volume in volumes_to_delete:
        
        # Get the name of the server
        tags = volume['Tags']        
        for tag in volume['Tags']:
            if tag['Key'] == 'Name':
                name = tag['Value']
        
        # Delete any current AMIs
        images = ec2.describe_images(Owners=['self'])['Images']
        for ami in images:
            if ami['Name'] == name:
                print('Deleting image {}'.format(ami['ImageId']))
                ec2.deregister_image(DryRun=False,ImageId=ami['ImageId'])


        # Create a snapshot of the volume
        snap = ec2.create_snapshot(VolumeId=volume['VolumeId'], TagSpecifications=[{'ResourceType': 'snapshot', 'Tags': volume['Tags']}])
        snap_id = snap['SnapshotId']
        snap_waiter = ec2.get_waiter('snapshot_completed')
        
        try:
            snap_waiter.wait(SnapshotIds=[snap_id], WaiterConfig={'Delay': 15,'MaxAttempts': 60 })
            print("Created snapshot: {}".format(snap['SnapshotId']))
        except botocore.exceptions.WaiterError as e:
            print("Could not create snapshot, aborting")
            print(e.message)
            return        

        # Remove previous snapshots of the volumes
        previous_snapshots = ec2.describe_snapshots(Filters=[{'Name': 'tag:Name', 'Values': [name]}])['Snapshots']
        for snapshot in previous_snapshots:
            if snapshot['SnapshotId'] != snap['SnapshotId']:
                print("Removing previous snapshot: {}".format(snapshot['SnapshotId']))
                ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

        # Create a new AMI with the new snapshot
        ami = ec2.register_image(
            Name=name, 
            RootDeviceName="/dev/sda1",
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'DeleteOnTermination': False,
                        'SnapshotId': snap['SnapshotId']
                    }
                },
            ],
        )
        print('Created image {}'.format(ami['ImageId']))

        # Tag the AMI
        ec2.create_tags(
            Resources=[ami['ImageId']],
            Tags=[
                {'Key': 'InstanceType', 'Value': 'GAME_SERVER'},
                {'Key': 'Name', 'Value': name}
            ]
        )

    # Delete the volumes
    for volume in volumes_to_delete:
        v = res_client.Volume(volume['VolumeId'])
        print("Deleting EBS volume: {}, Size: {} GiB".format(v.id, v.size))
        v.delete()
        
lambda_handler(None, None)