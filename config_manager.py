import json

default_value = {
    "token": "",
    "prefix": "!"
}


def change_entry(name: str, value):
    old_config_file = open("config.json")
    config = old_config_file.read()
    old_config_file.close()
    if default_value.__contains__(name):
        config[name] = value
    else:
        print("Warning: Unknown config entry is tried to be accessed.")
    config_file = open("config.json", "w")
    config_file.write(config)


def read_entry(name: str):
    config_file = open("config.json")
    output = json.loads(config_file.read())
    if output.__contains__(name):
        return output[name]
