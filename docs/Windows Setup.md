# Change Administrator password

The first thing you should do is to change the Windows password for admin as the password will no longer be retrievable on future instances.

1. Navigate to Control Panel > User Accounts > Manage Accounts
2. Create a new user and change it's account type to admin.
3. Close the RDP Session and attempt to remote using your newly created account to verify that it is working.

# Install SteamCMD

1. Use the browser to navigate to https://developer.valvesoftware.com/wiki/SteamCMD
2. Download the SteamCMD client and extract it to the C Drive.
3. Run the SteamCMD client.


# Setup startup script

To start the server without logging in, use Task Scheduler.  
Create a new folder called V Rising Server. Within this folder, create a basic task.  
Configure the task to start a program and start C:\Windows\System32\cmd.exe  
Set the arguments as /c start "" "C:\steamcmd\steamapps\common\VRisingDedicatedServer\start_server.bat"  
and start in directory to C:\steamcmd\steamapps\common\VRisingDedicatedServer (no quotes)

Save the task and edit it's properties to ensure that it is "run only when user is logged on".  
Test your task by running it through the task scheduler. The batch file should run and the cmd should be clearly visible.  
Once you have verified that the task works, set it to "Run whether user is logged on or not". This will automatically start the V Rising Server once the instance is created. This disables the GUI for the script so you will no longer be able to see the cmd window when you run the script again. Task Manager should however, still show that VRisingServer is running in the background.
