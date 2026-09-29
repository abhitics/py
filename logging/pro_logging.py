import logging
import sys

# 1. Initialize a dedicated child logger for our module
# Using __name__ automatically names this logger after your python file!
logger = logging.getLogger(__name__) 

# Set the logger's main gate to the lowest level (DEBUG) 
# so it doesn't accidentally block messages too early.
logger.setLevel(logging.DEBUG)

# Prevent messages from traveling up to the root logger and duplicating
logger.propagate = False

# 2. Design our message look (The Formatter)
formatter = logging.Formatter("%(asctime)s | [%(levelname)s] | %(filename)s:%(lineno)d | %(message)s")

# 3. Create a Console Handler (For standard viewing)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO) # Screen ignores detailed DEBUG stuff
console_handler.setFormatter(formatter)

# 4. Create a File Handler (For critical error tracking)
file_handler = logging.FileHandler("app_errors.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.ERROR) # File ignores INFO/DEBUG; only saves major errors
file_handler.setFormatter(formatter)

# 5. Connect both paths to our logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# --- Put it to work ---
logger.debug("Testing local variable x=10.") # Silent everywhere (Both handlers reject level 10)
logger.info("Server is listening on port 8080.") # Shows ONLY on Console Screen
logger.error("Database connection lost!") # Shows on Console Screen AND writes to app_errors.log
