import requests
import json
from datetime import date, datetime
import csv 
import sys
import itertools
import re 
import click
import pytz

API_ENDPOINT = 'https://discord.com/api/v8'

def list_channels(token_type='Bot', token='', guild_id='', params={}):
    headers = {
        "Authorization": "{type} {token}".format(type=token_type, token=token)
    }


    url = '{host}/guilds/{guild_id}/channels'.format(host=API_ENDPOINT, guild_id=guild_id)
    r = requests.get(url, headers=headers, params=params)
    return r.json()

@click.command()
@click.option('--bot_token')
@click.option('--guild_id')
def main(bot_token, guild_id):
    channels = list_channels(token=bot_token, guild_id=guild_id)
    for c in channels:
        print("=======================================\n")
        print("channel_id =", c['id'])
        print("name       =", c['name'])
        print("\n=======================================")



if __name__ == '__main__':
    main()


