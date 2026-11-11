import numpy as np
import matplotlib.pyplot as plt

fs=1000
duration = 1.0
f0=20 + 8
noise =0.8
t=np.arange(0,duration,1 / fs)
x=np.sin(2*np.pi*f0*t)+noise * np.random.default_rng().normal(size=t.size)
spec=np.abs(np.fft.rfft(x))
freqs=np.fft.rfftfreq(t.size,1/fs)
peak_freq=freqs[np.argmax(spec)]
print(f"频率:{peak_freq:.2f} Hz")
fig,axs=plt.subplots(2,1)
axs[0].plot(t[:200],x[:200])
axs[1].plot(freqs,spec)
plt.savefig("output/fft.png")

