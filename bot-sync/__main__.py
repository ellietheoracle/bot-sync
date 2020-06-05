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

    # sends a test message
    await bot_send_msg(client, "Testing state events:", control_room)
    
    #sends a test state event
    await bot_send_emote(client, control_room)
    # ends the connection
    await client.close()


# function to send state events
async def bot_send_emote(client: AsyncClient, room: str):
    await client.room_put_state(
        room,
        event_type="im.ponies.user_emotes",
        content={
            "short": {
                ":burger1:": "mxc://the-apothecary.club/c1972b2b379a91b0919efbe933d85e69e333ba50",
                ":burger2:": "mxc://the-apothecary.club/0174ad418a247c1cc6bbf6afde836693530dd5db",
                ":burger3:": "mxc://the-apothecary.club/ad64e6808539fcf29b2298a06eae707d12c7dd71",
                ":trans_heart:": "mxc://the-apothecary.club/70f1782ce09447aa5f8501329edd560a0d3ae9b3",
                ":floating_trans_heart:": "mxc://the-apothecary.club/c851fa9037faaa6626328ed424cf931696c4002b",
                ":the_lie:": "mxc://the-apothecary.club/dFVTAjSmZrkiSaRtqDytLXmo",
                ":otter:": "mxc://the-apothecary.club/nkhSgMaDbFitksExmkGbUrBu",
                ":porsche:": "mxc://the-apothecary.club/unycpBFgdpovHpDgXPjguNJQ",
                ":frog:": "mxc://the-apothecary.club/DarWZaOLoAfjZpWMRxVLUpjy",
                ":trans_egg:": "mxc://the-apothecary.club/QjhxhIVPOifVdAKGiYBoqUfn",
                ":oof:": "mxc://the-apothecary.club/d4f9d532f79645010615e937da7e9d13c8465038",
                ":zero:": "mxc://the-apothecary.club/7a7df440d575328d738194ece233577fcc3e6b58",
                ":gay:": "mxc://the-apothecary.club/a69dcd92ec061c69f06978f34c85395d925b3d57",
                ":yeet:": "mxc://the-apothecary.club/49f50e14d5159a45496b0e3a8b0c354f2fa80f38",
                ":lol:": "mxc://the-apothecary.club/d4e39d102698ca77ff0c1d70c8a037565b5ad460",
                ":owo:": "mxc://the-apothecary.club/b2ee4687f76da4af6fd6049b76278c0e21381894",
                ":uwu:": "mxc://the-apothecary.club/f681fd13dd10c026aa95ce01d038d45b41e378bb",
                ":nice_neon:": "mxc://the-apothecary.club/d67439bddab298acb9b3a46250b2b32c3f9cd0d9",
                ":dissasociating:": "mxc://the-apothecary.club/02b32fd61a5e459ba9f6cadd5c87708e5c52f48e",
                ":minecraft:": "mxc://the-apothecary.club/3d3d043fa98e92e4e92f40b7ecde9ed5fa95d172",
                ":wink:": "mxc://the-apothecary.club/452b659c7bfb64e48864156539b28454f9968512",
                ":wave:": "mxc://the-apothecary.club/6b2a94cb20f94d2e54ed66dd230f60269bce264f",
                ":bam:": "mxc://the-apothecary.club/f3e2a0ed8a0ab64f3ec3ae9523eb042b56ea01fe",
                ":gay_dab:": "mxc://the-apothecary.club/2c5a6c39f31ea17b4e45abd1f74967f303729110",
                ":hildab:": "mxc://the-apothecary.club/296a353034e1c2fa2ddbbdd0e44e58fa70e20b80",
                ":headout_sponge:": "mxc://the-apothecary.club/4c15ef1e58d48401152c8024eefac9b817b1c0de",
                ":obama_prism:": "mxc://the-apothecary.club/f8677876b1332f6a2f4e44c823ad8d3d0cfce9d3",
                ":ban:": "mxc://the-apothecary.club/833cd4503fb6a2af69f6f64f9ecb4f242059d3d3",
                ":clippy:": "mxc://the-apothecary.club/GWQxXFuaEiAmOeNydXUYqnUE",
                ":cuthulu:": "mxc://the-apothecary.club/b45d235976ae5bbb59182cdbbdd218c42b4afe51",
                ":yarr:": "mxc://the-apothecary.club/f0f7a9e617bdb4efaf486cb005dd64a3bede7217",
                ":wonk:": "mxc://the-apothecary.club/54b99f26a644d05b127a46b94761e18f2d991a07",
                ":watch:": "mxc://the-apothecary.club/02a08f00af55a91e770d03a3bd786b7bfeb8409e",
                ":shoot:": "mxc://the-apothecary.club/ce415674215c69dad6e9e576134478b03dd4a8b9",
                ":unshoot:": "mxc://the-apothecary.club/866394643c8d54adb3d6fed5f50fdeaeeb3111cd",
                ":thumbsup:": "mxc://the-apothecary.club/23df0661e2ce0aecec231a88425db0f6f9e28570",
                ":thonk:": "mxc://the-apothecary.club/e19781a5b792a5ac59ad10a204f4874d43ed50cd",
                ":tentacle:": "mxc://the-apothecary.club/d104178b3f1ba047b1905d0f76f37d98d77f5a14",
                ":tentacle2:": "mxc://the-apothecary.club/7b7fbbd5242065337988e2d2cd71809c32e2dd8e",
                ":tentacle3:": "mxc://the-apothecary.club/1dc8ec57e59a8891fac5333a81a96260288e7527",
                ":tea:": "mxc://the-apothecary.club/e69575ef920c9ec066738a299663aa03c533f9db",
                ":tea2:": "mxc://the-apothecary.club/d5e764a2f6081e225ea5696fd03601462b24c16b",
                ":tea3:": "mxc://the-apothecary.club/f2072e64289e3a838a986768fc04b205314860f4",
                ":confused:": "mxc://the-apothecary.club/a80635b0b102466c6ede1e0bf1ca7b7619ca81c7",
                ":no_u:": "mxc://the-apothecary.club/f1a8a47f382e3cbb6c783ee9ead5610d6472c7bc",
                ":ok_boomer:": "mxc://the-apothecary.club/1b637368d0957066c9d100c9a46884e520ed74aa",
                ":rtx_off:": "mxc://the-apothecary.club/3871b33a666231c70715d04ce4114eddfdadbfc3",
                ":rtx_on:": "mxc://the-apothecary.club/226933f140a3f3c70c8013f1459831e97ea5d7db",
                ":windows_live:": "mxc://the-apothecary.club/68abc52f88b8643eac20755783b0b74632534f63",
                ":garlic_bread:": "mxc://the-apothecary.club/11c4b48f51daad7d0f11e01811874a291e203595",
                ":sweat:": "mxc://the-apothecary.club/638a2b8e9963358987278bb9d5cd2023b5c13b4e",
                ":content:": "mxc://the-apothecary.club/6c6258af588973b7bde79eb9da5a9285471d792b",
                ":heart:": "mxc://the-apothecary.club/667d4c12a54f272ed4012acd20b1bdf9cb271366",
                ":heart20:": "mxc://the-apothecary.club/854cb7b00c91e7dc28cf3335ce757f17e77260b8",
                ":heart30:": "mxc://the-apothecary.club/0858e008ede544e5f1c8982494532170fe0df0ec",
                ":heart50:": "mxc://the-apothecary.club/e29c868a61a44c1fd09e1e7284c7850f373698b3",
                ":reverse:": "mxc://the-apothecary.club/1be7dd72f5d202186ef76a7acff5fc1dfc8c31fa",
                ":crying:": "mxc://the-apothecary.club/ccae0229740cc13c56c1d1105bba1527322446c3",
                ":smile:": "mxc://the-apothecary.club/85e9056ee47067c0e086a97a46cc0197368eb609",
                ":smile2:": "mxc://the-apothecary.club/003a4f64a6aedc4d36f705d148c59a612edd9ea4",
                ":fear:": "mxc://the-apothecary.club/ad584b1ae79bb10c95d6269c18ad6e86e8c4ca80",
                ":sleepy:": "mxc://the-apothecary.club/089105022131e104e6f647474b93c8bc43895606",
                ":perfect:": "mxc://the-apothecary.club/40eeb957002a1da57dff8e5ad6eff27c0baadbde",
                ":metal:": "mxc://the-apothecary.club/74cf2fcb80c6907252119d0cd611cfe6ba2d12a2",
                ":whacky:": "mxc://the-apothecary.club/8c8c8bbd90bbaa8711f3d0c866091d54539e16a2",
                ":lemon:": "mxc://the-apothecary.club/8cbc2eb83dbf11346a7217b66c7928fc6e3b10ec",
                ":flex:": "mxc://the-apothecary.club/2434d0224a703e74a790428cd8ab37cdea5e1118",
                ":pray:": "mxc://the-apothecary.club/c879fa34fee8cf794e3028c9c22e3d475c015548",
                ":jebus:": "mxc://the-apothecary.club/OPpyiOazTWxvVHFcIpQKkvkO",
                ":illuminati:": "mxc://the-apothecary.club/6ebe8ec72e11bd6111f1a9786dcc2ae7a37c35dd",
                ":blob:": "mxc://the-apothecary.club/48435e4597f1d86d7080096f49f701efa48b4e62",
                ":ghost_boo:": "mxc://the-apothecary.club/8540c01d8f70ac5e4cd9a75d899817df44abb8a9",
                ":ghost_heart:": "mxc://the-apothecary.club/772f8cd4ed2e76c7f04ac33da12e5f9c8015ccf4",
                ":aperature:": "mxc://the-apothecary.club/00b3146bcb7a9bec9ac88bf5a2241768ff674afe",
                ":beg:": "mxc://the-apothecary.club/c136f63e58941fe8cc575228b4df59edc2594b96",
                ":pika_dance:": "mxc://the-apothecary.club/10397b9fbd786af63b0730964385073798b67e99",
                ":pat:": "mxc://the-apothecary.club/607d7833daafb2d3e2ac2b5a8dd9bcd9f2f21efc",
                ":bob_dance:": "mxc://the-apothecary.club/7b6bee346e5060ba914ac536cef7cb1fd670883d",
                ":walter_dance:": "mxc://the-apothecary.club/2a63f590fdf276bdb78685f29b7b9d7b58255606",
                ":think_wonky:": "mxc://the-apothecary.club/7d1de21e997349d6241445a6c9ddfc1634fa4907",
                ":flush_wonky:": "mxc://the-apothecary.club/f0f7629f2d88e362f5328732351821672cf3ec4b",
                ":gnome_parade:": "mxc://the-apothecary.club/a5ff8e79f6dc55bdbd876b2853426edaec646224",
                ":lick:": "mxc://the-apothecary.club/db687b27114a9e519c661d37f33de716c4c47448",
                ":oof_neon:": "mxc://the-apothecary.club/a1904a637480e0a6d8d5eeee9630f2272215f032",
                ":ping:": "mxc://the-apothecary.club/a7536f5b901623d646c0ac3530904ab3f642c6e8",
                ":recardo_gnome:": "mxc://the-apothecary.club/0a41837b4640803c254d0b436bb0d0196ee539d7",
                ":get_in_sponge:": "mxc://the-apothecary.club/787c078b8cef3c141ab8b93e4512ac894e95615c",
                ":wtf_neon:": "mxc://the-apothecary.club/59d2e5e9db4da76f52dc06bd82e06fd8ebcdf86b",
                ":wash:": "mxc://the-apothecary.club/c115945a6dd9f8fd0b2b0b67bf02ed79ce6b5f17",
                ":walter_bop:": "mxc://the-apothecary.club/5faacc557a221c07e1abb553fcc4032fdcedfb2e",
                ":sus_sponge:": "mxc://the-apothecary.club/17f1e0dde855e9cd491ceba3c494e8e80cab92b5",
                ":loading_dots:": "mxc://the-apothecary.club/26ec42db0a37bf8252cf8ab0c3078d01c6537b64",
                ":loading_windows:": "mxc://the-apothecary.club/088615425cb4ea276d4ba547853b5c9dd59357d2",
                ":mute:": "mxc://the-apothecary.club/079c5f19e2bd1a3f1a57fea00e3a38e4e3bb35eb",
                ":nom:": "mxc://the-apothecary.club/0864e6098c7eb8871ce7b91fa4eed03e5b3be5e1",
                ":lick2:": "mxc://the-apothecary.club/cf6c0c0497878b065c17867cbbab691798ad2a17",
                ":disc:": "mxc://the-apothecary.club/bc32c92ba6bb85608abe0c419ce7f9a71b0d539d",
                ":pizza:": "mxc://the-apothecary.club/25b4bc081a92b40a432968fec7d460e43377974a",
                ":tongue:": "mxc://the-apothecary.club/444b360e6bcf24f6a3cbef754249b4fd48dc82ef",
                ":sip:": "mxc://the-apothecary.club/513e138ea99f02c95a87bdb3ef1b0cdac714d0cc",
                ":uno_uwu:": "mxc://the-apothecary.club/539fe6a8dd27ffc48c0f8b2f1e71b35368b8cb09",
                ":dankjerry:": "mxc://the-apothecary.club/iEZsRcZXZhqCSaLMAhruaBgq",
                ":doubt:": "mxc://the-apothecary.club/bc1be4e1a0c36553ef7073a3c8b744f6ab0469a7",
                ":bruh:": "mxc://the-apothecary.club/9fa9d1b700ad589964fce587ea87951e4e65560f",
                ":bruh2:": "mxc://the-apothecary.club/85ca67799d655ca26f9d20ea6a6edcbd433dbe85",
                ":bruh_moment:": "mxc://the-apothecary.club/cb43dd535226f9b9a3076026b72a5d9c85277dc6",
                ":certified_bruh:": "mxc://the-apothecary.club/874bd059032d7ba12b12510e948c32a07d08f421",
            }
        },
    )


# function to send messages
async def bot_send_msg(client: AsyncClient, message: str, room: str):
    await client.room_send(
        room,
        message_type="m.room.message",
        content={"msgtype": "m.text", "body": message},
    )


asyncio.get_event_loop().run_until_complete(main())
