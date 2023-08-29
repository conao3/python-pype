import argparse
import os
import pathlib
import shutil
import sys

import jinja2

env = jinja2.Environment(undefined=jinja2.StrictUndefined)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='execute a command')
    parser.add_argument('-n', default=False, action='store_true', help='-n')

    return parser.parse_args()


def main():
    args = parse_args()
    template_str = (pathlib.Path(__file__).parent / 'template.py.jinja').read_text()

    dct = {
        'arg_e': args.e,
        'arg_n': args.n,
    }
    template = env.from_string(template_str)
    print(template.render(dct), flush=True)
    os.close(1)

    with open('tmp.fifo', 'w') as f:
        shutil.copyfileobj(sys.stdin, f)
