import psutil

# might return "45%", for instance


def get_cpu_usage() -> str:
    return str(psutil.cpu_percent()) + "%"


def get_block(module_info: dict) -> str:
    block = {}
    block["name"] = "cpu_usage"
    block["full_text"] = "CPU: {}".format(get_cpu_usage())
    return block
