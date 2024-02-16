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

    print_message(args.uselog, "##teamcity[message text='Exception text' errorDetails='stack trace' status='ERROR']")

if __name__ == '__main__':
    main()
