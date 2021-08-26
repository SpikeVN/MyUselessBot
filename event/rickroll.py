import api


async def handle(message):
    await api.send_message(
        message.channel,
        {
            "message": "Rick Astley sent you a gift!\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "original_message": message
        },
        reply=True
    )
