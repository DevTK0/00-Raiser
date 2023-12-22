# Starting the app
This application uses poetry for it's dependency management. Please ensure that you have it installed.
```
poetry install
poetry run app
```

Run the following to sync the slash commands to the server.
```
00R <game> sync <guild_id>
```

The following slash commands are available:
```
/<game> start
/<game> stop
/<game> status
```

# Running Tests


```bash
# run all tests
pytest

# run specific tests
pytest -k <method_name> -v
```

# Deployment
The bot is hosted on Fly.io

```
flyctl deploy
```

# FAQs
1. Slash commands for the cogs aren't working.

Please run the sync command (for each cog) for every new Discord Server. This will tell Discord to register the /commands with the server.
