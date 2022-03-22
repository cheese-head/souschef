# Souschef
A Discord Bot for the bakery. 

## Getting Started
### Discord Setup
- Login to https://discord.com/developers/applications
- Create a new application
- Add a Bot to the newly created application
- Click on OAuth2 -> URL Generator
- Select the "bot" scope
  - Read Messages/View Channels
- Copy the generated url and navigate to it in a new browser. Select the server you want to add the Bot in
- Navigate to the Bot settings page
  - Reset and copy the Bot's security token
### Docker
If you don't want to deal with installing python and the additional pip libraries, you can use docker to run this script. [Docker](https://www.docker.com/)

### Args/Variables
* channel_id [required] - this is the id of the channel that will be used for parsing the picks. 
* bot_token  [required] - this is the bot's secret token (provided by Discord)
* tz         [optional] - name of the timezone for deciding the day that the pick belongs to (defaults to 'America/Los_Angeles') 

### Building 

```bash
docker build . -t souschef
```
### Commands
There are three commands available
- list_guilds (list the guilds that the user belongs to)
- list_channels (list the channels that belong to a guild)
- collect_plays (parse plays from a specific channel)

### Running
```
export BOT_TOKEN="my secret bot token from discord...."
export CHANNEL_ID="channel id from discord"
docker run --env BOT_TOKEN --env CHANNEL_ID souschef:latest python collect_plays.py --channel_id=$CHANNEL_ID --bot_token=$BOT_TOKEN
```


### Examples
```bash

(venv) ➜  souschef docker run --env BOT_TOKEN --env CHANNEL_ID souschef:latest python list_guilds.py --bot_token=$BOT_TOKEN
=======================================

guild_id = 95366588238150323
name     = My Server

=======================================

```

```bash
(venv) ➜  souschef docker run --env BOT_TOKEN --env CHANNEL_ID souschef:latest python list_channels.py --guild_id=953665882381504582 --bot_token=$BOT_TOKEN
=======================================

channel_id = 953665882381504583
name       = Text Channels

=======================================
=======================================

channel_id = 953665882381504584
name       = Voice Channels

=======================================
=======================================

channel_id = 953665882381504585
name       = general

=======================================
=======================================

channel_id = 953665882381504586
name       = General

=======================================
=======================================

channel_id = 953665949330993172
name       = jam-challenge

=======================================

```

```bash
(venv) ➜  souschef docker run --env BOT_TOKEN --env CHANNEL_ID souschef:latest python collect_plays.py --channel_id=$CHANNEL_ID --bot_token=$BOT_TOKEN
3-22-2022,j,wilkins,(CBB),u,12.5,pts
3-22-2022,,wilkins,(CBB),u,12.5,pts
```# souschef
