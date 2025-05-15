'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
from utils.logger_utils import  logger

def print_request_data(url,header,body):
    
    logger.info(f">>>##########################################################")
    logger.info(f"REQUEST DETAILS::")
    logger.info(f"URL = {url}")
    #////////////////////////////////////////////////////////////////////////////
    logger.info(f"HEADERS = {header}")
    #////////////////////////////////////////////////////////////////////////////
    logger.info(f"PAYLOAD = \n{body}")
    logger.info(f"<<<##########################################################")
    