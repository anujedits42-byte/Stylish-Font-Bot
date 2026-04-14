import os
from typing import List

API_ID = os.environ.get("API_ID", "34724970")
API_HASH = os.environ.get("API_HASH", "f240eae7c60e8e30c17203ab0e052f7e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8707891981:AAGHOAc6F5lwnLf8R1zBfm2V9PSdelfm010")
PICS = (os.environ.get("PICS", "https://h.uguu.se/rcbHaRWs.jpg https://o.uguu.se/qHEASLdi.jpg https://h.uguu.se/xWxZoSwD.jpg https://d.uguu.se/hSmYCiBy.jpg https://h.uguu.se/suePRbGS.jpg")).split()
ADMIN = int(os.environ.get("ADMIN", "7892805795"))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003475522251"))
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Anujedit")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
