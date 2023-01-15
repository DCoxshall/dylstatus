import psutil
import subprocess


def get_remaining_time(battery: psutil._common.sbattery) -> str:
    minutes, seconds = divmod(battery.secsleft, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def get_battery_percentage(battery: psutil._common.sbattery) -> str:
    return str(round(battery.percent, 1)) + "%"


def get_state(battery: psutil._common.sbattery) -> str:
    if battery.power_plugged:
        return "Plugged in"
    else:
        return "Not plugged in"


def get_block(module_info: dict) -> dict:
    battery = psutil.sensors_battery()
    block = {}
    text = "{percent} - {time} - {state}".format(percent=get_battery_percentage(
        battery), time=get_remaining_time(battery), state=get_state(battery))
    block["full_text"] = text
    block["name"] = "battery"
    return block
