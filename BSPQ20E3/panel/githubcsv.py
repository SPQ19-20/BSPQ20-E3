"""Simple module with functions to get the csv files from the internet"""

import os, urllib, datetime, threading, time
import pandas as pd
from .logs import get_logger


def get_csv_from_github(url=None, date=None):

    """
    Description
    -----------
    Gets the .csv file from the specified url and the specified date, guaranteed only to work for the default 
    url. Raises "ValueError" when invalid data formats are introduced.

    Parameters
    ----------
    url: str
      raw.github where csv files are stored
      default value: see https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

    date: str
      date format "dd-mm-yyyy"
      default value: today's date (adjusted for US time)

    return: leaves a "file.csv" with updated data from the date given

    """

    # default values for "url" and "date" parameters

    if url is None:
        get_logger().debug("Default url to be used for csv extraction.")
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"

    if date is None:
        get_logger().debug("Default date to be used for csv extraction.")
        date = (datetime.datetime.now() - datetime.timedelta(days=1.0)).strftime("%d-%m-%Y") # adjust for US time...
    else:
        get_logger().debug(f"Specific date selected {date}.")
        if type(date) is not str:
            get_logger().warning(f"Type of supposed date \"{date}\" introduced (\"{type(date)}\") not valid")
            raise ValueError(f"Type of supposed date \"{date}\" introduced (\"{type(date)}\") not valid")
        # check date format with datetime lib functionality
        try:
            datetime.datetime.strptime(date, "%d-%m-%y")
        except ValueError:
            get_logger().warning(f"Date introduced \"{date}\" not valid for format dd-mm-yyyy")
            raise ValueError(f"Date introduced \"{date}\" not valid for format dd-mm-yyyy")

    # formatting of "date" to match file url

    date_formated = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%m-%d-%Y")
    url_to_file = url + date_formated +".csv"

    # get the .csv from the internets

    try:
        csv_file_from_url = pd.read_csv(url_to_file)
        csv_file_from_url.to_csv("file.csv", index=False)
        get_logger().debug(f"Successfully downloaded data for {date}.")
        os.system("mongoimport -d SoftwareP -c data --type csv --file ../file.csv --headerline")
    except urllib.error.HTTPError as error:
        get_logger().info(f"File not found for this date yet: {date} -> {error}.")
    except Exception as questionable_error:
        get_logger().info(f"Something happened trying to input data into BD -> {questionable_error}.")


def get_updated_csvs(seconds=3600, url=None):

    """
    Description
    -----------
    Loop intended to look up for new information in the url given for latest date, wrapper for function get_csv_from_github.
    Raises "ValueError" when 0 or negative wait-time is introduced.

    Parameters
    ----------
    seconds: integer
      number of seconds between csv lookups
      default value: 1h, 3600 seconds

    url: str
      raw.github where csv files are stored
      default value: see https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

    date: str
      date format in "dd-mm-yyyy"
      default value: today's date (adjusted for US time)

    """

    if seconds <= 0:
        get_logger().error(f"You can't set a negative time of {seconds} between iterations")
        raise ValueError(f"You can't set a negative time of {seconds} between iterations")

    while True:
        get_csv_from_github(url=url, date=None)
        wait_time = seconds - (time.perf_counter() % seconds)
        time.sleep(wait_time)
