import psutil

# might return "45%", for instance
def get_cpu_usage() -> str:
    return str(psutil.cpu_percent()) + "%"
