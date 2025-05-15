'''
Created on May 13, 2025

@author: Prashanth.Amancha
'''
import requests

from config.config import BASE_URL, HEADERS
from data.soap_payloads import get_case_start_payload
from data.soap_payloads import  *


def call_do_case_start(proc_name, case_desc):
    body = get_case_start_payload(proc_name, case_desc)
    response = requests.post(BASE_URL + "doCaseStart", data=body, headers=HEADERS)
    return response

def call_do_suspend(proc_name, case_num):
    body = get_do_suspend(proc_name, case_num)
    response = requests.post(BASE_URL + "doSuspend", data=body, headers=HEADERS)
    return response

