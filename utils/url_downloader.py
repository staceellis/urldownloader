import os
import urllib.request
import logging
import subprocess
import pandas as pd

logger = logging.getLogger("url_downloader")

def check_conection():
    logger.info("CHECKING INTERNET CONNECTION")
    output=''
    try:
        p = subprocess.Popen('ping www.google.com', stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell = True)
        output, err = p.communicate()

    finally:
        if p is not None:
            try: p.kill()
            except: pass

    output = output.decode("utf-8")
    output = str(output)

    if 'Request timed out' in output or 'Ping request could not find host' in output:
        logger.info("BAD CONNECTION, PLEASE CHECK CONNECTION AND TRY AGAIN")
        return 0
    else:
        logger.info("CONNECTION ESTABLISHED")
        return 1

def download(source, destination, name, n_urls, p_urls):
    try:
        path = os.path.join(destination, name)
        urllib.request.urlretrieve(source, path)
        logger.info(str(p_urls) + " OF " + str(n_urls) + " IMAGES DOWNLOADED: " + name)
        return 1

    except (urllib.error.HTTPError):
        logger.warning("ERROR DOWNLOADING " + name + " , URL BROKEN: SKIPPING")
        return 0

def process_csv(csv):
    if csv.endswith('.csv') or csv.endswith('.CSV'):
        logger.info("READING CSV")
        table = pd.read_csv(csv)

        if table.empty:
            logger.error(".CSV EMPTY, PLEASE MAKE SURE CORRECT .CSV FILE IS USED")
            return 0

        if 'url' in table.columns:
           urls = table['url'].tolist()
           return(urls)

        else:
            logger.error("CANNOT FIND 'url' COLUMN IN CSV, PLEASE MAKE SURE CORRECT .CSV FILE IS USED")
            return 0

    else:
        logger.error("FILE NOT RECOGNIZED AS .CSV, PLEASE MAKE SURE .CSV FILE IS USED")
        return 0

def run(csv, destination):
    connection = check_conection()
    if connection == 1:
        urls = process_csv(csv)
        if urls == 0:
            return
        else:
            n_urls = len(urls)
            p_urls = 1
            for i in urls:
                try:
                    name = (i.split('/'))[-1]
                    download_urls = download(i, destination, name, n_urls, p_urls)
                    if download_urls == 1:
                        p_urls += 1
                except AttributeError:
                    logger.error("UNABLE TO INTERPRET 'url' COLUMN IN CSV, PLEASE MAKE SURE CORRECT .CSV FILE IS USED")
                    pass

            logger.info("DOWNLOAD COMPLETE")
            return
    else:
        return