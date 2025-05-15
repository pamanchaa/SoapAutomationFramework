'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
from utils.logger_utils import  logger
from utils.xml_beautify import beautify_xml

def print_response_data(response):
    
    logger.info(f">>>##########################################################")
    logger.info(f"RESPONSE DETAILS::")
    beautify_response = beautify_xml(response.text)  
    logger.info(f"RESPONSE TEXT = \n{beautify_response}")
    #/////////////////////////////////////////////////////////////////////
    logger.info(f"STATUS CODE = {response.status_code}")    
    logger.info(f"<<<##########################################################")