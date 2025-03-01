import aiohttp
import os
import json
from dotenv import load_dotenv 
from discord import Webhook

load_dotenv(".env")
ownerID = int(os.getenv("ownerid"))

async def sendWebhook(content):
    async with aiohttp.ClientSession() as session:
        url = os.getenv("webhookURL")
        if url:
            webhook = Webhook.from_url(url, session=session)
            await webhook.send(content, username="Bot Log")
        else:
            print("ERROR: No Webhook URL found!")

#Update env values
def updateroles():
    load_dotenv(override=True)
    return {
        "whipRole": os.getenv("whipRole"),
        "btRole": os.getenv("btRole"),
        "chairRole": os.getenv("chairRole")
    }

#Update usesID value from .env
def updateuseid():
    load_dotenv(override=True)
    usesID = os.getenv("usesid")
    return usesID

# File to store whip data
DATA_FILE = "whip_data.json"

# Function to load whip data from the file
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if file doesn't exist
    except json.JSONDecodeError:
        return {}  # Return empty dict if file is empty or invalid

# Function to save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)