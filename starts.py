import json
# import urllib library
from urllib.request import urlopen 
import sys
from datetime import date
import datetime
import os


url = "https://api2.lowfuelmotorsport.com/api/users/getUserStats/1704"
response = urlopen(url)
data = json.loads(response.read())

print(str(int(data["starts"])+1))