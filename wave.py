import matplotlib.pyplot as plt
from pathlib import Path

p=Path.home()/"Documents"/"C++Projects"/"WaveSound"

file_x=p/"x"

x=[float(i) for i in file_x.read_text().splitlines()]

file_y=p/"waveformText"
y=[float(i) for i in file_y.read_text().splitlines()]
print(x)
print(y)
plt.plot(x[:10000],y[:10000])
plt.axis('off')
plt.show()