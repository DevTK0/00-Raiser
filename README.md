# vrisingserver

## Implementation of V Rising Server hosted on AWS


# Starting the app
```
source venv/bin/activate
python3 -m app.bot
```
Runs app/bot.py

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
