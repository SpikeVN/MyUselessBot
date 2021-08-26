import config_manager

import command.test
import command.bad_apple

cmds = {
    "bad_apple": "Prints out an bad apple ascii art video in the current chat.",
    "test": "Tests if the bot works or not"
}


def search_command(name: str):
    global cmds
    if cmds.__contains__(name):
        return True, {name: cmds[name]}
    else:
        return False, {}


async def execute_command(name: str, data: dict) -> None:
    if name == "test":
        await command.test.execute(data)


def separate_arguments(input: str) -> list:
    output = []
    if input[0] == config_manager.read_entry("prefix"):
        current_arg = ""
        for i in input:
            if i == " " or i == config_manager.read_entry("prefix"):
                output.append(current_arg)
                current_arg = ""
            else:
                current_arg += i
        output.append(current_arg)
        output[0] = config_manager.read_entry("prefix")
        return output
    else:
        raise ValueError(f"{input} is not a command")
