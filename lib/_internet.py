import socket

hostname = "google.com"


def internet_connected():
    '''If internet is connected, return local IP address. If not, return "Not Connected"'''
    try:
        s = socket.create_connection((hostname, 80), timeout=0.5)
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        pass
    return "Not Connected"


def get_local_ip():
    addr = socket.gethostbyname(socket.gethostname())
    return addr


def get_block(module_info: dict):
    block = {"name": "internet"}

    ip = internet_connected()
    block["full_text"] = ip

    if ip == "Not Connected":
        block["color"] = "#FF0000"
    else:
        block["color"] = "#00FF00"

    return block
