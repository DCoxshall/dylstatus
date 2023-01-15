import datetime


def get_date() -> str:
    return datetime.datetime.today().strftime('%H:%M:%S %Y-%m-%d')


def get_block(module_info: dict) -> dict:
    block = {}
    block["full_text"] = get_date()
    # block["name"] = "time"
    return block
