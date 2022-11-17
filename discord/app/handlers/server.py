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


async def status_handler(message, ec2, nametag):
    instances = ec2.instances.filter(
        Filters=[{"Name": "tag:Name", "Values": [nametag]}]
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


async def stop_handler(message, ec2, nametag):
    instances = ec2.instances.filter(
        Filters=[
            {
                "Name": "tag:Name",
                "Values": [nametag],
            }
        ]
    )
    for instance in instances:
        if instance.state["Name"] == "running":
            instance.terminate()
            await message.channel.send("Server stopped")


async def start_handler(message, ec2, aws, nametag, templateId):
    images = aws.describe_images(
        Owners=["self"], Filters=[{"Name": "name", "Values": [nametag]}]
    )
    amiId = images["Images"][0]["ImageId"]
    print("Launching new instance with AMI id: " + amiId)
    instances = ec2.create_instances(
        LaunchTemplate={
            "LaunchTemplateId": templateId,
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
        await asyncio.sleep(10)

    server_ip = instance.public_ip_address
    await message.channel.send("Server is running with IP: {}:9876".format(server_ip))
