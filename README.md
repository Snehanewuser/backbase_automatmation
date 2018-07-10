**********************BACKBASE QA AUTOMATION DEMONSTRATION

**********************The purpose of this automation suite is to Add a computer, read the details of the computer, Update the values of the computer details and delete computer [CRUD opeerations, using company as a constant value, while everything else is configurable]

The code is the designed using python2(WEBDRIVER+UNITTEST)

The design approach is modular to suit the custom needs.
Please follow the below mentioned steps to execute the testsuite.
1. The host machine used for the automation is ubuntu
2. Install pyhton2, selenium, and download the geckodriver
    sudo apt-get update -y && \
    sudo apt-get install python-pip wget curl -y && \
    sudo pip install --upgrade pip && \
    sudo pip install selenium
3. Downoad the geckodriver https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz ./
    Install using : tar -zxvf ./geckodriver-v0.20.1-linux64.tar.gz -C /usr/bin 
4. In the config.properties file add the following
    backbase_url=<hthe test URL given> [PLEASE DO NOT " " before and after values]
    computername=<company_name> [PLEASE DO NOT " " before and after values]
    introduction_date=<yyyy-mm-dd> [PLEASE DO NOT " " before and after values]
    discontinued_date=<yyyy-mm-dd> [PLEASE DO NOT " " before and after values][make sure the discontinued_date is greater than      
    introduction_date]
    updatedcomputername=<updated_companyname> [PLEASE DO NOT " " before and after values]
5. The suite is designed using python selenium (using find_element_id), making it easy to maintain and in places where id/css is 
   not working xpath is used to do the operations.
6. The main.py uses a configparser to read values from the config.prop file and pass them to the functions for executions.
7. For uniqueness of the computer name, after reading the value from config.prop, a random value is added.
8. The company chosen is hard coded, hence keeping it simple, 
9. The user_actions.py file, holds all the function definitions, that accept input args and execute accordingly.
    Add_computer: accepts the computerdataurl, computername, introduction date, distcontiued date, Adds the computer and validates 
    the success message.
    read_search_computer: accepts the computerdataurl, computername, introduction date, distcontiued date, searches the computer 
    navigates to the details page,compares with the values fetched and fed and returns the result.
    Update_computer : accepts the computerdataurl, computername, updatedcomputername, searches the computername, navigates to the 
    computer page, updates the computer name and validates the success message upon saving.
    Delete_computer: accepts the computerdataurl updatedcomputername, searches the computername, navigates to the 
    computer page, deletes the computer and validates the success message.
 10.The logger.py has the logger defined with basic config to capture all debug logging events and also the function execution    
     logs in the log.txt file 
 11. The results.py has the function for the results to be stored in the very basic format as PASS or FAIL in reportfile.txt.
 
 NOTE: Also found in the git repo is teh XLS for the manual testcase, the manual testcase sheet has some findings in form of BUGS/ENHANCEMENTS
 
