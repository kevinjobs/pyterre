import logging
import logging.config
from os import path
from terre.config import LOGS_PATH
from terre.util.day import now
from terre.util.day import HOUR_FMT


logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - [%(levelname)s] %(message)s"
        },
        "full": {
            "format": "%(asctime)s - %(filename)s:%(lineno)d - %(name)s [%(levelname)s] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "full",
            "filename": f"{path.join(LOGS_PATH, now(HOUR_FMT)+'.log')}",
            "maxBytes": 1024 * 1024 * 20,  # 20mb
            "backupCount": 20,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "default": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file"]
    }
}


def init_logging(_config=None) -> None:
    conf = logger_config
    if isinstance(_config, dict):
        conf = _config
    logging.config.dictConfig(conf)
