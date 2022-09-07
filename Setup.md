## Setup instructions

This article describes how this project was setup from scratch.

# Core Concepts

This project uses the following:

-   AWS EC2
-   AWS Lambda Functions
-   AWS Snapshots
-   AWS EBS Volumes
-   AWS AMI
-   SteamCMD
-   V Rising Server Client

# System Description

The V Rising Server Client runs on a single EC2 (g4dn.large) instance. To minimize cost, the system has been designed to start and stop using text commands sent to a discord bot. Thereafter, the bot programmatically starts/stops and backs up everything. The following concepts have been utilized to minimise cost:

1. Use Snapshots instead of EBS volumes.
2. Automatically terminate instance when idle.

**On Startup**

**On Shutdown**
When the EC2 instance has been terminated, the EBS Volume will remain so that we can back it up as a snapshot. An AWS Lambda Function has been configured to execute this on instance termination.

# Setup Instructions

1. Create a new EC2 Instance

2. Install V Rising Server

3. Configure Backup Lambda

4. Configure AMI

5. Setup Discord Bot

# FAQ

# References

-   https://www.youtube.com/watch?v=gE20QLY6gAI
