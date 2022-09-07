import boto3
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client.run("MTAxNjk3MDUyMjc5MTI2MDE5NA.GGkv3h.Us3sIeswYMohRX8EX0dHrTIXSpiTREAhn6m3HY")

ec2 = boto3.client("ec2")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("describe_images"):
        images = ec2.describe_images(["self"])
        print(images)
        await message.channel.send("Done!")
