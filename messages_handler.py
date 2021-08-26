import command
import config_manager
import event


async def handle_message(message) -> None:
    # Don't reply to itself or other bots.
    if message.author.bot and (not config_manager.read_entry("affect_other_bot")):
        return
    if message.content.startswith(config_manager.read_entry("prefix")):
        args = command.separate_arguments(message.content)
        await command.execute_command(args[1], {"message": message})
    else:
        await event.handle_event(message)
