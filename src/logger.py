import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(LOGS_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOGS_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

