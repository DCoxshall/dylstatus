import psutil


def get_block(module_info):
    block = {"name": "RAM"}
    block["full_text"] = "RAM: " + str(psutil.virtual_memory().percent) + "%"
    return block


if __name__ == "__main__":
    mem = psutil.virtual_memory()
    print(mem)
