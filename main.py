import json
import discord
from discord import message

import messages_handler

token_file = open("config.json", "r")
token = json.loads(token_file.read())["token"]
token_file.close()

bot = discord.Client()


@bot.event
async def on_ready():
    print("Bot is ready and online.")


@bot.event
async def on_message(a_message):
    await messages_handler.handle_message(a_message)


async def execute_action(action: int, data: dict) -> None:
    if action == 1:  # 1 = send_message
        await data["channel"].send(data["message"])
    if action == 2:  # 2 = delete_message
        await data["channel"].delete(message)
    if action == 3:  # 3 = reply_message
        await data["original_message"].reply(data["message"])


if __name__ == "__main__":
    bot.run(token)
