###########################################################################################
# backbase test automation demonstration
#
# (C) 2018 by Sneha Mirajkar (sneha.mirajkar@gmail.com)
# Can be copied for any purposes, Please get prior approval.
#
# The results.py the library function is written to log results of the def functions
#
###########################################################################################
def report_status(reportstring):
        try :
                from selenium import webdriver
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.ui import Select
                import datetime
                import time
                import os
                import re
        except ImportError:
                print ("failed to load the reporting module")
                exit()

        filename="reportfile.txt"
        f=open(filename, 'a')
        f.write(reportstring)
        f.write("\n")
        f.close()
