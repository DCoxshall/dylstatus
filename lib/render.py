import json


def render(data: list) -> None:
    """Renders a list of blocks.
    One list should be one line to be displayed on the status-bar.
    One block is one dictionary of data."""
    print("[", end="")
    for i in range(len(data)):
        print(json.dumps(data[i]), end="")
        if i != len(data) - 1:
            print(',', end="")
    print("],", flush=True)
