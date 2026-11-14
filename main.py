"""Souffle pancake photo courier, second seating.

Delivers entry.png — jiggly Japanese souffle pancakes dusted with
icing sugar, honey dripping down the sides, whipped cream and
strawberries — byte-for-byte into the output directory. Copy only.
"""

import os
import shutil

SOUFFLE_NAME = "entry.png"
SOUFFLE_ENV_VAR = "MAKEFUN_OUTPUT_DIR"
SOUFFLE_DEFAULT = "/output"


def souffle_out_path():
    folder = os.environ.get(SOUFFLE_ENV_VAR, SOUFFLE_DEFAULT)
    return os.path.join(folder, SOUFFLE_NAME)


def souffle_in_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOUFFLE_NAME)


def deliver_souffle():
    src = souffle_in_path()
    if not os.path.isfile(src):
        raise SystemExit(f"souffle pancake photo missing: {src}")
    if os.path.getsize(src) == 0:
        raise SystemExit(f"souffle pancake photo empty: {src}")
    dst = souffle_out_path()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    size_out = os.path.getsize(dst)
    print(f"souffle pancake photo delivered to {dst} ({size_out} bytes)")


if __name__ == "__main__":
    deliver_souffle()
