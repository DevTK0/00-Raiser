# Create corekeeper user 
```
sudo adduser corekeeper
sudo su - corekeeper
```

# Install SteamCMD

```
sudo add-apt-repository multiverse
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install lib32gcc-s1 steamcmd
steamcmd +login anonymous +app_update 1963720 +quit
```

# Configure CoreKeeper as a service
```
[Unit]
Description=CoreKeeper
After=network.target

[Service]
Type=forking
User=corekeeper
Group=corekeeper
ExecStart=exec "/home/corekeeper/Steam/steamapps/common/Core Keeper Dedicated Server/launch.sh"
ExecStop=sudo pkill -15 CoreKeeper
Restart=on-failure
RestartSec=1s
WorkingDirectory=/home/corekeeper/Steam/steamapps/common/Core Keeper Dedicated Server

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl enable corekeeper
sudo systemctl start corekeeper
sudo systemctl status corekeeper
```

# References
- https://www.reddit.com/r/CoreKeeperGame/comments/uym86p/dedicated_core_keeper_server_tips_tricks/
- https://github.com/escapingnetwork/core-keeper-dedicated