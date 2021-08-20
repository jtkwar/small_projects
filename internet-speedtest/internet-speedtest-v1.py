import speedtest
import pandas as pd
import numpy as np
from tqdm import tqdm
import time
from datetime import datetime


def main():
	date = datetime.today().strftime('%Y-%m-%d')
	out = []
	for i in tqdm(range(24), desc='Hourly Progress'):
		wifi = speedtest.Speedtest()
		
		# download and upload speed (in MB/s)
		down = wifi.download() / 1024 / 1024
		up     = wifi.download() / 1024 / 1024
		
		wifi.get_servers([])
		ping = wifi.results.ping
		
		print("\n")
		print(f"Download Speed: {down} MB/s")
		print(f"Upload Speed: {up} MB/s")
		print(f"Ping: {ping} ms")
		
		out.append([down, up, ping])
		
		for i in tqdm(range(3600), desc='Wait Time'):
			time.sleep(1)
	
	df = pd.DataFrame(out)
	df.columns = ['Download-Speed', 'Upload-Speed', 'Ping']
	df.to_csv(f"{date}_internet_speed_test.csv", index=False)
			

if __name__ == '__main__':
	main()
		