## Setup instructions

This article describes how this project was setup from scratch.

# Core Concepts

This project uses the following:

-   AWS EC2
-   AWS Lambda Functions
-   AWS EventBridge
-   AWS Snapshots
-   AWS EBS Volumes
-   AWS AMI & Launch Templates
-   SteamCMD
-   V Rising Server Client

# System Description

The V Rising Server Client runs on a single EC2 (g4dn.large) instance. To minimize cost, the system has been designed to start and stop using text commands sent to a discord bot. Thereafter, the bot programmatically starts/stops and backs up everything. The following concepts have been utilized to minimise cost:

1. Use Snapshots instead of EBS volumes.
2. Automatically terminate instance when idle.

**On Startup**
The system uses a Launch Template to startup future instances of the server. This instance will use the previous instances as an AMI (see SnapAndDelete script).

**On Shutdown**
When the EC2 instance has been terminated, the EBS Volume will remain so that we can back it up as a snapshot. An AWS Lambda Function has been configured to execute this on instance termination.

# Setup Instructions

1. Create a new EC2 Instance

On the first setup, we will need to configure the instance for which successive instances will be based on.
Launch a new EC2 instance with the following configurations:

-   Name: "V Rising Server"
-   AMI : "Windows_Server-2022"
-   Instance Type: "g4dn.xlarge"
-   Key Pair: "v-rising-server"
-   Network Settings: "V-Rising-SG"
-   Storage: "512 gp2, Delete on termination - No, Encrypted - No"
-   Request Spot Instances

Once created, connect to the instance using remote desktop.

Note: First thing you should do is to change the Windows password for admin as the password will no longer be retrievable on future instances.

2. Install V Rising Server

See Windows Setup.

3. Configure Backup Lambda

Create a new lambda function. Use SnapAndDelete.py as your lambda function making sure to set the GAMING_INSTANCE_NAME, GAMING_INSTANCE_REGION and GAMING_INSTANCE_SIZE_GB appropriately. Once done, deploy and test the lambda. The lambda should delete the EBS Volume, create a new snapshot and AMI from the previous instance. You should see a lambda output similar to the following:

```
START RequestId: 4e2ece9c-3b3f-4b2f-8c0b-7eea3ad5a824 Version: $LATEST
Created snapshot: snap-08bc41c0df0dae964
Deleting EBS volume: vol-037f2c2d0a0aba6d1, Size: 512 GiB
Created image ami-0b55e3c0d99eb0bdf
END RequestId: 4e2ece9c-3b3f-4b2f-8c0b-7eea3ad5a824
REPORT RequestId: 4e2ece9c-3b3f-4b2f-8c0b-7eea3ad5a824	Duration: 212933.36 ms	Billed Duration: 212934 ms	Memory Size: 128 MB	Max Memory Used: 83 MB
```

4. Configure EventBridge

To invoke the lambda created, create a new rule to run whenever the EC2 instance is terminated.

5. Configure Launch Template

Create a launch template with the same configurations as step 1.

6. Setup Discord Bot

# FAQ

# References

-   https://www.rockpapershotgun.com/v-rising-server
-   https://www.youtube.com/watch?v=gE20QLY6gAI
