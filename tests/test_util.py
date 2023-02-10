import logging
import time
from os import remove
import pytest
from terre.util.array import concat
from terre.util.day import now_stamp
from terre.util.day import now
from terre.util.day import days_later
from terre.util.day import LONG_FMT
from terre.util.day import SHORT_FMT
from terre.util.day import HOUR_FMT
from terre.util.day import is_same
from terre.util.day import is_after
from terre.util.day import is_before
from terre.util.day import is_same_or_after
from terre.util.day import is_same_or_before
from terre.util.day import date_format
from terre.util.fs import save_json
from terre.util.fs import save_file
from terre.util.fs import read_file
from terre.util.logger import init_logging


def test_concat():
    a = [
        "hello",
        "world",
        "do",
        "you",
        "like",
        "this?"
    ]

    b = [
        "yes",
        "I",
        "like",
        "this",
        "machine",
        8,
        8,
        6
    ]

    c = concat(a, b)
    assert (len(a) + len(b)) == len(c)


def test_day():
    assert len(str(now_stamp())) == 13
    assert len(now()) == 19
    assert len(now(SHORT_FMT)) == 10
    assert len(now(HOUR_FMT)) == 13
    assert len(now(LONG_FMT)) == 19
    a = "2020-02-08 12:00:22"
    assert days_later(a, 1).strftime(SHORT_FMT) == "2020-02-09"
    assert is_same(a, "2020-02-08")
    assert is_same(a, "2020-02-08 12:00:22", "second")
    assert is_same(a, "2020-02-08 12:00:22", "microseconds")
    assert is_before(a, "2020-02-09")
    assert is_same_or_before(a, "2022-02-08")
    assert is_after(a, "1997-01-02")
    assert is_same_or_after(a, "1082-03-31T22:23:08Z")
    assert date_format(a) == "2020-02-08"
    assert date_format(a, "%Y-%m-%d %H:%M:%S") == "2020-02-08 12:00:22"
    assert date_format(time.time())
    with pytest.raises(SyntaxError):
        date_format(a+"hello")


def test_save_json():
    filename = "test-file"
    json_str = {"hello": "world"}
    filepath = save_json(filename, json_str)

    assert filepath == filename + '.json'
    assert read_file(filepath) == '{\n"hello": "world"\n}'

    remove(filepath)


def test_save_file():
    filepath = "test-file"
    raw_text = "hello, world"

    assert save_file(filepath, raw_text) == filepath
    assert read_file(filepath) == raw_text

    remove(filepath)


def test_logging():
    init_logging()
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
    logger = logging.getLogger("default")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
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
                "filename": "test.log",
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
    init_logging(logger_config)
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
