import os
import queue
import logging
import logging.handlers


# TREAT THIS LOGGER AS A ROOT (BASE) LOGGER
# AND DO NOT PROPAGATE LOG RECORDS TO THE ROOT LOGGER FROM THE LOGGING LIBRARY.
# ALL LOGGERS MUST USE THIS LOGGER AS AN ANCESTOR.
logger = logging.getLogger(os.environ["APP_LOGGER_ROOT_LOGGER_NAME"])
logger.propagate = False
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s",
)
stream_handler.setFormatter(formatter)

q = queue.Queue()
queue_handler = logging.handlers.QueueHandler(q)
queue_listener = logging.handlers.QueueListener(q, stream_handler)
queue_listener.start()
logger.addHandler(queue_handler)
