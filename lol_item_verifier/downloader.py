"""downloader.py provides a simple way to download the latest data set or
a specified version.

It will download from the riot api and save it to the data set folder.

It may fail if it cannot reach the url or cannot save locally."""
from .data import save_data


def download_data_set():
    """Download the data set"""
    pass
