import logging
import sys
import time

from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
from com.base.watchdog import print1
"""
监控指定目录下文件（文件夹）变更情况
"""



def doSomething():
    print(print1())
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
