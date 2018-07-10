**********************BACKBASE QA AUTOMATION DEMONSTRATION
The code is the designed used python2(WEBDRIVER+UNITTEST)
The design approach is modular to suit the custom needs.
Please follow the below mentioned steps to execute the testsuite.
1. The host machine used for the automation is ubuntu
2. Install pyhton2, selenium, and download the geckodriver
  sudo apt-get update -y && \
  sudo apt-get install python-pip wget curl -y && \
  sudo pip install --upgrade pip && \
  sudo pip install selenium
3.Downoad the geckodriver https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz ./
   Install using : tar -zxvf ./geckodriver-v0.20.1-linux64.tar.gz -C /usr/bin 
4. In the config.properties file add the following
  backbase_url=<hthe test URL given> [PLEASE DO NOT " " before and after values]
  computername=<company_name> [PLEASE DO NOT " " before and after values]
  introduction_date=<yyyy-mm-dd> [PLEASE DO NOT " " before and after values]
  discontinued_date=<yyyy-mm-dd> [PLEASE DO NOT " " before and after values]
  updatedcomputername=<updated_companyname> [PLEASE DO NOT " " before and after values]
5. 
 
