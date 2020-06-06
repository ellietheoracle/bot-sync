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

    # import room data
    with open(ROOMS_FILE, "r") as f:
        config = json.load(f)
        control_room = config["control_room"]
        rooms = config["rooms"]

    await bot_send_msg(client, "Online", control_room)

    # execute in each room
    for room in rooms:
        await client.join(room)
        # sends a test message
        await bot_send_msg(client, "Testing state events:", room)

        # sends a test state event
        # await bot_set_emote(client,)
        # ends the connection
        await client.close()


# function to send state events
async def bot_set_emote(client: AsyncClient, room: str):
    await client.room_put_state(
        room, event_type="im.ponies.user_emotes", content={},
    )


# function to send messages
async def bot_send_msg(client: AsyncClient, message: str, room: str):
    await client.room_send(
        room,
        message_type="m.room.message",
        content={"msgtype": "m.notice", "body": message},
    )


asyncio.get_event_loop().run_until_complete(main())
