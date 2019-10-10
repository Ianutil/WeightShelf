#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""

import logging
import time
import os

LOG_File = "log/log.log"

if not os.path.exists(LOG_File):
    os.makedirs("log")

logging.basicConfig(filename=LOG_File, filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)

def log(text):
    logging.basicConfig()
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

def e(text):
    logging.error(text)

def d(text):
    logging.error(text)


if __name__ == "__main__":
    print("Hello World")