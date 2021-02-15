"""
CLI implementation to download URLs From Transpower Defects Dashboard

To download using exported CSV:
    >> python CLI.py [DESTINATION] [.CSV]
example:
    >> python CLI.py c:\images c:\export.csv
    >> python CLI.py ~/images/ ~/export.csv/
"""

import sys
import os
from datetime import datetime
import click
import logging
from utils import url_downloader

__version__ = '0.0.1'

logger = logging.getLogger("url_downloader")

@click.command()
@click.argument("destination", type=click.Path(exists=True))
@click.argument("csv", type=click.Path(exists=True))

def main_cli(csv:str, destination:str):

    logger.setLevel(logging.INFO)
    logger.propagate = False

    fmt = '%(asctime)s.%(msecs)03d %(module)s %(lineno)d %(levelname)s: %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    if not os.path.exists("logs"):
        os.mkdir("logs")

    filehandler = logging.FileHandler(f"logs/{datetime.now().strftime('%Y%m%d%H%M%S')}_url_downloader.log")
    filehandler.setLevel(logging.INFO)
    filehandler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)

    url_downloader.run(os.path.abspath(csv), os.path.abspath(destination))

if __name__ == '__main__':
    main_cli()