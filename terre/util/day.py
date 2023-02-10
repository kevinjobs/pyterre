from typing import Union
from time import time
from datetime import datetime
from datetime import timedelta


SHORT_FMT = r"%Y-%m-%d"
HOUR_FMT = r"%Y-%m-%d-%H"
LONG_FMT = r"%Y-%m-%d %H:%M:%S"
FULL_FMT = r"%Y-%m-%dT%H:%M:%SZ"
INT_FMT = r"%Y%m%d%H%M%S"
UNION_DATE = Union[str, float]


def now_stamp():
    return int(round(time() * 1000))


def now(fmt=LONG_FMT):
    return datetime.now().strftime(fmt)


def date_format(dt: UNION_DATE, fmt=SHORT_FMT):
    return _convert_to_datetime(dt).strftime(fmt)


def days_later(dt: UNION_DATE, days: int) -> datetime:
    d = _convert_to_datetime(dt)
    return d + timedelta(days)


def is_same(a: UNION_DATE, b: UNION_DATE, gradation="day") -> bool:
    return _delta(a, b, gradation) == 0


def is_before(a: UNION_DATE, b: UNION_DATE, gradation="day") -> bool:
    return _delta(a, b, gradation) < 0


def is_same_or_before(a: UNION_DATE, b: UNION_DATE, gradation="day") -> bool:
    return _delta(a, b, gradation) <= 0


def is_after(a: UNION_DATE, b: UNION_DATE, gradation="day") -> bool:
    return _delta(a, b, gradation) > 0


def is_same_or_after(a: UNION_DATE, b: UNION_DATE, gradation="day") -> bool:
    return _delta(a, b, gradation) >= 0


def _delta(a: UNION_DATE, b: UNION_DATE, gradation) -> int:
    aa = _convert_to_datetime(a)
    bb = _convert_to_datetime(b)
    delta = aa - bb
    if gradation == "day":
        return delta.days
    elif gradation == "second":
        return delta.seconds
    elif gradation == "microseconds":
        return delta.microseconds


def _convert_to_datetime(dt: UNION_DATE):
    if isinstance(dt, str):
        length = len(dt)
        if length == 10:
            return datetime.strptime(dt, SHORT_FMT)
        elif length == 19:
            return datetime.strptime(dt, LONG_FMT)
        elif length == 20:
            return datetime.strptime(dt, FULL_FMT)
        else:
            raise SyntaxError(r"the format of param datetime must be one of 2022-02-02 || 2022-02-02 02:02:02 || "
                              r"2022-02-02T02:02:02Z")
    elif isinstance(dt, float):
        return datetime.fromtimestamp(dt)
