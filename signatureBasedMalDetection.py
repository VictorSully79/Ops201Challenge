# signatureBasedMalDetection
# Victor Sullivan
# 20211116
# Detection and remediation of malware is the core function of many security products, and an optional secondary feature on others like perimeter firewalls and proxy servers.

import os
import hashlib,datetime
from time import sleep

def get_hashcode():
    folder_name = input("which folder do you want to scan? ")
    output_search(folder_name)

# Getting current time stamp


def get_time():
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%b-%d-%Y-%H:%M:%S")
    return timestampStr

# Outputting final results

def output_search(pt):
    abs_path = os.path.abspath(pt)
    print("Timestamp            File-name            Hash-code             Size     File-path")
    for root, dirs, files in os.walk(abs_path):
            for filo in files:
                try:
                    full_path= os.path.join(root, filo)
                    hash_value = hash_co(full_path)
                    print(f"{get_time()} {filo} {hash_value}   {os.path.getsize(full_path)}   {full_path}")
                    sleep(1.5)
                except Exception as msg:
                    print(msg)
                    continue

# Getting the hash code#

def hash_co(fn):
    md_hash = hashlib.md5()
    with open(fn, "rb") as f:
        for byte_block in iter(lambda: f.read(4896),b""):
            md_hash.update(byte_block)
    f.close()
    return md_hash.hexdigest()

get_hashcode()