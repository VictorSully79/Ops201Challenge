#!/usr/bin/env python
#Import Library
#script Name: eventLoggingToolPt2
#Author: Victor Sullivan    
#Date: 20211109
#Description of purpose: Added rotated logs to part1

import logging
import time

from logging.handlers import RotatingFileHandler

def create_rotating_log(path):

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(path, maxBytes=20, backupCount=5)

    logger.addHandler(handler)

    for i in randomStrings[]:


    randomStrings = ["this", "is", "so", "much", "fun", "for reelz", "yo", "I", "mean", "it"]

print("This is position 4: ", randomStrings[3])

print("This is positions 6 - 10: ", randomStrings[5:10])

print("Here is the old array: ", randomStrings)

randomStrings[6] = "onion"

print("Here is the new array: ", randomStrings)

logging.warning('Be Careful, you may get good at this!')
logging.info('Still working on skills')



