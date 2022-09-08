import asyncio


async def help_handler(ctx):
    await ctx.send(
        "You must provide a subcommand, available commands: "
        + "```"
        + "00R vrising start\n"
        + "00R vrising stop\n"
        + "00R vrising status\n"
        + "```"
    )


async def status_handler(message, ec2):
    instances = ec2.instances.filter(
        Filters=[{"Name": "tag:Name", "Values": ["V Rising Server"]}]
    )

    found = False

    for instance in instances:
        if instance.state["Name"] == "running":
            found = True
            await message.channel.send(
                "Server is running with IP: {}:9876".format(instance.public_ip_address)
            )

    if not found:
        await message.channel.send("Server is not running")


async def stop_handler(message, ec2):
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


async def start_handler(message, ec2, aws):
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
        asyncio.sleep(10)

    server_ip = instance.public_ip_address
    await message.channel.send("Server is running with IP: {}:9876".format(server_ip))
