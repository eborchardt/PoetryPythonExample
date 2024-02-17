import argparse
import logging


def print_message(use_log, message):
    if use_log:
        logging.getLogger(__name__).info(message)
    else:
        print(message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uselog", action="store_true")
    args = parser.parse_args()

    if args.uselog:
        logging.basicConfig(level=logging.INFO)

    print_message(args.uselog, "##teamcity[inspectionType id='id' name='name' category='Medium Severity' description='description']")
    print_message(args.uselog, "##teamcity[inspection typeId='id' message='message 1' file='filename.c' line='1' SEVERITY='Medium Severity']")
    print_message(args.uselog, "##teamcity[inspection typeId='id' message='message 2' file='filename.c' line='2' SEVERITY='Medium Severity']")
    print_message(args.uselog, "##teamcity[inspection typeId='id' message='message 3' file='filename.c' line='3' SEVERITY='Medium Severity']")


if __name__ == '__main__':
    main()
