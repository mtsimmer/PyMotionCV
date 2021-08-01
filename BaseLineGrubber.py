#Building some TestBase

http://195.223.180.50/cam_1.jpg

import requests
import time

BASEFILE = "0.0.0.0_"
resp = requests.request("GET","http://195.223.180.50/cam_1.jpg")
counter = 0
while True:
	time.sleep(1)
	resp = requests.request("GET","http://195.223.180.50/cam_1.jpg")
	with open(BASEFILE+str(counter)+".jpeg",'wb') as f:
		f.write(resp.content)
		counter += 1
