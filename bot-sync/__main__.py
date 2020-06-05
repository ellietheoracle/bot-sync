"""
bot-sync gets all emotes from a source control room,
and syncs them with all rooms in config file.
rooms can also be added through the bot.
"""

import asyncio, os, json

# imports the client from matrix-nio, the python matrix sdk
from nio import AsyncClient

# client login data config file
CONFIG_FILE = "restore_login_config.json"
# bot affected rooms data
ROOMS_FILE = "rooms.json"


# creates a client instance
async def main() -> None:
    client = AsyncClient("https://the-apothecary.club", "@bot-sync:the-apothecary.club")

    # imports login data
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
        client.access_token = config["access_token"]
        client.user_id = config["user_id"]
        client.device_id = config["device_id"]

    # sends a test message
    await bot_send_msg(client, "Emi, your love has caused my heart to bleed .")

    # ends the connection
    await client.close()


# function to send state events
async def bot_send_state():
    pass


# function to send messages
async def bot_send_msg(client: AsyncClient, message: str):
    await client.room_send(
        room_id,
        message_type="m.room.message",
        content={"msgtype": "m.text", "body": message},
    )


asyncio.get_event_loop().run_until_complete(main())
