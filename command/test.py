import api


async def execute(data):
    await api.send_message(
        data["message"].channel,
        {
            "message": "```This is a test, performed py SpikeBonjour```\n *If you see this text, the test is successful*",
            "original_message": data["message"]
        },
        reply=True
    )
