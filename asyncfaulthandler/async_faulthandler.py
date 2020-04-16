import asyncio
import sys
import threading
from time import sleep


def _stacktraces(loop, interval, repeat, file=sys.stderr):
    i = 0
    while True:
        sleep(interval)
        print(f"Async Tasks Dump #{i}:", file=file)
        i += 1
        for task in asyncio.all_tasks(loop):
            task.print_stack(file=file)
        if not repeat:
            return


def start_tracing(loop, interval, repeat=True, file=sys.stderr):
    threading.Thread(target=_stacktraces, args=(loop, interval, repeat, file,)).start()
