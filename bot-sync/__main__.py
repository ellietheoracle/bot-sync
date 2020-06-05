import asyncio, os, json
from nio import AsyncClient

CONFIG_FILE = "restore_login_config.json"
ROOMS_FILE = "rooms.json"
room_id = "!xwkzwkGafsaYJOFWoj:the-apothecary.club"

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)
    client.access_token = config["access_token"]
    client.user_id = config["user_id"]
    client.device_id = config["device_id"]


async def main() -> None:
    client = AsyncClient("https://the-apothecary.club", "@bot-sync:the-apothecary.club")
    bot_login(client)
    await bot_send_msg(client, "Emi, your love has caused my heart to bleed .")
    await client.close()


async def bot_send_state():
    pass


async def bot_send_msg(client: AsyncClient, message: str):
    await client.room_send(
        room_id,
        message_type="m.room.message",
        content={"msgtype": "m.text", "body": message},
    )


asyncio.get_event_loop().run_until_complete(main())
