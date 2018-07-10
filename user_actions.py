###########################################################################################
# backbase test automation demonstration
#
# (C) 2018 by Sneha Mirajkar (sneha.mirajkar@gmail.com)
# Can be copied for any purposes, Please get prior approval.
#
# The user_actions.py contains the following def function
# Add computer, Search/READ computer details, Edit Computer and Delete computer.
###########################################################################################

#!/usr/bin/python

def add_computer(backbaseurl, computername, introdate, discontinuedate):
        try :
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.ui import Select
                from selenium.common.exceptions import NoSuchElementException
                from selenium.common.exceptions import NoAlertPresentException
		from logger import *
		from results import *
                import unittest, time, re
        except ImportError:
                print ("failed to load selenium module for Add_computers")
                exit()
        try :
                driver = webdriver.Firefox()
                driver.implicitly_wait(30)
                driver.get(backbaseurl)
		if driver.find_element_by_id("add"):
			logging.info("The backbase URL launched successfully")
			driver.find_element_by_id("add").click()
			driver.find_element_by_id("name").click()
			driver.find_element_by_id("name").clear()
			driver.find_element_by_id("name").send_keys(computername)
			driver.find_element_by_id("introduced").click()
			driver.find_element_by_id("introduced").clear()
			driver.find_element_by_id("introduced").send_keys(introdate)
			driver.find_element_by_id("discontinued").clear()
			driver.find_element_by_id("discontinued").send_keys(discontinuedate)
			Select(driver.find_element_by_id("company")).select_by_visible_text("Thinking Machines")
			driver.find_element_by_xpath("//option[@value='2']").click()
			driver.find_element_by_xpath("//input[@value='Create this computer']").click()
			driver.find_element_by_xpath('//div[@class="alert-message warning"]').click()
			validation=driver.find_element_by_xpath('//div[@class="alert-message warning"]').get_attribute("innerHTML")
			logging.info(validation)
			addcomputersuccess= "Computer "+ computername + " has been created" 
			logging.info(addcomputersuccess)
			if re.search (addcomputersuccess, validation):
				logging.info("Add computer executed successfully")
				successresult="TestCase for Add Computer: PASS"
				report_status(successresult)
				driver.quit()
				exit()	
			else: 
				logging.error("Add computer failed")
				failresult="TestCase for Add Computer: FAIL"
				report_status(failresult)
				driver.quit()
		else:
			logging.error("Unable to launch the Backbase URL")
			driver.quit()
    			exit()

        except :
		#logging.info("execution completed Add computer")
		pass


def read_search_computer(backbaseurl, computername, introdate, discontinuedate):
	try :
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.ui import Select
                from selenium.common.exceptions import NoSuchElementException
                from selenium.common.exceptions import NoAlertPresentException
		from logger import *
		from results import *
                import unittest, time, re
        except ImportError:
                print ("failed to load selenium module for read_search_computer")
                exit()
        try :
                driver = webdriver.Firefox()
                driver.implicitly_wait(30)
                driver.get(backbaseurl)
		if driver.find_element_by_id("add"):
			logging.info("The backbase URL launched successfully")
			driver.find_element_by_id("searchbox").click()
        		driver.find_element_by_id("searchbox").clear()
        		driver.find_element_by_id("searchbox").send_keys(computername)
        		driver.find_element_by_id("searchsubmit").click()
			driver.find_element_by_link_text(computername).click()
			driver.find_element_by_id("name").click()
			compname = driver.find_element_by_id("name").get_attribute("value")
			driver.find_element_by_id("introduced").click()
			intrdate=driver.find_element_by_id("introduced").get_attribute("value")
			driver.find_element_by_id("discontinued").click()
			discdate=driver.find_element_by_id("discontinued").get_attribute("value")
			logging.info("since the company is hardcoded, it will not be compared")
			logging.info("the values fetched as follows")
    			logging.info(compname)
			logging.info(intrdate)
			logging.info(discdate)
			if compname == computername and intrdate == introdate and discdate == discontinuedate :
				logging.info("the Read/search of the computer is successfully executed")
				successresult="TestCase for Read/search of the computer: PASS"
				report_status(successresult)
				driver.quit()
				exit()
			else:
				logging.info("the Read/search is unsuccessful")
				failresult="TestCase for Read/search of the computer: FAIL"
				report_status(failresult)
				driver.quit()
				exit()	
		
		else:
			logging.error("Unable to launch the Backbase URL")
			driver.quit()
    			exit()

        except :
                #logging.info("read_search_computer function completed")
		pass


