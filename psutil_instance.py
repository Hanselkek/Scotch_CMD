import os
import psutil

def get_mem_usage_by_app():
    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]/2.**30

    return memoryUse