import os


def is_charging(batteries: list):
    if "AC" in batteries:
        charging_status_file = open("/sys/class/power_supply/AC/online", "r")
        status = charging_status_file.readline().rstrip()
        if status == "0":
            charging = False
        else:
            charging = True
    else:
        charging = False
    return charging


def get_block(module_info: dict) -> dict:
    block = {"name": "battery"}
    batteries = os.listdir("/sys/class/power_supply")
    charging = is_charging(batteries)

    if "AC" in batteries:
        batteries.remove("AC")

    if charging:
        text = "Charging - "
    else:
        text = "Not charging - "

    for battery in batteries:
        try:
            battery_capacity = open(
                "/sys/class/power_supply/{}/capacity".format(battery)).readline().rstrip()
            text += "{}: {}% - ".format(battery, battery_capacity)
        except FileNotFoundError:
            text += "{battery} - "
    text = text[0:-3]

    block["full_text"] = text
    return block


if __name__ == "__main__":
    get_block(4)
