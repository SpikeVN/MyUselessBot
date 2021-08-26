import main


async def send_message(channel, content, reply=False):
    if not reply:
        await main.execute_action(1, {"channel": channel, "message": content["message"]})
    else:
        await main.execute_action(3, {"channel": channel, "message": content["message"], "original_message": content["original_message"]})
