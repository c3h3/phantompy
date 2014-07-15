'''
Created on Jul 15, 2014

@author: c3h3
'''

import os

PACKAGE_PATH = os.path.dirname(__file__)

TEMP_HTML_RES_DIR = os.path.join(PACKAGE_PATH, "TempResHTML")

if not("TempResHTML" in os.listdir(PACKAGE_PATH)):
    os.mkdir(TEMP_HTML_RES_DIR)
    
def list_all_temp_files():
    return os.listdir(TEMP_HTML_RES_DIR)

def clean_all_temp_files():
    map(lambda xx:os.remove(os.path.join(TEMP_HTML_RES_DIR,xx)),
        list_all_temp_files())
