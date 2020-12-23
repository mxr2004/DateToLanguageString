import logging
import subprocess
import sys


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Installing requirements")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


if __name__ == '__main__':
    main()
