'''import logging 
import os
from from_root import from_root
from datetime import datetime

now=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

log_file_name=f'{now}.log'

folder="file_artifacts"

print(from_root())

folder="file_artifacts"

file_path=os.path.join(from_root(),folder,log_file_name)

os.makedirs(os.path.dirname(file_path), exist_ok=True)

os.makedirs()
logging.basicConfig(
    level=logging.INFO,
    force=True,
    format='(%(asctime)s - %(levelname)s - %(message)s)',
    filename=log_file_name
)'''

import logging 
import os
from datetime import datetime
from from_root import from_root  # Note: Ensure you run 'pip install from-root' in your terminal

# 1. Generate timestamped log filename
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_name = f'{now}.log'

# 2. Define the folder name
folder = "file_artifacts"

# 3. Create the absolute path pointing inside your project root
file_path = os.path.join(from_root(), folder, log_file_name)

# 4. Extract the directory portion of the path and create it safely
# This ensures "file_artifacts" is created directly inside your project root
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# 5. Configure the Logging Pipeline
logging.basicConfig(
    level=logging.INFO,
    force=True,
    format='(%(asctime)s - %(levelname)s - %(message)s)',
    filename=log_file_name  # Use the timestamped log filename
)

# Test it
logging.info("Logging infrastructure is perfectly configured!")
