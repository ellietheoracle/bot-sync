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
        bot_control_room = config["control_room"]
        bot_template_room = config["template_room"]
        bot_rooms = config["rooms"]

    ## await bot_send_msg(client, "Online", bot_control_room)

    # get room state
    room_state = await client.room_get_state(bot_template_room)

    ## print(room_state)

    # execute in each room
    for room in bot_rooms:

        # logs room cycle
        print("Syncing state in:", room["id"])

        # join rooms if not already joined
        await client.join(room["id"])

        # sends a test message
        ##resp = await bot_send_msg(client, "Syncing...", room["id"])
        ##print(resp)
        # sends a test state event
        resp = await bot_set_emote(client, room["id"])
        print(resp)
        # ends the connection
        await client.close()


# function to send state events
async def bot_set_emote(client: AsyncClient, room: str):
    return await client.room_put_state(
        room, event_type="im.ponies.user_emotes", content={"short": {"test": "tube"}},
    )


# function to send messages
async def bot_send_msg(client: AsyncClient, message: str, room: str):
    return await client.room_send(
        room,
        message_type="m.room.message",
        content={"msgtype": "m.notice", "body": message},
    )


asyncio.get_event_loop().run_until_complete(main())
