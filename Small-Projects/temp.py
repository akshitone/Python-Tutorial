import time
import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'screenshots')
print(FILE_PATH)
print(BASE_DIR)
print(TEMPLATE_DIR)
# print(int(round(time.time() * 1000)))
