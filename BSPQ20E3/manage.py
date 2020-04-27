#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os, sys, threading
from panel.githubcsv import get_updated_csvs
from panel.logs import get_logger, change_logger


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BSPQ20E3.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":

    # start a thread for regular updates on csv info

    if ("runserver" in sys.argv):

        # logger set up to display even debug messages
        change_logger(nlevel=10)

        timerThread = threading.Thread(name="csv-getter", target=get_updated_csvs, daemon=True)
        timerThread.start()
        get_logger().debug("Csv-getter thread started.")

    main()
