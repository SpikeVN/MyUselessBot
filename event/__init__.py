import event.rickroll


async def handle_event(message):
    if [
        "rickroll", "rick", "astley", "never gonna give you up", "give you up",
        "let you down", "tell you lie", "dessert you", "tell you lie", "say goodbye",
        "you know the rules and so do i", "what i'm thinking of", "you wouldn't get this from any other guy"
    ].__contains__(message.content):
        await rickroll.handle(message)
