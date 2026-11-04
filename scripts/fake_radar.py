import random
import time

with open("data/radar.log","w") as f:
	for i in range(60):
		distance = max(1.5,4.0 - 0.1*i)+random.gauss(0,0.05)
		if random.random() < 0.01:
			distance = -1.0
		f.write(f"{i*0.5:.1f},{distance:.2f}\n")
		f.flush()
		print("sleepeveryday")
		time.sleep(0.5)

