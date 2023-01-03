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
poetry pytest

# run specific tests
poetry pytest -k <method_name> -v
```

# Deployment
The bot is hosted on railway.app
Any changes to the repository will automatically trigger a deployment.

# FAQs
1. Slash commands for the cogs aren't working.

Due to the way cogs are imported, the cogs will only be loaded after main bot runs the sync command.
As such, You will need to manually sync using the text based sync command.

2. I reloaded a cog and now the slash commands aren't working

For some reason, there is no easy way to update/replace existing slash commands so when you reload the cogs and run the sync again, it will throw an error indicating duplicate commands. The only way to resolve this at the moment is to restart the bot or kick it and make it rejoin the server.
