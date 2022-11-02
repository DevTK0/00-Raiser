# Install V Rising Server

1. Run the SteamCMD Client.
2. Enter "login anonymous" in the terminal.  
3. Enter "App_update 1829350" to start installing the V Rising Server.
4. Navigate to "C:\steamcmd\steamapps\common\VRisingDedicatedServer"
5. Run start_server_example.bat to verify that the server is working.
6. If you have any backups to setup, you can upload them to "C:\steamcmd\steamapps\common\VRisingDedicatedServer\save-data\"

# Configure Firewall
For clients to be able to start connecting to the server, you need to open up the TCP and UDP ports required.

1. Search for Windows Firewall and select advanced settings.  
2. Select Inbound rules and select New Rule.
3. Select Rule Type: Port
4. Create a new TCP and add 9876-9877 to the inbound port rules. (Keep the default settings for everything else.)
5. Repeat the above to create a UDP rule with the same settings.

![TCP Firewall Rule](screenshots/V%20Rising/TCP-Firewall-Rule.png)

# Add Security Group 
AWS will block all unauthorised connections to the server instance, so we will need to create a security group to allow requests to the game's required ports.

![V Rising Security Group](screenshots/V%20Rising/V-Rising-SG.png)

