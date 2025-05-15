'''
Created on May 13, 2025

@author: Prashanth.Amancha
'''
import random
from services.do_case_start import call_do_case_start
from utils.xml_utils import get_value_from_tag
from utils.logger_utils import get_logger
from utils.xml_beautify import beautify_xml

#//////////////////////////////////////////////////////////////////////////////
# Class Variables:
proc_carpool="carpool"
#//////////////////////////////////////////////////////////////////////////////
#Generate random numbner to be used in case desc
random_num1 = random.randint(1, 1000)  # ✅ Random number between 1 and 1000
case1_desc="carpool"+str(random_num1)

#//////////////////////////////////////////////////////////////////////////////
#Functions:

def test_case_start(logger):
    logger.info("==========Begin of test_case_start()==========")
    #//////////////////////////////////////////////////////////////////////////////////
    logger.info(f"Procedure Name = {proc_carpool}")
    logger.info(f"Case Description = {case1_desc}")
    response = call_do_case_start(proc_carpool, case1_desc)
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
    logger.info("==========End of test_case_start()==========")
#//////////////////////////////////////////////////////////////////////////////