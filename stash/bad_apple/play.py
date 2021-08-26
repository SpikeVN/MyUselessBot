import json, time, os

input_file = open("stash/bad_apple/bad_apple.json").read()
animation_array = json.loads(input_file)


def get_frame(frame: int):
    output = ""
    for i in animation_array:
        if i["frame"] == frame:
            for j in i["content"]:
                output += j + "\n"
    return output
