###########################################################################################
# backbase test automation demonstration
#
# (C) 2018 by Sneha Mirajkar (sneha.mirajkar@gmail.com)
# Can be copied for any purposes, Please get prior approval.
#
# The logger defined below is used log all the events during the script execution.
# Default log level is set to DEBUG
###########################################################################################


import logging
logging.basicConfig(filename='log.txt',
                            filemode='a',
                            format='%(asctime)s %(levelname)s %(message)s',
                            level=logging.DEBUG)

