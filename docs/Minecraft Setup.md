# Install Java and Git

```
sudo apt update
sudo apt install openjdk-18-jre-headless
sudo apt install git
```

# Setup Minecraft user

```
sudo adduser minecraft
sudo su - minecraft
```

# Configure Firewall
```
sudo ufw allow 25565
sudo ufw enable
sudo ufw status
```
Output:
```
Status: active

To                         Action      From
--                         ------      ----
OpenSSH                    ALLOW       Anywhere
25565                      ALLOW       Anywhere
OpenSSH (v6)               ALLOW       Anywhere (v6)
25565 (v6)                 ALLOW       Anywhere (v6)
```


# Download and install Spigot
```
mkdir buildtools && cd buildtools
wget -O BuildTools.jar  https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
java -jar BuildTools.jar --rev latest
cd ~ && mkdir server && cd server
mv ~/buildtools/spigot-*.jar ~/server/spigot.jar
vim spigotstart.sh
```
spigotstart.sh
```
#!/bin/sh

java -Xms3G -Xmx3G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar spigot.jar nogui
```

```
chmod +x spigotstart.sh
./spigotstart.sh
vim eula.txt
```

# Configure Spigot as a service

```
sudo vim /etc/systemd/system/spigot.service
```
spigot.service
```
[Unit]
Description=SpigotMC
After=network.target

[Service]
Type=forking
User=minecraft
Group=minecraft
ExecStart=/usr/bin/screen -d -m -S minecraft /home/minecraft/server/spigotstart.sh
ExecStop=/usr/bin/screen -S minecraft -p 0 -X stuff "stop$(printf \\r)"
WorkingDirectory=/home/minecraft/server

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl enable spigot
sudo systemctl start spigot
sudo systemctl status spigot
```

# References
- https://www.howtoforge.com/how-to-install-spigot-minecraft-server-on-ubuntu-20-04/
- https://www.reddit.com/r/aws/comments/n18gjn/how_can_i_automatically_copy_files_to_nvme_and/
- https://github.com/doctorray117/minecraft-ondemand/