import os
import logging
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")


logging.basicConfig(
    filename="logs/run.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def log_step(step, detail):
    logging.info(f"{step}: {detail}")
    print(f"[{step}] {detail}")  
