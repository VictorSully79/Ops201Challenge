#!/usr/bin/env python
#Import Library
#script Name: eventLoggingToolPt1
#Author: Victor Sullivan    
#Date: 20211108
#Description of purpose: Python Script to Log Errors

import logging

randomStrings = ["this", "is", "so", "much", "fun", "for reelz", "yo", "I", "mean", "it"]

print("This is position 4: ", randomStrings[3])

print("This is positions 6 - 10: ", randomStrings[5:10])

print("Here is the old array: ", randomStrings)

randomStrings[6] = "onion"

print("Here is the new array: ", randomStrings)

logging.warning('Be Careful, you may get good at this!')
logging.info('Still working on skills')