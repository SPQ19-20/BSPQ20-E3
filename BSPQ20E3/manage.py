#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os, sys, urllib, datetime, threading, time
import pandas as pd


def get_csv_from_github(url=None, date=None):

    """
    url: raw.github where csv files are stored

        default value: see https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

    date -> dd-mm-yyyy

        default value: today's date

    return -> leaves a "file.csv" with updated data from the date given
    """

    # default values for "url" and "date" parameters

    if url is None:
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    if date is None:
        date = datetime.datetime.now().strftime("%d-%m-%Y")

    # formatting of "date" to match file url

    date_formated = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%m-%d-%Y")
    url_to_file = url + date_formated +".csv"

    # get the .csv from the internets

    try:
        csv_file_from_url = pd.read_csv(url_to_file)
        csv_file_from_url.to_csv("file.csv")
        print(f"get_csv_from_github -> Successfully downloaded data...")
    except urllib.error.HTTPError as csv_not_found:
        print(f"get_csv_from_github -> File not found for this date yet {date} -> {csv_not_found}")
    except Exception as error:
        print(f"get_csv_from_github -> Sth weird happenned -> {error}")


def get_updated_csvs(seconds=3600, url=None, date=None):

    """
    seconds: number of seconds between csv lookups

        default value: 1h, 3600 seconds

    url: raw.github where csv files are stored

        default value: see https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

    date -> dd-mm-yyyy

        default value: today's date
    """

    while True:
        get_csv_from_github(url=url, date=date)
        wait_time = seconds - (time.perf_counter() % seconds)
        time.sleep(wait_time)


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

    # start a thread responsible for regular updates of application

    timerThread = threading.Thread(target=get_updated_csvs)
    timerThread.daemon = True
    timerThread.start()

    main()
