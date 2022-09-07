import boto3
import discord
import time

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

aws = boto3.client("ec2")
ec2 = boto3.resource("ec2")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("00R help"):
        await message.channel.send(
            "```"
            + "00R vrising start - Starts the V Rising Server\n"
            + "00R vrising stop - Stops the V Rising Server\n"
            + "00R vrising status - Gets the V Rising Server status\n"
            + "00R minecraft start - Starts the Minecraft Server\n"
            + "00R minecraft stop - Stops the Minecraft Server\n"
            + "00R minecraft status - Gets the Minecraft Server status\n"
            + "```"
        )

    if message.content.startswith("00R vrising start"):
        images = aws.describe_images(
            Owners=["self"], Filters=[{"Name": "name", "Values": ["V Rising Server"]}]
        )
        amiId = images["Images"][0]["ImageId"]
        print("Launching new instance with AMI id: " + amiId)
        instances = ec2.create_instances(
            LaunchTemplate={
                "LaunchTemplateId": "lt-06d69bc8cce351113",
                "Version": "1",
            },
            ImageId=amiId,
            MinCount=1,
            MaxCount=1,
        )

        instance = instances[0]

        print("Instance (id: " + instance.instance_id + ") created")

        while instance.public_ip_address == None:
            instance.load()
            time.sleep(10)

        server_ip = instance.public_ip_address
        await message.channel.send(
            "Server is running with IP: {}:9876".format(server_ip)
        )

    if message.content.startswith("00R vrising stop"):
        instances = ec2.instances.filter(
            Filters=[
                {
                    "Name": "tag:Name",
                    "Values": ["V Rising Server"],
                }
            ]
        )
        for instance in instances:
            if instance.state["Name"] == "running":
                instance.terminate()
                await message.channel.send("Server stopped")

    if message.content.startswith("00R vrising status"):
        instances = ec2.instances.filter(
            Filters=[{"Name": "tag:Name", "Values": ["V Rising Server"]}]
        )

        for instance in instances:
            if instance.state["Name"] == "running":
                await message.channel.send(
                    "Server is running with IP: {}:9876".format(
                        instance.public_ip_address
                    )
                )
            else:
                await message.channel.send("Server is not running")


client.run("MTAxNjk3MDUyMjc5MTI2MDE5NA.GGkv3h.Us3sIeswYMohRX8EX0dHrTIXSpiTREAhn6m3HY")
