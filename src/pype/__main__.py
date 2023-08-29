import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='execute a command')

    return parser.parse_args()


def main():
    args = parse_args()
    print(args)
