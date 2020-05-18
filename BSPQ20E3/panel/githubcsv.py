"""Simple module with functions to get the csv files from the internet"""

import os, urllib, datetime, threading, time
import pandas as pd
from .logs import get_logger
from .models import Data, Auth_user
from .cache import Cache
from .sender import send
from mongoengine import *


# variable to avoid multiple operations on the same url
previous_url = None

connect('SoftwareP', host='127.0.0.1', port=27017)

def sendEmails():
    """
    -----------
    Description
    -----------
    Gets the recipients from the database and sends the notification emails

    """    
    users = Auth_user.objects()
    recipients = []
    if users.count()!= 0:
        for u in users:
            if u.is_active == True:
                recipients.append(u.email)
        if len(recipients)!=0 :
            send(recipients)
    get_logger().info(f"Function Complete!")


def get_csv_from_github(url="default", date=None):

    """
    -----------
    Description
    -----------
    Gets the .csv file from the specified url and the specified date, guaranteed only to work for the default 
    url. Raises "ValueError" for shady parameter-passing...

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

    global previous_url

    # default values for "url" and "date" parameters

    if url == "default":
        get_logger().debug("Default url to be used for csv extraction")
        url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    else:
        get_logger().debug(f"Specific url selected {url}")

        if type(url) is not str:
            get_logger().error(f"Type of supposed url \"{url}\" introduced (\"{type(url)}\") not valid")
            raise ValueError(f"Type of supposed url \"{url}\" introduced (\"{type(url)}\") not valid")

        if not url:
            get_logger().error(f"url \"{url}\" cannot be empty")
            raise ValueError(f"url \"{url}\" cannot be empty")


    if date is None:
        date = (datetime.datetime.now() - datetime.timedelta(days=1.0)).strftime("%d-%m-%Y") # adjust for US time...
        get_logger().debug("Default date to be used for csv extraction")

    else:
        get_logger().debug(f"Specific date selected {date}")

        if type(date) is not str:
            get_logger().error(f"Type of supposed date \"{date}\" introduced (\"{type(date)}\") not valid")
            raise ValueError(f"Type of supposed date \"{date}\" introduced (\"{type(date)}\") not valid")

        if not date:
            get_logger().error(f"Date \"{date}\" cannot be empty")
            raise ValueError(f"Date \"{date}\" cannot be empty")

        # check date format with datetime lib functionality

        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            get_logger().error(f"Date introduced \"{date}\" not valid for format dd-mm-yyyy")
            raise ValueError(f"Date introduced \"{date}\" not valid for format dd-mm-yyyy")

    # formatting of "date" to match file url

    date_formated = datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%m-%d-%Y")
    url_to_file = url + date_formated +".csv"
    get_logger().debug(f"Date formatted and url created: {url_to_file}")

    # get the .csv from the internets

    try:
        if (previous_url != url_to_file):
            csv_file_from_url = pd.read_csv(url_to_file)
            previous_url = url_to_file
            csv_file_from_url.to_csv("file.csv", index=False)
            os.system("mongoimport -d SoftwareP -c data --type csv --file file.csv --headerline")
            get_logger().debug(f"Successfully downloaded data for {date}")
            sendEmails()
    except urllib.error.HTTPError as error:
        get_logger().info(f"CSV file not found for this date yet: {date} -> {error}")
    except Exception as questionable_error:
        get_logger().warning(f"Something happened trying to input data into BD -> {questionable_error}")


def get_updated_csvs(seconds=3600, url="default"):

    """
    -----------
    Description
    -----------
    Loop intended to look up for new information in the url given for latest date, wrapper for function get_csv_from_github.
    Raises "ValueError" for shady parameter-passing...

    Parameters
    ----------
    seconds: integer
      number of seconds between csv lookups
      default value: 1h, 3600 seconds

    url: str
      raw.github where csv files are stored
      default value: see https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

    """

    if type(seconds) is not int:
        get_logger().error(f"Type of supposed seconds \"{seconds}\" introduced (\"{type(seconds)}\") not valid")
        raise ValueError(f"Type of supposed seconds \"{seconds}\" introduced (\"{type(seconds)}\") not valid")

    if seconds <= 0:
        get_logger().error(f"You can't set a this time of {seconds} seconds between iterations")
        raise ValueError(f"You can't set a this time of {seconds} seconds between iterations")

    if type(url) is not str:
        get_logger().error(f"Type of supposed url \"{url}\" introduced (\"{type(url)}\") not valid")
        raise ValueError(f"Type of supposed url \"{url}\" introduced (\"{type(url)}\") not valid")

    if not url:
        get_logger().error(f"url \"{url}\" cannot be empty")
        raise ValueError(f"url \"{url}\" cannot be empty")

    while True:

        get_csv_from_github(url=url, date=None)
        Cache().DATA = Data.objects()
        # Get distinct countries and dates from the data model entries
        # Purpose: filtering in the client side
        # Why: to not make a query every time a client enters livelog, this data remains constant until wait_time
        
        #Save countries and dates into text file in order to make possible the filtering
        saveToFile("countries.txt", Data.objects.distinct(field="Country_Region"), ":")
        dates = []
        for i in Data.objects.distinct(field="Last_Update"):
            yearMonthDay = i.split(" ")[0]
            dates.append(yearMonthDay)

        saveToFile("dates.txt", dates, "&")
        get_logger().info("COUNTRIES and DATES cached.")

        #sendEmails()
        wait_time = seconds - (time.perf_counter() % seconds)
        time.sleep(wait_time)


def loadSerializedCache():
    """
    Description
    -----------
    Gets the data stored in the specified files and stores it in the Cache object

    """
    Cache().COUNTRY_CHOICES = loadSerialFile("countries.txt", ":")
    Cache().DATE_CHOICES = loadSerialFile("dates.txt", "&")

def loadSerialFile(FILENAME, DELIM):
    """
    Description
    -----------
    Gets the data stored in a certain file and returns it as a list

    Parameters
    ----------
    file: str
      file path to read

    delim: str
      delimitator of the elements present in the file
    """
    try:
        FILELIST = open(FILENAME, "r").read().split(DELIM)
        LIST = [ ]
        for i in range(len(FILELIST)): 
            LIST.insert(i, (FILELIST[i], FILELIST[i]))
        LIST.insert(i, ("", "All"))
        return LIST

    except Exception as e:
        print(e)

def saveToFile(FILENAME, LIST, DELIM):
    """
    Description
    -----------
    Stores the data received as parameter in a text file

    Parameters
    ----------
    filename: str
      file path to write
    
    list: list
      list of strings to write

    delim: str
      delimitator for the elements
    """

    with open(FILENAME, 'w') as f:
        for item in LIST:
            f.write("%s%s" % (item, DELIM))
