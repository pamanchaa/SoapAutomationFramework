'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
import pytest
import os
import sys


import pytest
import os
import sys
import pytest
import datetime



# ✅ Add 'src' to Python's module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.logger_utils import get_logger  # ✅ Now Python can find 'utils'

project_path = os.getcwd()
print("Current Project Path:", project_path)


    
# Define a mapping between services and test files
SERVICE_TEST_MAPPING = {
   
    
    # "do_suspend": "tests/test_do_suspend.py",
    # "case_start": "tests/test_case_start.py", 
       
    # "do_suspend": "test_do_suspend.py",
    # "case_start": "test_case_start.py",
    
    # "doSuspend": "{project_path}/test_do_suspend.py",
    # "doCaseStart":"{project_path}/test_case_start.py",
    # "getNodeName":"{project_path}/test_get_nodename.py"
    
    "doSuspend": "test_do_suspend.py",
    "doCaseStart":"test_case_start.py",
    "getNodeName":"test_get_nodename.py"



}

def get_tests_to_run(logger):
    """Reads test_services.txt and returns a list of test files to run."""
    test_files = []
    config_file = os.path.join(os.path.dirname(__file__), "test_services.txt")

    try:
        with open(config_file, "r") as file:
            services = file.read().splitlines()
            logger.info(f"Services to be tested: {services}")
            for service in services:
                if service in SERVICE_TEST_MAPPING:
                    test_files.append(SERVICE_TEST_MAPPING[service])
                else:
                    logger.warning(f"No test case mapped for service '{service}'")
    except FileNotFoundError:
        logger.error("Error: test_services.txt not found.")
    
    logger.info(f"Test files selected: {test_files}")
    return test_files

def run_tests(logger):
    """Executes pytest for the selected test cases with command-line options."""
    test_files = get_tests_to_run(logger)
    logger.info(f"Final test cases to run = {test_files}")
    
    if test_files:
        # Worked
        
        # pytest_args = test_files + sys.argv[1:]  # ✅ Append command-line arguments        
        # logger.info(f"Final command to run = {pytest_args}")
        # pytest.main(pytest_args)  # ✅ Explicitly pass test files
        
         #////////////////////////////////////////////////////////////////////////////////////
         final_testcases_list_arg=test_files
         #////////////////////////////////////////////////////////////////////////////////////
         # Generate timestamp (YYYYMMDD_HHMMSS format)
         timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H%M%S")
         # Define the report name with the timestamp
         report_filename = f"--html=results/report_{timestamp}.html"
         #////////////////////////////////////////////////////////////////////////////////////
         final_report_name_arg = report_filename
         #////////////////////////////////////////////////////////////////////////////////////
         final_html_type_arg="--self-contained-html"
         #////////////////////////////////////////////////////////////////////////////////////
         final_existing_system_arg=sys.argv[1:]
         #////////////////////////////////////////////////////////////////////////////////////
         final_pytest_args = final_testcases_list_arg  +[final_report_name_arg] + [final_html_type_arg] + final_existing_system_arg
         logger.info(f"Final command to run = {final_pytest_args}")
          #////////////////////////////////////////////////////////////////////////////////////
        # pytest_args = test_files + sys.argv[1:]
        
         # Run pytest with the dynamic report name
         pytest.main(final_pytest_args)
         #pytest.main(pytest_args)  # ✅ Explicitly pass test files
    else:
        logger.warning("No valid test cases found to run.")

if __name__ == "__main__":
    logger_instance = get_logger()  # ✅ Initialize logger manually
    run_tests(logger_instance)  # ✅ Pass logger explicitly



##Example to run this is -->  python run_tests.py -s --html=report.html  (navigaet to C:\Users\Prashanth.Amancha\eclipse-workspace\SoapAutomationFramework\src\tests)
##In eclipse, under Run > External Tools > Arguments --> C:\Users\Prashanth.Amancha\eclipse-workspace\SoapAutomationFramework\src\tests\run_tests.py -s --html=report.html --self-contained-html