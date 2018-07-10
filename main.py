###########################################################################################
# backbase test automation demonstration
#
# (C) 2018 by Sneha Mirajkar (sneha.mirajkar@gmail.com)
# Can be copied for any purposes, Please get prior approval.
#
# The class backbase_qa executes all the CRUD operations through function calls
# The class backbase_qa reads the configurations from config.prop file and passes
# to the functions as args.
###########################################################################################


import unittest
import time
import requests
import user_actions
from logger import *
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import ConfigParser

class backbase_qa(unittest.TestCase):

	@classmethod
    	def setUpClass(self):
		self.driver=webdriver.Firefox()
		logging.info("starting with execution of the backbase automation")
        	config = ConfigParser.ConfigParser()
		# read the custom values from the config.properties file.
        	config.read('config.properties')
        	self.backbaseurl = config.get('config_values', 'backbase_url')
        	self.computername = config.get('config_values', 'computername')+ ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(3)])
        	self.introdate = config.get('config_values', 'introduction_date')
        	self.discontinuedate = config.get('config_values', 'discontinued_date')
        	self.updatedcomputername = config.get('config_values', 'updatedcomputername')
		
	
	def test_addcomputer(self):
		user_actions.add_computer(self.backbaseurl, self.computername, self.introdate, self.discontinuedate)
		user_actions.read_search_computer(self.backbaseurl, self.computername, self.introdate, self.discontinuedate)
		user_actions.update_computer(self.backbaseurl, self.computername, self.updatedcomputername)
		user_actions.delete_computer(self.backbaseurl, self.updatedcomputername)
	
	def tearDown(self):
        	self.driver.quit()
	
if __name__ == "__main__":
    unittest.main()
	
	
