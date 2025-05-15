'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
import requests
import time

#from config.config import BASE_URL, HEADERS
from config.config import *
from data.soap_payloads import get_case_start_payload
from data.soap_payloads import  *
from services.send_request import call_do_suspend
from services.send_request import call_get_nodename

from utils.xml_utils import get_value_from_tag
from utils.logger_utils import get_logger
from utils.xml_beautify import beautify_xml

from services.do_case_start import call_do_case_start
from utils.parse_request_data import print_request_data
from utils.parse_response_data import print_response_data


import pytest



def test_get_nodename(logger):
    logger.info("========== Begin of test_do_suspend() ==========")    
    #/////////////////////////////////////////////////////////////////////
    response = call_get_nodename()
    #/////////////////////////////////////////////////////////////////////
    # Verifications on getNodename response
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
    #expected_nodename="staffw_nod46UPGD"
    expected_nodename=nodename
    if return_value !=expected_nodename:
        logger.error(f"Test failed: Expected Return Value is {expected_nodename}, but got {return_value}")
        pytest.fail(f"Test failed: Expected Return Value is {expected_nodename},  but got {return_value}")
    #/////////////////////////////////////////////////////////////////////
    logger.info("========== End of test_do_suspend() ==========")