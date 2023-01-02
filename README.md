# Starting the app
```
 python3 -m venv venv
source venv/bin/activate
python3 -m pip install -e .
python3 -m app.bot
```
Runs app/bot.py

```
00R <game> sync <guild_id>
```
Syncs the slash commands to the server.

```
/load <extension>
/reload <extension>
/unload <extension>
```
Slash commands for managing extensions.

# Running Tests

## Run all tests
```
pytest
```

## Running specific tests
```
pytest -k <method_name> -v
```

-k flag will run all tests that satisfy the substring matching on the method name


# FAQs
1. Slash commands for the cogs aren't working.

Due to the way cogs are imported, the cogs will only be loaded after main bot runs the sync command.
As such, You will need to manually sync using the text based sync command.

2. I reloaded a cog and now the slash commands aren't working

For some reason, there is no easy way to update/replace existing slash commands so when you reload the cogs and run the sync again, it will throw an error indicating duplicate commands. The only way to resolve this at the moment is to restart the bot or kick it and make it rejoin the server.