def update_computer(backbaseurl, computername, updatedcomputername):
        try :
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.ui import Select
                from selenium.common.exceptions import NoSuchElementException
                from selenium.common.exceptions import NoAlertPresentException
		from logger import *
		from results import *
                import unittest, time, re
        except ImportError:
                print ("failed to load selenium module for update_computer")
                exit()
        try :
                driver = webdriver.Firefox()
                driver.implicitly_wait(30)
                driver.get(backbaseurl)
		if driver.find_element_by_id("add"):
			logging.info("The backbase URL launched successfully")
			driver.find_element_by_id("searchbox").click()
        		driver.find_element_by_id("searchbox").clear()
        		driver.find_element_by_id("searchbox").send_keys(computername)
        		driver.find_element_by_id("searchsubmit").click()
			driver.find_element_by_link_text(computername).click()
			driver.find_element_by_id("name").click()
			driver.find_element_by_id("name").clear()
			driver.find_element_by_id("name").send_keys(updatedcomputername)
			driver.find_element_by_xpath("//input[@value='Save this computer']").click()
			driver.find_element_by_xpath('//div[@class="alert-message warning"]').click()
			validation=driver.find_element_by_xpath('//div[@class="alert-message warning"]').get_attribute("innerHTML")
			logging.info(validation)
			addcomputersuccess= "Computer "+ updatedcomputername + " has been updated"
			logging.info(addcomputersuccess)
			if re.search (addcomputersuccess, validation):
				logging.info("Update computer executed successfully")
				successresult="TestCase for Update computer: PASS"
				report_status(successresult)				
				driver.quit()
				exit()
			else: 
				logging.error("Update computer failed")
				failresult="TestCase for Update computer: FAIL"
				report_status(failresult)
				driver.quit()
		else:
			logging.error("Unable to launch the Backbase URL")
			driver.quit()
    			exit()

        except :
		#logging.info( "execution for update computer completed")
		pass


def delete_computer(backbaseurl, updatedcomputername):
        try :
                from selenium import webdriver
                from selenium.webdriver.common.by import By
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.support.ui import Select
                from selenium.common.exceptions import NoSuchElementException
                from selenium.common.exceptions import NoAlertPresentException
		from logger import *
		from results import *
                import unittest, time, re
        except ImportError:
                print ("failed to load selenium module for Add_computers")
                exit()
        try :
                driver = webdriver.Firefox()
                driver.implicitly_wait(30)
                driver.get(backbaseurl)
		if driver.find_element_by_id("add"):
			logging.info("The backbase URL launched successfully")
			driver.find_element_by_id("searchbox").click()
        		driver.find_element_by_id("searchbox").clear()
        		driver.find_element_by_id("searchbox").send_keys(updatedcomputername)
        		driver.find_element_by_id("searchsubmit").click()
			driver.find_element_by_link_text(updatedcomputername).click()
			driver.find_element_by_xpath("//input[@value='Delete this computer']").click()
			driver.find_element_by_xpath('//div[@class="alert-message warning"]').click()
			validation=driver.find_element_by_xpath('//div[@class="alert-message warning"]').get_attribute("innerHTML")
			logging.info(validation)
			addcomputersuccess= "Computer has been deleted"
			logging.info(addcomputersuccess)
			if re.search (addcomputersuccess, validation):
				logging.info("Delete computer executed successfully")
				successresult="TestCase for Delete computer: PASS"
				report_status(successresult)				
				driver.quit()
				exit()
			else: 
				logging.error("Delete computer failed")
				failresult="TestCase for Delete computer: FAIL"
				report_status(failresult)
				driver.quit()
		else:
			logging.error("Unable to launch the Backbase URL")
			driver.quit()
    			exit()

        except :
		#logging.info( "execution for delete computer completed")
		pass




	
