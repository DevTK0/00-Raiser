# Change Administrator password

# Install SteamCMD

# Install V Rising Server

To install the V Rising Server Client, first download SteamCMD from https://developer.valvesoftware.com/wiki/SteamCMD.
Once done, run the SteamCMD client, a CMD window should appear and start installing the client.
When the SteamCMD client is done installing, enter "login anonymous" in the same terminal.
Afterwhich, enter "App_update 1829350" to start installing the V Rising Server client through SteamCMD.
Once complete, go to "" and run the start_server_example.bat script to verify that the server is working.
If you have any backups that you would wish to setup, go to the "" folder and upload your backup files. The server should automatically load them on startup.

# Configure Firewall

For clients to be able to start connecting to the server, you need to open up the TCP and UDP ports required.
Search for Windows Firewall and select advanced.
Select TCP and add 9876-9877 to the inbound port rules.

# Setup startup script

To start the server without logging in, use Task Scheduler.
Create a new folder called V Rising Server. Within this folder, create a basic task.
Configure the task to start a program and start C:\Windows\System32\cmd.exe
Set the arguments as /c start "" "C:\steamcmd\steamapps\common\VRisingDedicatedServer\start_server.bat"
and start in directory to C:\steamcmd\steamapps\common\VRisingDedicatedServer (no quotes)

Save the task and edit it's properties to ensure that it is "run only when user is logged on".
Test your task by running it through the task scheduler. The batch file should run and the cmd should be clearly visible.
Once you have verified that the task works, set it to "Run whether user is logged on or not". This will automatically start the V Rising Server once the instance is created. This disables the GUI for the script so you will no longer be able to see the cmd window when you run the script again. Task Manager should however, still show that VRisingServer is running in the background.
