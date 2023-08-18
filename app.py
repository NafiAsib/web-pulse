from dotenv import load_dotenv
import os
import json
import time
import requests
from datetime import datetime

load_dotenv()


def send_notification_teams(webhook_url):
    try:
        with open("teams.json", "r") as f:
            data = json.load(f)
            current_time = datetime.now().strftime("%I:%M %p")
            data["text"] = f"The server is down, please check it out! ⏰ {current_time}"
            requests.post(webhook_url, json=data)

    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {str(e)}")


def send_notification_discord(webhook_url):
    try:
        with open("discord.json", "r") as f:
            data = json.load(f)
            current_time = datetime.now().strftime("%I:%M %p")

            data["embeds"][0][
                "description"
            ] = f"The server is down, please check it out! ⏰ {current_time}"
            requests.post(webhook_url, json=data)

    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {str(e)}")


def check_website(website_url, teams_webhook_url, discord_webhook_url):
    try:
        response = requests.get(website_url, timeout=5)
        if response.status_code != 200:
            send_notification_teams(teams_webhook_url)
            send_notification_discord(discord_webhook_url)

    except requests.exceptions.RequestException as e:
        print(f"Error checking {website_url}: {str(e)}")


teams_webhook_url = os.getenv("TEAMS")
discord_webhook_url = os.getenv("DISCORD")
website_url = os.getenv("WEBSITE")

check_website(website_url, teams_webhook_url, discord_webhook_url)
