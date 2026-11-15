import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "level", choices=["ERROR", "WARN"]
    )
    parser.add_argument(
        "--max", type=int, default=1
    )
    parser.add_argument(
        "--short", action="store_true"
    )
    args = parser.parse_args(argv)
    text = open("server.log").read()
    count = text.count(args.level)
    if args.short:
        print(count)
    else:
        print(count, "allowed", args.max)
    if count > args.max:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
