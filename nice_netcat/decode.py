#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="nice netcat")
    parser.add_argument('-f', "--file", required=True)

    args = parser.parse_args()


    with open(args.file) as f:
        for r in [x.strip() for x in f.readlines()]:
            sys.stdout.write(chr(int(r)))
