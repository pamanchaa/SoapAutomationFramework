'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''

import pytest
from utils.logger_utils import get_logger  # Import logger function from utils

@pytest.fixture(scope="session")
def logger():
    """Creates a logger instance for the entire test suite."""
    return get_logger()  # Use the logger from logger_utils.py

