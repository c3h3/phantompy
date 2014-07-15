'''
Created on Jul 15, 2014

@author: c3h3
'''

from .settings import PACKAGE_PATH, TEMP_HTML_RES_DIR
import os, commands 
import uuid


def get(url, filename=None):
    
    if filename==None:
        filename = uuid.uuid4().hex
    
    filepath = os.path.join(TEMP_HTML_RES_DIR, filename)
         
    current_dir = os.getcwd()
    
    os.chdir(PACKAGE_PATH)
    res_commands = commands.getoutput('phantomjs phantom_requests.coffee "%s" "%s"' % (url, filepath))
    print "res_commands = ",res_commands
    
    os.chdir(TEMP_HTML_RES_DIR)
    with open(filename, "r") as rf:
        res_text = rf.read()
    
    os.chdir(current_dir)
    
    res_dict = {}
    res_dict["res_commands"] = res_commands
    res_dict["res_text"] = res_text  
    res_dict["filepath"] = filepath 
    res_dict["filename"] = filename

    return res_dict 
    
    
    
    