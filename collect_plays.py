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

def list_messages(token_type='Bot', token='', channel_id='', params={}):
    headers = {
        "Authorization": "{type} {token}".format(type=token_type, token=token)
    }
    url = '{host}/channels/{channel_id}/messages'.format(host=API_ENDPOINT, channel_id=channel_id)
    r = requests.get(url, headers=headers, params=params)
    return r.json()

def utc_to_local(utc_dt, local):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local)
    return local.normalize(local_dt) # .normalize might be unnecessary



@click.command()
@click.option('--channel_id')
@click.option('--bot_token')
@click.option('--tz', default='America/Los_Angeles')
def main(channel_id, bot_token, tz):
    messages = list_messages(token=bot_token, channel_id=channel_id)
    local_tz = pytz.timezone(tz)
    for message in messages:
        writer = csv.writer(sys.stdout, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        content = message['content']
        time = datetime.fromisoformat(message['timestamp'])
        time = utc_to_local(time, local_tz)
        today = datetime.now(tz=local_tz)
        if time.date() != today.date():
            break
        try:
            last_name, line_with_side, stat, sport = content.split(' ', 4)
            side = line_with_side[0]
            line = line_with_side[1:len(line_with_side)]
            row = [
                "{}-{}-{}".format(time.month, time.day, time.year),
                "",
                last_name,
                sport,
                side, 
                line, 
                stat,
            ]
            writer.writerow(row)
        except ValueError as e:
            # try to unpack first and last name....
            first_name, last_name, line_with_side, stat, sport = content.split(' ', 5)
            side = line_with_side[0]
            line = line_with_side[1:len(line_with_side)]
            row = [
                "{}-{}-{}".format(time.month, time.day, time.year),
                first_name,
                last_name,
                sport,
                side, 
                line, 
                stat,
            ]
            writer.writerow(row)


if __name__ == '__main__':
    main()



