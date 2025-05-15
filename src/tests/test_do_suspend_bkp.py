'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
import requests

from config.config import BASE_URL, HEADERS
from data.soap_payloads import get_case_start_payload
from data.soap_payloads import  *
from services.send_request import call_do_suspend

from utils.xml_utils import get_value_from_tag
from utils.logger_utils import get_logger
from utils.xml_beautify import beautify_xml

from services.do_case_start import call_do_case_start


def test_do_suspend(logger):
    logger.info("==========Begin of test_do_suspend()==========")
    #//////////////////////////////////////////////////////////////////////////////////
    response = call_do_case_start("carpool", "Testing case start")
    ##logger.info(f"Response Text = {response.text}")    
    beautify_response = beautify_xml(response.text)
    logger.info(f"Response Text = {beautify_response }")
    #//////////////////////////////////////////////////////////////////////////////////
    logger.info(f"Status Code = {response.status_code}")    
    assert response.status_code == 200
    #//////////////////////////////////////////////////////////////////////////////////
    case_number = get_value_from_tag(response.text, "return")
    logger.info(f"Case Number  = {case_number}")
    #//////////////////////////////////////////////////////////////////////////////////
    assert case_number is not None and case_number != "" and int(case_number) > 0
    #////////////////////////////////////////////////////////////////////////////////// 
    logger.info(f"--> End of pre req of creating a case {case_number} !!")
    #//////////////////////////////////////////////////////////////////////////////////
    logger.info(f"--> Begin of Suspending the case {case_number} ")
    #//////////////////////////////////////////////////////////////////////////////////
    body = call_do_suspend("carpool", "{case_number}")
    #//////////////////////////////////////////////////////////////////////////////////
    response = requests.post(BASE_URL + "doSuspend", data=body, headers=HEADERS)
    beautify_response = beautify_xml(response.text)
    logger.info(f"Response Text = {beautify_response }")
     #//////////////////////////////////////////////////////////////////////////////////
    logger.info(f"Status Code = {response.status_code}")    
    assert response.status_code == 200
    #//////////////////////////////////////////////////////////////////////////////////
    logger.info("==========End of test_do_suspend()==========")