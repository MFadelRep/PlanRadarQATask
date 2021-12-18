import datetime


def timestamp_filename():
    date_stamp = str(datetime.datetime.now()).split('.')[0]
    date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
    file_name = date_stamp + ".png"
    return file_name

