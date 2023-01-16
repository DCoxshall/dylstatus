#!/usr/bin/env python3
import time
from io import StringIO
import sys
import json

from lib import render, _time, _cpu, _battery, _internet
from lib.io_poll import attemptRead


def setup() -> dict:
    # Returns a dictionary with the modules to be rendered as the keys, and the
    # individual settings for each one as the values in the form of a second
    # layer of nested dictionaries. If no settings are specified for a given
    # key, value will be an empty string
    try:
        config_file = open("/home/dylan/.config/dylstatus/config.txt", "r")
        lines = [line for line in config_file.readlines() if (
            not line.startswith("//")) and line != "\n"]
        config_file.close()
        config_data = {line.rstrip(): "" for line in lines}

    except FileNotFoundError:
        config_data = {"time": "", "battery": "", "cpu_usage": ""}

    return config_data


def run(active_modules: dict):
    print("{\"version\": 1, \"click_events\": true}")
    print("[[],")

    # time should be the last module to be called, to ensure accuracy
    while True:
        blocks = []
        if "cpu_usage" in active_modules:
            blocks.append(_cpu.get_block(active_modules["cpu_usage"]))
        if "battery" in active_modules:
            blocks.append(_battery.get_block(active_modules["battery"]))
        if "internet" in active_modules:
            blocks.append(_internet.get_block(active_modules["internet"]))
        if "time" in active_modules:
            blocks.append(_time.get_block(active_modules["time"]))

        render.render(blocks)

        time.sleep(.125)


if __name__ == "__main__":
    active_modules = setup()
    run(active_modules)
