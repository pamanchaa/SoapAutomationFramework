'''
Created on May 14, 2025

@author: Prashanth.Amancha
'''
# src/utils/logger_utils.py
import logging
from colorama import Fore, Style

# Define a custom formatter
class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.BLUE,      # Blue for debug
        logging.INFO: Fore.GREEN,      # Green for info
        logging.WARNING: Fore.YELLOW,  # Yellow for warnings
        logging.ERROR: Fore.RED,       # Red for errors
        logging.CRITICAL: Fore.RED + Style.BRIGHT,  # Bright red for critical errors
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, Style.RESET_ALL)  # Default color reset
        return f"{log_color}{super().format(record)}{Style.RESET_ALL}"

# Function to get a logger with color formatting
def get_logger(name: str = "SoapAutomationLogger") -> logging.Logger:
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # Set logger level to DEBUG to capture all messages
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Ensure handler captures all levels
        
        # Use the custom color formatter
        formatter = ColorFormatter('\n%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        logger.propagate = False  # Prevent duplicate logs
    
    return logger

# Example usage
logger = get_logger()
logger.debug("This is a debug message.")    # Blue
logger.info("This is an info message.")     # Green
logger.warning("This is a warning message.") # Yellow
logger.error("This is an error message.")   # Red
logger.critical("This is a critical error.") # Bright Red

