import logging
import os
from datetime import datetime

# Generate log file name with timestamp
log_file = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") + ".log"

# Create logs directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Full path of the log file
log_file_path = os.path.join(log_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] [Line:%(lineno)d] [%(name)s] - %(message)s"
)

