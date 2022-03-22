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

def list_guilds(token_type='Bot', token='', params={}):
    headers = {
        "Authorization": "{type} {token}".format(type=token_type, token=token)
    }
    url = '{host}/users/@me/guilds'.format(host=API_ENDPOINT)
    r = requests.get(url, headers=headers, params=params)
    return r.json()

@click.command()
@click.option('--bot_token')
def main(bot_token):
    guilds = list_guilds(token=bot_token)
    for g in guilds:
        print("=======================================\n")
        print("guild_id =",g['id'])
        print("name     =",g['name'])
        print("\n=======================================")



if __name__ == '__main__':
    main()



