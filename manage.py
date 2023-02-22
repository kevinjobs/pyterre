from os import path
from argparse import ArgumentParser
from terre.util.day import now_stamp
from terre.config import STORE_PATH


def args():
    ap = ArgumentParser()
    ap.add_argument("cmd", help="input command to run.")
    ap.add_argument("-r", "--ramper", help="ramper name. use 'all' to run all rampers.")
    return ap.parse_args()


def run_ramper(name: str):
    from rampers.hupu import HupuRamper
    from rampers.zhihu import ZhihuRamper
    from rampers.ithome import IthomeRamper

    rampers = {
        "hupu": HupuRamper,
        "zhihu": ZhihuRamper,
        "ithome": IthomeRamper,
    }

    if name == "all":
        for k, _ in rampers.items():
            filepath = path.join(STORE_PATH, f"{k}-{now_stamp()}")
            rampers[k]().save_json(filepath)
        return

    filepath = path.join(STORE_PATH, f"{name}-{now_stamp()}")
    rampers.get(name)().save_json(filepath)


if __name__ == "__main__":
    argv = args()
    cmd = argv.cmd
    ramper = argv.ramper

    if cmd == "run":
        run_ramper(ramper)
