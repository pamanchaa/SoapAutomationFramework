'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
import requests
import time
import random

from config.config import BASE_URL, HEADERS
from data.soap_payloads import get_case_start_payload
from data.soap_payloads import  *
from services.send_request import call_do_suspend

from utils.xml_utils import get_value_from_tag
from utils.logger_utils import get_logger
from utils.xml_beautify import beautify_xml

from services.do_case_start import call_do_case_start
from utils.parse_request_data import print_request_data
from utils.parse_response_data import print_response_data


import pytest
#//////////////////////////////////////////////////////////////////////////////
# Class Variables:
proc_carpool="carpool"
#//////////////////////////////////////////////////////////////////////////////
#Generate random numbner to be used in case desc
random_num1 = random.randint(1, 1000)  # ✅ Random number between 1 and 1000
case1_desc="carpool"+str(random_num1)

#//////////////////////////////////////////////////////////////////////////////
def test_do_suspend(logger):
    logger.info("========== Begin of test_do_suspend() ==========")    
    #/////////////////////////////////////////////////////////////////////
    # Pre-requisite: Start a case
    logger.info(f"Procedure Name = {proc_carpool}")
    logger.info(f"Case Description = {case1_desc}")
    response = call_do_case_start(proc_carpool, case1_desc)
    #/////////////////////////////////////////////////////////////////////
    # Verifications on case start response
    assert response.status_code == 200
    #/////////////////////////////////////////////////////////////////////
    # Extract case number
    case_number = get_value_from_tag(response.text, "return")
    logger.info(f"Case Number = {case_number}")
    assert case_number is not None and case_number != "" and int(case_number) > 0

    logger.info(f"--> End of pre-req of creating a case {case_number} !!")

    #/////////////////////////////////////////////////////////////////////
    logger.info(f"--> Begin of Suspending the case {case_number}")
    logger.info(f"Procedure Name = {proc_carpool}")
    logger.info(f"Case Number = {case_number}")
    # Suspending the case
    time.sleep(2)
    #/////////////////////////////////////////////////////////////////////
    # body = call_do_suspend("carpool", case_number)  
    #/////////////////////////////////////////////////////////////////////
    response =  call_do_suspend(proc_carpool, case_number)
    #/////////////////////////////////////////////////////////////////////
    # Verifications on case start response
    # ✅ Check if response is None or missing expected attributes
    if response is None:
        logger.error("Error: Response is None, test execution stopped prematurely!")
        pytest.fail("Test failed: Response object is None")
    #/////////////////////////////////////////////////////////////////////
    # ✅ Explicitly fail if response code is not 200
    if response.status_code != 200:
        logger.error(f"Test failed: Expected status code 200, but got {response.status_code}")
        pytest.fail(f"Test failed: Expected status code 200, but got {response.status_code}")
    #/////////////////////////////////////////////////////////////////////
    # ✅ Explicitly fail if response value is not 0
    return_value = get_value_from_tag(response.text, "return")
    logger.info(f"Return Value = {return_value}")
    #assert case_number is not None and case_number != "" and int(case_number) > 0
    if int(return_value) !=0:
        logger.error(f"Test failed: Expected Return Value is 0, but got {return_value}")
        pytest.fail(f"Test failed: Expected Return Value is 0,  but got {return_value}")
    #/////////////////////////////////////////////////////////////////////
    logger.info("========== End of test_do_suspend() ==========")
