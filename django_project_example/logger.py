import logging

class Log:
    log_config = {}
    def __init__(self):
        self.log_config = {"filename":"mhealth_api.log",
                            "level":logging.DEBUG,
                            "format":"%(asctime)s - %(levelname)s - %(message)s",
                            "datefmt":"%Y-%m-%d %H:%M:%S"
                           }
